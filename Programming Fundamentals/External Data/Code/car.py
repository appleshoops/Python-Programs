filename = 'Python Programs/Programming Fundamentals/External Data/Data/car.txt'

with open(filename, "r") as file:  # use r for read mode, w for write mode, a for append mode!!! 😺 
    file_content = file.read()
    file.close()

carList = []
with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        carInfo = line.split(',')
        carList.append(carInfo)
    file.close()
# print(carList[0][0])

carDict = []
with open(filename, "r") as file:
    for line in file:
        line = line.strip().split(',')
        carDict.append({
            "Make": carInfo[0],
            "Model": carInfo[1],
            "Year": int(carInfo[2]),
            "Colour": carInfo[3],
            "Price": int(carInfo[4])
        })