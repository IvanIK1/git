def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivat = arr[0]
    left_part = [x for x in arr if x < pivat ]
    midl = [x for x in arr if x == pivat]
    right_part = [x for x in arr if x > pivat]
    return quick_sort(left_part) +midl + quick_sort(right_part)

a = [3 , 1 , 4 , 2 ,5 , -3 ]




def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
            
def merge(left , right):
    sorted_arr = []
    i = h = 0
    while i < len(left) and h < len(right):
        if left[i] < right[h]:
            sorted_arr.append(left[i])
            i += 1 
        else:
            sorted_arr.append(right[h])
            h += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[h:])
    return sorted_arr  

