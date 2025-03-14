def sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

def average(numbers):
    _avg = sum(numbers)/len(numbers)
    return _avg

print(average([1, 2, 3, 4, 5]))