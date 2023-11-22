# Problem: https://leetcode.com/problems/min-stack/

# Pattern: Keep track of 2 stacks - 1 for all the values, and 1 for all the
# minimum values

# Time complexity: O(1) per operations
# Space complexity: O(n)


class MinStack:
    def __init__(self) -> None:
        self.items: list[int] = []
        self.mins: list[int] = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if len(self.mins) == 0 or self.mins[-1] >= val:
            self.mins.append(val)

    def pop(self) -> None:
        removed: int = self.items.pop()
        if self.mins[-1] == removed:
            self.mins.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.mins[-1]


def main():
    minStack: MinStack = MinStack()

    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # Expected: -3
    minStack.pop()
    print(minStack.top())  # Expected: 0
    print(minStack.getMin())  # Expected: -2


if __name__ == "__main__":
    main()
