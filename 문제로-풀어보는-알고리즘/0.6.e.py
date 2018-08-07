class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.is_empty():
            return
        self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0

# Implement a queue with two stacks
class Queue:
    def __init__(self):
        self.stackOne = Stack()
        self.stackTwo = Stack()
    
    def enqueue(self, val):
        self.stackOne.push(val)
    
    def dequeue(self):
        if not self.stackTwo.size > 0:
            self.move_context()
        return self.stackTwo.pop()
    
    def move_context(self):
        while self.stackOne.size > 0:
            self.stackTwo.push(self.stackOne.pop())
