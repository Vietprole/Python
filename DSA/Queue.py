class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
    
# Queue in python
# Creating a queue
queue = Queue()
# Some operations on the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.size())  # Output: 2
print(queue.dequeue())  # Output: 2
