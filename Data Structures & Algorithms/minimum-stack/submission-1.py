class MinStack:

    def __init__(self):
        self.stack = []
        self.minmum = []
        self.minVal = 0
        

    def push(self, val: int) -> None:
        if not self.minmum:
            self.minVal = val
        else:
            self.minVal = min(self.minmum[-1], val)
        self.minmum.append(self.minVal)
        self.stack.append(val)
        # [3,1,4,5,2]
        # stack: [3]
        # minmum: [3]
    def pop(self) -> None:
        self.stack.pop(-1)
        self.minmum.pop(-1)
        if not self.minmum:
            self.minVal = 0
        else:
            self.minVal = self.minmum[-1]

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minmum[-1]



        
