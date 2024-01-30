a = [1,-5,6,2,-10,1,2,-5,1,3]
# find the sum of the contiguous subarray within a a[] with the largest sum
result = 0
max = 0
for x in a:
    max += x
    if max > result:
        result = max
    if max < 0:
        max = 0
print(result)

