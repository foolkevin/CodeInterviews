from collections import deque

class MaxQueue:
    def __init__(self):
        self.maxQueue = deque()
        self.valQueue = deque()

    def max_value(self) -> int:
        if len(self.maxQueue) == 0: return -1
        return self.maxQueue[0]

    def push_back(self, value: int) -> None:
        self.valQueue.append(value)
        if len(self.maxQueue) == 0:
            self.maxQueue.append(value)
            return
        while self.maxQueue[-1] < value:
            self.maxQueue.pop()
        self.maxQueue.append(value)
    
    def pop_front(self) -> int:
        if len(self.valQueue) == 0: return -1
        if self.valQueue[0] == self.maxQueue[0]:
            self.maxQueue.popleft()
        return self.valQueue.popleft()

        