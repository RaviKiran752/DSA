stack = []
stack.append(1)  # Push
stack.append(2)
stack.pop()  # Pop (removes 2)


#using class
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

# Usage
s = Stack()
s.push(1)
s.push(2)
print(s.pop())  # Output: 2
