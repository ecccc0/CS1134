from DoublyLinkedList import *
class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, e):
        self.data.add_last(e)
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.header.next.data
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.delete_first()
    