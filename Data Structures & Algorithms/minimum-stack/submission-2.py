class MinStack:

    def __init__(self):
        self.data = []
        self.currentMin = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.currentMin:
            self.currentMin.append(val)
        else:
            if self.currentMin[-1] >= val:
                self.currentMin.append(val)

    def pop(self) -> None:
        removed = self.data.pop()
        if removed == self.currentMin[-1]:
            self.currentMin.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.currentMin[-1]
