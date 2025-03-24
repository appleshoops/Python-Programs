weight = float(input("Enter the weight of the parcel in kg: "))

match weight:
    case weight if weight < 2.5 and weight > 0:
        print(f'Delivery will cost ${(3.5 * weight):.2f}')
    case weight if weight >= 2.5 and weight <= 5:
        print(f'Delivery will cost ${(2.85 * weight):.2f}')
    case weight if weight > 5:
        print(f'Delivery will cost ${(2.45 * weight):.2f}')
    case _:
        print("Invalid Weight")
