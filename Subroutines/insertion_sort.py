import random

def InsertionSort(_list):
    for i in range(len(_list) - 1):
        _min = i
        for n in range(i, len(_list)):
            if _list[n] < _list[_min]:
                _min = n
        _temp = _list[i]
        _list[i] = _list[_min]
        _list[_min] = _temp
        print(_list)
        return False


def RandomList(_min, _max, _num):
    _list = []
    for i in range(_num):
        x = random.randint(_min, _max)
        _list.append(x)
    return _list

print(InsertionSort(RandomList(1, 100, 6)))
list = [10, 1, 69, 3, 42, 84]
#print(InsertionSort(list))