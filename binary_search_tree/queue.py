"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   A queue is a container of objects that are inserted and removed according to the first-in first-out (FIFO) principle
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# ### Queues
#  * Has the methods: `enqueue`, `dequeue`, and `len`.
#    * `enqueue` adds an element to the back of the queue.
#    * `dequeue` removes and returns the element at the front of the queue.
#    * `len` returns the number of elements in the queue.

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size == 0:
#             return
#         else:
#             self.size -= 1
#             return self.storage.pop(0)

from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_head()