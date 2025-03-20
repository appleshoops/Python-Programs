import math

def SevenTimes():
    for i in range(1, 11):
        print(f'7 x {i} = {7 * i}')

def Exponentials():
    for i in range(1, 21):
        print(f'Number is {i}, square is {math.pow(i, 2)}, cube is {math.pow(i, 3)}')

def TimeConvert():
    _time = 0
    _unit = 'AM'
    while _time != 9999:
        _time = int(input("Input the time in 24-hour format: "))
        if _time >= 0 and _time <= 2459:
            _hour = math.floor(_time / 100)
            _min = _time % 100
            
            if _min >= 60:
                print("Invalid input")
            else:
                if _hour > 12:
                    _hour -= 12
                    _unit = 'PM'
                print(f'Time is {_hour}:{_min} {_unit}')
    else:
        print("Invalid input")
    



# SevenTimes()
# Exponentials()
TimeConvert()

