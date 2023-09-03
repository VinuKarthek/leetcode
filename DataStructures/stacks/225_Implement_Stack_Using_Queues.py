#225. Implement Stack using Queues

class MyStack:

    def __init__(self):
        self.stack = []
        self.top_idx = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.top_idx += 1

    def pop(self) -> int:
        if not self.top_idx == 0:
            self.top_idx -= 1
            return(self.stack.pop(self.top_idx))

    def top(self) -> int:
        if self.top_idx == 0: return
        return(self.stack[self.top_idx])

    def empty(self) -> bool:
        return self.top_idx == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()