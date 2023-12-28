class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLList:
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
            print(cur.data, end='')
            cur = cur.next
            while cur != self.head:
                print("-->", cur.data, end='')
                cur = cur.next
            print("-->", self.head.data)
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            self.head = new_node
    def add_before(self, data, x):
        if self.is_empty():
            if self.head.data == x:
                new_node = Node(data)
                new_node.next = self.head.next
                self.head.next = new_node
                return
            cur = self.head.next
            while cur.next != self.head:
                if cur.data == x:
                    break
                cur = cur.next
            if (cur.next == self.head) & (cur.data != x):
                print('list has not this data')
            else:
                new_node = Node(data)
                new_node.next = cur.next
                cur.next = new_node
    def delete(self, data):
        if self.is_empty():
            if self.head.data == data:
                cur = self.head
                if cur == cur.next:
                    self.head = None
                while cur.next != self.head:
                    cur = cur.next
                self.head = self.head.next
                cur.next = self.head
            else:
                cur = self.head
                while cur.next != self.head:
                    if cur.next.data == data:
                        break
                    cur = cur.next
                if cur.next == self.head:
                    print('list has not this data')
                else:
                    cur.next = cur.next.next

cll = CircularLList()
cll.add_begin(5)
cll.add_begin(6)
cll.add_begin(2)
cll.add_before(1, 6)
cll.add_before(8, 5)
cll.delete(2)
cll.traversal()