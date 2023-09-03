class Stack():
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, value):
        self.stack.append(value)
        self.top += 1
    
    def pop(self):
        if not self.top == 0:
            self.top -= 1
            return self.stack.pop(self.top)
        print('Nothing to pop')

    def empty(self):
        self.stack.empty()
        self.top = 0

    def display(self):
        print(self.stack)

s = Stack()

s.pop()
s.push(1)
s.push(2)
s.display()
s.pop()
s.display()
