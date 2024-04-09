class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next
        def disconnect(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return (len(self) == 0)
    
    def add_after(self, node, val):
        new_node = SinglyLinkedList.Node(val)
        if node is self.tail:
            self.tail = new_node
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        self.size += 1
        return new_node
    
    def add_first(self, val):
        new_node = SinglyLinkedList.Node(val)
        if len(self) == 0:
            self.header = new_node
            self.tail = new_node
        else:
            original_header = self.header
            new_node.next = original_header
            self.header = new_node
        self.size += 1
        return new_node
    
    def add_last(self, val):
        if len(self) == 0:
            new_node = SinglyLinkedList.Node(val)
            self.header = new_node
            self.tail = new_node
            self.size += 1
            return new_node
        return self.add_after(self.tail, val)
    
    def delete_frist(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        data = self.header.data
        self.header = self.header.next
        self.size -= 1
        return data
    
    def delete_last(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        data = self.tail.data
        cur = self.header
        while not (cur.next is self.tail):
            cur = cur.next
        cur.next = None
        self.size -= 1
        return data
    
    # def reverse(self):
        