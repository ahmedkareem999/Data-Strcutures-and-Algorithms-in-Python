# Here we are implementing stack using linked list
# Time complexity is O(1) and Space Complexity is O(n)

# created an empty node in node class
class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

# created an empty stack in stack class
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    # function to push data into the stack
    # Time complexity of push operation is O(1)
    def push(self,data):
        node = Node(data) # initialising node as object
        if node is None:
            print("Stack is empty")
            return
        node.data = data
        node.next = self.top
        self.top = node
        self.count += 1

    # Function to pop the top element from the stack
    # Time Complexity of pop operation is O(1)
    def pop(self):
        if self.top is None: # checking if stack is empty
            print("Stack is empty")
            return
        else:
            self.count -= 1
            top = self.top.data
            self.top.data = self.top.next
            return top

    # Function to print the elements ofthe stack in the form of linkedlist
    def print_stack(self):
        if self.top is None:
            print("Stack is Empty")
            return
        while self.top is not None:
            print(self.top.data, "----->", end = " ")
            self.top = self.top.next

stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('print')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        stack.push(int(do[1]))
    elif operation == 'pop':
        popped = stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'print':
        print("\nThe elements present in the stack that are represented in the form of linked list are:\n")
        stack.print_stack()
        break
    elif operation == 'quit':
        break
