inp1 = input('Enter the first dictionary: ')
inp2 = input('Enter the second dictionary: ')
dict1 = {}
for i in inp1.split(", "):
    k = i.split(': ')
    if k[0] in dict1.keys():
        dict1[k[0]] += int(k[1])
    else:
        dict1[k[0]] = int(k[1])

for i in inp2.split(", "):
    k = i.split(': ')
    if k[0] in dict1.keys():
        dict1[k[0]] += int(k[1])
    else:
        dict1[k[0]] = int(k[1])
output = []
for i in dict1.values():
    if i not in output:
        output.append(i)
output = sorted(output)
output = tuple(output)

print(dict1)
print("Values: ", output)
