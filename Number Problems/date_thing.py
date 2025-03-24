date = input("Enter a date in the format 'dd/mm/yyyy' ")
value = date.split("/")
values = list(map(int, value))

if values[1] >= 1 and values[1] <= 12:
    match values[1]:
        case 1, 3, 5, 7, 8, 10, 12:
            if values[0] <= 31 and values[0] > 0:
                print("Valid date")
            else:
                print("Invalid date")
        case 4, 6, 9, 11:
            if values[0] <= 30 and values[0] > 0:
                print("Valid date")
            else:
                print("Invalid date")
        case 2:
            if values[2] % 4 == 0:
                if values[0] <= 29 and values[0] > 0:
                    print("Valid date")
                else:
                    print("Invalid date")
            else:
                if values[0] <= 28 and values[0] > 0:
                    print("Valid date")
                else:
                    print("Invalid date")