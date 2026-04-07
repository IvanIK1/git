# Найти наибольший элемент 

def max_val(arr):
    if len(arr) <= 0 :
        return IndexError
    i = 0
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            i += 1 
        else:
            i += 1 
    return max 


arr1 = [ 11 , 1 , 0 , 2, 3, 100,5, 1 , - 1, 0, 0, 1021]\

arr2 = [0 , 0, 0 ]

arr3 = [ ]

print(max_val(arr2))