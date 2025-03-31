import random

rolls = 0

diceroll = random.randint(1, 6)
rolls += 1
print(diceroll)

while diceroll != 6:
    diceroll = random.randint(1, 6)
    rolls += 1
    print(diceroll)

print(f'It took {rolls} dice rolls to get 6')