"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        return self.storage.insert(0,new_element)

    def peek(self):
        
        return self.storage[-1]

    def dequeue(self):
        return self.storage.pop()