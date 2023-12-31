def quick_sort(a):
    if len(a) > 1:
        hight = [u for u in a if u > a[0]]
        low = [u for u in a if u < a[0]]
        eq = [u for u in a if u == a[0]]
        a = quick_sort(low) + quick_sort(eq) + quick_sort(hight)
    return a
a = [5, -8, 0, 9, 10, -3, 6, 2]
print(quick_sort(a))