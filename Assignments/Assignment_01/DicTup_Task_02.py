dict1 = {}
while True:
    inp = input("Enter: ")
    if inp.lower() == "stop":
        break
    inp = int(inp)
    if inp in dict1.keys():
        dict1[inp] += 1
    else:
        dict1[inp] = 1
for key,value in dict1.items():
    print(f"{key} - {value} times")
