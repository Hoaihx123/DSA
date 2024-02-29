class BNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.key = []
        self.child = []
class BTree:
    def __init__(self, t):
        self.root = BNode(True)
        self.t = t
    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BNode(y.leaf)
        x.key.insert(i, y.key[t-1])
        x.child.insert(i+1, z)
        z.key = y.key[t:2*t-1]
        y.key = y.key[0:t-1]
        if y.leaf is False:
            z.child = y.child[t:2*t]
            y.child = y.child[0:t]
    def insert_non_full(self, x, k):
        i = len(x.key)-1
        if x.leaf:
            x.key.append(None)
            while i >= 0 and x.key[i][0] > k[0]:
                x.key[i+1] = x.key[i]
                i -= 1
            x.key[i+1] = k
        else:
            while i >= 0 and x.key[i][0] > k[0]:
                i -= 1
            i += 1
            if len(x.child[i].key) == 2*self.t -1:
                self.split_child(x, i)
                if k[0] > x.key[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)
    def insert(self, k):
        root = self.root
        if len(root.key) == 2*self.t - 1:
            temp = BNode()
            self.root = temp
            temp.child.append(root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)
    def print_tree(self, x, l=0):
        print('level ', l, ':')
        for i in x.key:
            print(i, end=' ')
        print()
        l +=1
        if not x.leaf:
            for i in x.child:
                self.print_tree(i, l)
    def find(self, k):
        x = self.root
        while 1:
            i = len(x.key)-1
            while i >= 0 and x.key[i][0] > k:
                i -= 1
            if x.key[i][0] == k:
                return x.key[i][1]
            elif x.leaf:
                return None
            else:
                x = x.child[i+1]



btree = BTree(2)
btree.insert([5, 'Hoai'])
btree.insert([4, 'ok'])
btree.insert([6, 'Duy'])
btree.insert([7, 'ok'])
btree.insert([3, 'Dep Trai'])
btree.insert([2, 'ok'])
btree.insert([1, 'My Nhu'])
btree.insert([8, 'Le Quang'])
btree.insert([9, 'ok'])
btree.insert([10, 'ok'])
btree.insert([11, 'ok'])

btree.print_tree(btree.root)
