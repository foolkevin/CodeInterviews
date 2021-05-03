class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataStack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.dataStack.append(x)
        if not self.minStack:
            self.minStack.append(x)
            return
        if x < self.minStack[-1]:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if not self.dataStack:
            return
        self.dataStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if not self.dataStack:
            return None
        return self.dataStack[-1]

    def min(self) -> int:
        if not self.minStack:
            return None
        return self.minStack[-1]
