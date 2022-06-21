# implementing class stack
class Stack:
    def __init__(self,size):
        self.size = size
        self.arr = [None] * self.size
        self.top = -1

    # Inserting data into the stack
    # Time complexity: O(1)
    def push(self,data):
        if self.top == self.size - 1:
            print("Stack is Full")
            return
        self.top += 1
        self.arr[self.top] = data

    # Removing data from the Stack
    # Time complexity: O(1)
    def pop(self):
        if self.top == -1:
            print("Stack is Empty")
            return
        else:
            print(f"Popped element is: {self.arr[self.top]}")
            self.top -= 1

    def print_stack(self):
        if self.top == -1:
            print("Stack is Empty")
        print(self.arr)
stack = Stack(7)
stack.push(30)
stack.push(5)
stack.push(10)
stack.push(8)
stack.push(2)
stack.push(1)
stack.push(6)
stack.pop()
stack.pop()
stack.print_stack()
