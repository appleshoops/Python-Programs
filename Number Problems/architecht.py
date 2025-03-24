cost = float(input("Enter total cost of building: "))
fee = 0

if cost <= 5000:
    fee = cost * 0.08
else:
    fee += 5000 * 0.08 
    remaining_cost = cost - 5000 

    if remaining_cost <= 80000:
        fee += remaining_cost * 0.03 
    else:
        fee += 80000 * 0.03 
        fee += (remaining_cost - 80000) * 0.025 

print(f'The architect fee for this building will be ${fee:.2f}')
