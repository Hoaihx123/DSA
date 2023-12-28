# list
list1 = list()
list1.append(1)
list1.append(2)
print(list1)
list2 = [1, 2, ]
print(list1 == list2)
list1.append('sdsfs')
print(list1)
print(list1[-2])
del list1[1]
print(list1)

# tuple
tuple1 = (1, 2, 3, 4)
print(tuple1)
tuple2 = 4, 3, 2, 1
print(tuple2 == tuple1)
print(type(tuple2))
tuple3 = (4)
print(type(tuple3))
# can't append element to tuple
print(tuple1[2])

# dictionary
d1 = dict()
d2 = {}
d2 = {'1': 1, '2': 2, '1': 3}
d1 = {'2': 2, '1': 3}
print(d2)
print(d2 == d1)
print(d2['1'])
del d2['1']
print(d2)

# set
s1 = set("hello")
print(s1)
s2 = {1, 2, 3, 4}
print(s2)
s1 = set([4, 1, 1, 3, 3, 2, 2, 1])
print(s1)
print(s1 == s2)
s1.add(5)
print(5 in s1)
