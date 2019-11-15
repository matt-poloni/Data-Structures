import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = self.len()

    def pop(self):
        if self.len() > 0:
            self.size = self.len() - 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length
