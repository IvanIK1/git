def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivat = arr[0]
    left_part = [x for x in arr if x < pivat ]
    midl = [x for x in arr if x == pivat]
    right_part = [x for x in arr if x > pivat]
    return quick_sort(left_part) +midl + quick_sort(right_part)

a = [3 , 1 , 4 , 2 ,5 ]

# print(quick_sort(a))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
            
def merge(left , right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1 
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr  

if __name__ == "__main__":
