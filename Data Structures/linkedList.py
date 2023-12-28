class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head is None:
            print('is empty')
            return 0
        else:
            return 1
    def traversal(self):
        cur = self.head
        while cur is not None:
            print("-->", cur.data)
            cur = cur.next
    def add_begin(self, data):
        cur = Node(data)
        cur.next = self.head
        self.head = cur
    def add_end(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
    def add_between(self, data, x, c):
        if c == 1:
            if self.head == None:
                print('list is empty')
            else:
                cur = self.head
                if cur.data == x:
                    self.add_begin(data)
                    return
                while cur.next is not None:
                    if cur.next.data == x:
                        break
                    cur = cur.next
                if cur.next is None:
                    print('list has not this data')
                else:
                    new_node = Node(data)
                    new_node.next = cur.next
                    cur.next = new_node
        if c == 0:
            if self.head == None:
                print('list is empty')
            else:
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
                    cur.next = new_node
    def delete_begin(self):
        if self.is_empty():
            self.head = self.head.next
    def delete_end(self):
        if self.is_empty():
            cur = self.head
            if cur.next is None:
                self.delete_begin()
            else:
                while cur.next.next is not None:
                    cur = cur.next
                cur.next = None

    def delete_between(self, x):
        if self.is_empty():
            cur = self.head
            while cur is not None:
                if cur.data == x:
                    break
                cur = cur.next
            if cur is None:
                print('list has not this data')
            elif cur.next is None:
                return
            else:
                cur.next = cur.next.next

llist = LinkedList()
llist.add_begin(2)
llist.add_begin(5)
llist.add_end(6)
llist.add_between(3, 5, 1)
llist.delete_between(6)
llist.traversal()