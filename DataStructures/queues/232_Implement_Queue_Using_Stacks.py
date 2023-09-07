#32. Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        self.stack = []
        self.top_idx = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.top_idx += 1

    def pop(self) -> int:
        if not self.top_idx == 0:
            self.top_idx -= 1
            return(self.stack.pop(0))

    def peek(self) -> int:
        if self.top_idx == 0: return
        return(self.stack[0])

    def empty(self) -> bool:
        return self.top_idx == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(10)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()