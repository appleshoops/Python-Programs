num = int(input("How many numbers will you be entering? "))
while num <= 0:
    print("Invalid input, enter a number greater than 0")
    num = int(input("How many numbers will you be entering? "))
sum = 0

for i in range(num):
    num2 = int(input("Enter a number: "))
    sum += num2
avg = sum / num
print(f'The sum is {sum} and the average is {avg:.2f}')