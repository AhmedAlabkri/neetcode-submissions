class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        #self.minVal = minVal
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))
        

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minstack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
