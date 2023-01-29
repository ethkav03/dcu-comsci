def bubbleSort(arr_input):
    for i in range(len(arr_input)):
        for j in range(len(arr_input) - 1, i, -1):
            if arr_input[j] < arr_input[j - 1]:
                tmp = arr_input[j]
                arr_input[j] = arr_input[j - 1]
                arr_input[j - 1] = tmp
    return arr


arr = [3, 4, 2, 6, 5, 7, 1, 9]
print('Before sorting:', arr)
print('After sorting:', bubbleSort(arr))