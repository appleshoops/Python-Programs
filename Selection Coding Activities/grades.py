x = int(input("Input a number between 0 and 100: "))

match x:
    case x if x >= 90:
        print("A")
    case x if x >= 80 & x <= 89:
        print("B")
    case x if x >= 70 & x <= 79:
        print("C")
    case x if x >= 60 & x <= 69:
        print("D")
    case x if x < 60:
        print("F")