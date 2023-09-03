class Queue():
    def __init__(self):
        self.queue = []
        self.top = 0

    def enqueue(self, value):
        self.queue.append(value)
        self.top += 1
    
    def dequeue(self):
        if not self.top == 0:
            self.top -= 1
            return self.queue.pop(0)
        print('Nothing to DeQueue')

    def flush(self):
        self.queue.empty()
        self.top = 0

    def display(self):
        print(self.queue)

s = Queue()

s.dequeue()
s.enqueue(1)
s.enqueue(2)
s.display()
s.dequeue()
s.display()
