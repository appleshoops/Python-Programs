for i in range(1, 21):
    match i:
        case i if i % 3 == 0 and i % 5 == 0:
            print(f'{i} FizzBuzz')
        case i if i % 3 == 0:
            print(f'{i} Fizz')
        case i if i % 5 == 0:
            print(f'{i} Buzz')
        case _:
            print(i)