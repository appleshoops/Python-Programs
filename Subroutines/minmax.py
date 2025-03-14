import random

def MaximumValue(_list):
    if len(_list) != 0:
        _max = _list[0]
        if len(_list) > 1:
            for i in range(1, len(_list)):
                if _list[i] > _max:
                    _max = _list[i]
            return _max
    else:
        print("List is empty")

def RandomList(_min, _max, _num):
    _list = []
    for i in range(_num):
        x = random.randint(_min, _max)
        _list.append(x)
    return _list

values = RandomList(1, 1000, 20)

print(values)
print(MaximumValue(values))