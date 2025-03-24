import random

def Swap(_list, _index1, _index2):
    _temp = _list[_index1]
    _list[_index1] = _list[_index2]
    _list[_index2] = _temp
    return _list

def bubbleSort(_list):
    for i in range(len(_list) - 1):
        swapped = False
        for n in range(len(_list) - (1 + i)):
            if _list[n] > _list[n + 1]:
                _list = Swap(_list, n, n + 1)
                swapped = True
        if swapped == False:
            print(_list)
    return _list

def RandomList(_min, _max, _num):
    _list = []
    for i in range(_num):
        x = random.randint(_min, _max)
        _list.append(x)
    return _list

values = RandomList(1, 100, 10)
print(values)
bubbleSort(values)