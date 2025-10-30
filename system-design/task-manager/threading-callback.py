import time
import random
import threading
import uuid
from queue import Queue
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Callable, Optional, Any, Tuple

class TaskStatus(Enum):
    """Status states for concurrent tasks."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Task:
    """Represents a task with execution state and callback."""
    id: str
    func: Callable
    args: Tuple
    callback: Optional[Callable] = None
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    error: Optional[str] = None

class TaskManager:
    """Manages task execution with worker thread pool and callbacks."""

    def __init__(self, num_workers: int = 3) -> None:
        """Initialize TaskManager with specified number of worker threads.

        Args:
            num_workers: Number of concurrent worker threads. Defaults to 3.
        """
        self.queue: Queue[str] = Queue()
        self.tasks: Dict[str, Task] = {}
        self.workers: list[threading.Thread] = []

        for _ in range(num_workers):
            worker = threading.Thread(target=self._worker, daemon=True)
            worker.start()
            self.workers.append(worker)

    def submit(self, func: Callable, *args, callback: Optional[Callable] = None) -> str:
        """Submit a function for execution in a worker thread.

        Args:
            func: A callable to execute.
            *args: Positional arguments to pass to the function.
            callback: Optional callable to invoke upon task completion.

        Returns:
            Task ID string for tracking the task.
        """
        task_id = str(uuid.uuid4())
        task = Task(id=task_id, func=func, args=args, callback=callback)
        self.tasks[task_id] = task
        self.queue.put(task_id)
        return task_id

    def get_status(self, task_id: str) -> Optional[Task]:
        """Get the status and result of a task.

        Args:
            task_id: ID of the task to retrieve.

        Returns:
            Task object or None if task_id not found.
        """
        return self.tasks.get(task_id)

    def _worker(self) -> None:
        """Worker thread that processes tasks from the queue.

        Continuously pulls tasks from the queue, executes them, handles errors,
        and invokes the callback upon completion.
        """
        while True:
            task_id = self.queue.get()
            task = self.tasks[task_id]
            task.status = TaskStatus.RUNNING

            try:
                task.result = task.func(*task.args)
                task.status = TaskStatus.COMPLETED
            except Exception as e:
                task.error = str(e)
                task.status = TaskStatus.FAILED
            finally:
                if task.callback:
                    task.callback(task)

            self.queue.task_done()

def long_task() -> str:
    """Simulate a long-running IO task.

    Returns:
        A message indicating sleep duration in seconds.
    """
    n = random.randint(1, 10)
    time.sleep(n)
    return f"Slept for {n} seconds"

def on_complete(task: Task) -> None:
    """Print task completion status and result.

    Args:
        task: The completed Task object.
    """
    if task.status == TaskStatus.COMPLETED:
        print(f"Task {task.id} done: {task.result}")
    else:
        print(f"Task {task.id} failed: {task.error}")

def main() -> None:
    """Main entry point for task execution demo.

    Creates a TaskManager with worker threads, submits multiple tasks,
    registers callbacks, and waits for all tasks to complete.
    """
    manager = TaskManager(num_workers=4)

    task_ids = []
    for _ in range(random.randint(5,10)):
        task_ids.append(manager.submit(long_task, callback=on_complete))

    print(f"Submitted: {task_ids}")

    # Wait for all tasks to complete
    manager.queue.join()
    print("All tasks completed")

if __name__ == "__main__":
    main()
