# Here, we are implementing stack using list

# Creating an empty stack in stack class
class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    # Function to push the value into the stack
    # Time complexity for the push operation is O(1)
    def push(self, value):
        self.stack.append(value)
        self.top += 1

    # Function to pop value from the stack
    # Time complexity is O(1)
    def pop(self,value):
        if self.stack is None:
            print("The stack is empty")
            return
        self.stack.remove(value)
        self.top -= 1

    def print_stack(self):
        print(self.stack)

stack = Stack()
stack.push(5)
stack.push(2)
stack.push(6)
stack.push(8)
stack.push(10)
stack.print_stack()
