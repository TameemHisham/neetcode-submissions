class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None: 
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        # print()
        # print("PUSH")
        # print("stack:", self.stack)
        # print("minStack:", self.minStack)
        # print("MinVal:", self.minVal)
        # print('topPointer', self.topPointer)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        # print()
        # print("POP")
        # print("stack:", self.stack)
        # print("minStack:", self.minStack)
        # print("MinVal:", self.minVal)
        # print('topPointer', self.topPointer)

    def top(self) -> int:
        # print()
        # print("minStack:", self.minStack)
        # print("MinVal:", self.minVal)
        # print('topPointer', self.topPointer)
        return self.stack[-1]

    def getMin(self) -> int:
        # print()
        # print("MIN")
        # print("stack:", self.stack)
        # print("minStack:", self.minStack)
        # print("MinVal:", self.minVal)
        # print('topPointer', self.topPointer)
        return self.minStack[-1]
        
        
