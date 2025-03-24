message = input("Input your message: ")
shiftNum = int(input("Input amount to shift by: "))

for i in range(len(message)):
    if message[i].isalpha():
        tempval = ord(message[i]) + shiftNum

        if message[i].isupper():
            if tempval > 90:
                val = tempval - 90
                tempval = 64 + val
            elif tempval < 65:
                val = tempval
        if message[i].islower():
            if tempval > 122:
                val = tempval - 122
                tempval = 96 + val
            elif tempval < 
        
        