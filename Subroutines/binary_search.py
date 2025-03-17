def BinarySearch(_list, _searchItem):
    if len(_list) > 1:
        _leftList = _list[:len(_list)//2]
        _rightList = _list[len(_list)//2:]

        if _searchItem >= _rightList[0]:
            BinarySearch(_rightList, _searchItem)
        else:
            BinarySearch(_leftList, _searchItem)

    else:
        if _list[0] == _searchItem:
            return "found"
        else:
            return "not found"
        
def binarySearch2(_list, _searchItem):
    low = 0
    high = (len(_list) - 1)

    while low < high:
        mid = (low + high) // 2
        if _searchItem == _list[mid]:
            return "found"
        elif _searchItem < _list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "not found"

def mergeSort(arr): # Taken from merge sort activity
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        mergeSort(left_arr)
        mergeSort(right_arr)

        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr
        
values = [12, 28, 12, 63, 6, 90, 82, 42, 59, 10]
values = mergeSort(values)
print(values)
print(binarySearch2(values, 2))