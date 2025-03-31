import sys
import os
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
subroutines_path = os.path.join(base_dir, "Subroutines")
sys.path.append(subroutines_path)
import linear_search # type: ignore

filename = "Python Programs/Programming Fundamentals/External Data/Data/names_list.txt"

def namesIntoDict(_filename):
    _nameList = []
    with open(_filename, "r") as file:
        for line in file:
            _person = line.strip().split()
            _nameList.append({
                "First Name": _person[0],
                "Surname": _person[1]
            })
    return _nameList

namesList = namesIntoDict(filename)