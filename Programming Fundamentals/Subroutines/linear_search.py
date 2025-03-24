def LinearSearch(_list, _searchItem):
    for i in range(len(_list)):
        if _list[i] == _searchItem:
            return "item found"
    return "value not found"

print(LinearSearch([1, 2, 3, 4, 5], 7))
