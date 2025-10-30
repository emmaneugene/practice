import asyncio
import random
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Callable, Coroutine, Any, List, Optional

class TaskStatus(Enum):
    """Status states for async tasks."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Task:
    """Represents an async task with execution state and callbacks."""
    id: str
    coro: Coroutine
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    error: Optional[str] = None
    callbacks: List[Callable] = field(default_factory=list)

class TaskManager:
    """Manages async task execution with worker pool and callbacks."""

    def __init__(self, num_workers: int = 3) -> None:
        """Initialize TaskManager with specified number of worker coroutines.

        Args:
            num_workers: Number of concurrent worker tasks. Defaults to 3.
        """
        self.queue: asyncio.Queue[str] = asyncio.Queue()
        self.tasks: Dict[str, Task] = {}
        self.num_workers = num_workers

    async def start(self) -> List[asyncio.Task]:
        """Start worker coroutines.

        Returns:
            List of asyncio.Task objects for the worker coroutines.
        """
        workers = [
            asyncio.create_task(self._worker())
            for _ in range(self.num_workers)
        ]
        return workers

    def submit(self, coro: Coroutine) -> str:
        """Submit a coroutine for execution.

        Args:
            coro: A coroutine object to execute.

        Returns:
            Task ID string for tracking the task.
        """
        task_id = str(uuid.uuid4())
        task = Task(id=task_id, coro=coro)
        self.tasks[task_id] = task
        self.queue.put_nowait(task_id)
        return task_id

    def on_complete(self, task_id: str, callback: Callable) -> None:
        """Register a callback to be invoked when task completes.

        Args:
            task_id: ID of the task to monitor.
            callback: Callable to invoke on completion (can be sync or async).
        """
        if task_id in self.tasks:
            self.tasks[task_id].callbacks.append(callback)

    def get_status(self, task_id: str) -> Optional[Task]:
        """Get the status and result of a task.

        Args:
            task_id: ID of the task to retrieve.

        Returns:
            Task object or None if task_id not found.
        """
        return self.tasks.get(task_id)

    async def _worker(self) -> None:
        """Worker coroutine that processes tasks from the queue.

        Continuously pulls tasks from the queue, executes them, handles errors,
        and invokes registered callbacks upon completion.
        """
        while True:
            task_id = await self.queue.get()
            task = self.tasks[task_id]
            task.status = TaskStatus.RUNNING

            try:
                task.result = await task.coro
                task.status = TaskStatus.COMPLETED
            except Exception as e:
                task.error = str(e)
                task.status = TaskStatus.FAILED

            # Invoke callbacks
            for callback in task.callbacks:
                if asyncio.iscoroutinefunction(callback):
                    await callback(task)
                else:
                    callback(task)

            self.queue.task_done()

async def long_task() -> str:
    """Simulate a long-running IO task.

    Returns:
        A message indicating completion time in seconds.
    """
    n = random.randint(1, 10)
    await asyncio.sleep(n)
    return f"Completed IO in {n} seconds"

async def on_task_complete(task: Task) -> None:
    """Print task completion status and result.

    Args:
        task: The completed Task object.
    """
    print(f"Task {task.id}: {task.status.value}")
    if task.status == TaskStatus.COMPLETED:
        print(f"  Result: {task.result}")
    else:
        print(f"  Error: {task.error}")

async def main() -> None:
    """Main entry point for task execution demo.

    Creates a TaskManager with worker pool, submits multiple async tasks,
    registers callbacks, and waits for all tasks to complete.
    """
    manager = TaskManager(num_workers=4)
    await manager.start()

    # Submit tasks
    task_ids = []
    for _ in range(random.randint(5, 10)):
        task_id = manager.submit(long_task())
        manager.on_complete(task_id, on_task_complete)
        task_ids.append(task_id)

    print(f"Submitted: {task_ids}")

    # Wait for all tasks to complete
    await manager.queue.join()
    print("All tasks completed")

if __name__ == "__main__":
    asyncio.run(main())
