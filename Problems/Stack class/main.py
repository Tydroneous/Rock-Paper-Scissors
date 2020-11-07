class Stack():

    def __init__(self):
        self.myStack = []

    def push(self, el):
        self.myStack.append(el)

    def pop(self):
        return self.myStack.pop()

    def peek(self):
        return self.myStack[len(self.myStack) - 1]

    def is_empty(self):
        return not self.myStack
