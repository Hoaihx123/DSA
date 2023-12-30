class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def insert(self, key):
        if self.key is None:
            self.key = Node(key)
        else:
            if key > self.key:
                if self.right:
                    self.right.insert(key)
                else:
                    self.right = Node(key)
            elif key < self.key:
                if self.left:
                    self.left.insert(key)
                else:
                    self.left = Node(key)
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end=" ")
        if self.right:
            self.right.inorder()
    def preorder(self):
        print(self.key, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key, end=" ")
    def search(self, data):
        if self.key == data:
            print('data is found')
        elif self.key < data:
            if self.right is None:
                print('no find')
            else:
                self.right.search(data)
        else:
            if self.left is None:
                print('no find')
            else:
                self.left.search(data)
    def deletion(self, data):
        if self.key is None:
            print('tree is empty')
            return
        if data > self.key:
            if self.right:
                self.right = self.right.deletion(data)
            else:
                print('no find')
        elif data < self.key:
            if self.left:
                self.left = self.left.deletion(data)
            else:
                print('no find')
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            cur = self.right
            while cur.left:
                cur = cur.left
            self.key = cur.key
            self.right = self.right.deletion(self.key)
        return self
    def min_key(self):
        cur = self
        while cur.left:
            cur = cur.left
        return cur.key
    def max_key(self):
        cur = self
        while cur.right:
            cur = cur.right
        return cur.key
    def sorted_array(self, arr):
        if self.left:
            arr = self.left.sorted_array(arr)
        arr.append(self.key)
        if self.right:
            arr = self.right.sorted_array(arr)
        return arr


def to_balanced(arr, m, l):
    root = Node(arr[int((l+m)/2)])
    if l > m:
        root.right = to_balanced(arr, int((l+m+2)/2), l)
    if l > m+1:
        root.left = to_balanced(arr, m, int((l+m-2)/2))
    return root


root = Node(20)
listKeys = [18, 15, 2, 5, 14, 17, 25, 12, 9, 22, 23, 26, 21]
for key in listKeys:
    root.insert(key)

root.deletion(26)

root.preorder()
print('')
print(root.min_key())
print(root.max_key())

root.search(18)

arr = root.sorted_array([])
print(arr)

root = to_balanced(arr, 0, len(arr)-1)
root.preorder()