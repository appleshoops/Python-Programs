import sys
import os

filename = "Python Programs/Programming Fundamentals/External Data/Data/names_scores.txt"

def receiveData(_filename):
    _gradesList = []
    with open(_filename, "r") as file:
        for line in file:
            _person = line.strip().split(',')
            _person[1] = int(_person[1])
            _personDict = {
                "Name": _person[0],
                "Score": _person[1]
            }
            if _person[1] < 50:
                _personDict["Grade"] = "F"
            elif 50 <= _person[1] <= 59:
                _personDict["Grade"] = "E"
            elif 60 <= _person[1] <= 69:
                _personDict["Grade"] = "D"
            elif 70 <= _person[1] <= 79:
                _personDict["Grade"] = "C"
            elif 80 <= _person[1] <= 89:
                _personDict["Grade"] = "B"
            else:
                _personDict["Grade"] = "A"

            _gradesList.append(_personDict)
        file.close()
        return _gradesList
    
gradesList = receiveData(filename)
print(gradesList)

