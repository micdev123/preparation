# Queues
    # First-In First-Out

# Queues operations
    # Enqueue :: Add an item to the end of the line
    # Dequeue :: Remove an item from the front of the line

# Deque is double-ended queue. Can be used for queue

# Queue operation
    # append() :: To enqueue an item
    # popleft() :: To dequeue an item


# Import
from collections import deque

# Creating a queue
myQueue = deque()

# Adding an items
myQueue.append(1)
myQueue.append(2)

# print(myQueue)

# Pop first item
# print(myQueue.popleft())

class Queue():
    def __init__(self):
        self.queue = deque()

    # enqueue item to queue
    def enqueue(self, item):
        self.queue.append(item)

    # dequeue item from queue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None

    # Get queue size
    def get_size(self):
        return len(self.queue)

    # Get queue items
    def __str__(self):
        return str(self.queue)


myQueue = Queue()

# Adding item in queue
myQueue.enqueue(3)
myQueue.enqueue(4)

# Print queue size
print(myQueue.get_size())

# Print queue items
print(myQueue)

# Pop first item in queue
print(myQueue.dequeue(), myQueue)
    