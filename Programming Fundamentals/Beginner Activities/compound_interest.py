interest = 1.04
savings = float(input("Enter amount of money in your savings account "))

for i in range(1,4):
    savings = savings * interest
    print(f"New savings balance for year {i} is ${savings:.2f}")