# Stacks 
    #  Last-in First-out
    #  All push and pop operation are to|from the top of the stack

# Stack operations
    # append() || push() :: Add an item to the top of the stack
    # pop() :: Pop the first item from the stack
    # peek() :: Get an item on top of the stack without removing it
    # clear() :: Clear all the items from the stack


# Stack using list with a wrapper class
class Stack():
    # class constructor
    def __init__(self):
        # Creating a list
        self.stack = list()

    # Add item to stack
    def push(self, item):
        self.stack.append(item)

    # Pop the top item from list
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    # Peek
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
        
    # Print stack
    def __str__(self):
        return str(self.stack)

myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack)
print(myStack.pop(), myStack)
print(myStack.peek())