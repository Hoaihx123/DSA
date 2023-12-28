class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head is None:
            print('is empty')
            return 0
        else:
            return 1
    def traversal(self):
        if self.is_empty():
            cur = self.head
            while cur is not None:
                print("-->", cur.data)
                cur = cur.next
    def add_begin(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def add_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            new_node = Node(data)
            new_node.prev = cur
            cur.next = new_node
    def add_between(self, data, x):
        if self.is_empty():
            cur = self.head
            while cur is not None:
                if cur.data == x:
                    break
                cur = cur.next
            if cur is None:
                print('list has not this data')
            else:
                new_node = Node(data)
                new_node.next = cur.next
                if cur.next is not None:
                    new_node.next.prev = new_node
                new_node.prev = cur
                cur.next = new_node
    def delete(self, x):
        if self.is_empty():
            cur = self.head
            if cur.data == x:
                if cur.next is not None:
                    cur.next.prev = None
                    self.head = cur.next
                    del cur
                else:
                    self.head = None
                return
            while cur is not None:
                if cur.data == x:
                    break
                cur = cur.next
            if cur is None:
                print('list has not this data')
            else:
                cur.prev.next = cur.next
                if cur.next is not None:
                    cur.next.prev = cur.prev
                del cur

dll = DoublyLList()
dll.add_end(5)
dll.add_begin(2)
dll.add_begin(1)
dll.add_end(8)
dll.add_between(0, 8)
dll.delete(5)
dll.traversal()