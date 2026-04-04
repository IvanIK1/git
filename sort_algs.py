def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivat = arr[0]
    left_part = [x for x in arr if x < pivat ]
    midl = [x for x in arr if x == pivat]
    right_part = [x for x in arr if x > pivat]
    print(arr)
    return quick_sort(left_part) +midl + quick_sort(right_part)

a = [2 , 3 ,5 ,5,1 , 8 ,2,3,10,17,3]

print(quick_sort(a))