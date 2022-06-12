list1 = []
list2 = []

inp = ""
while inp != "STOP":
    inp = input("Enter: ")
    list1.append(inp)
list1 = list1[:-1]
for i in range(len(list1)):
    list2.append(0)

count = 0
for i in list1:
    if i not in list2:
        list2.append(i)
        for j in list1:
            if i == j:
                count += 1

        print(f"{i} - {count} times")
        count = 0
