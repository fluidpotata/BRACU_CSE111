inp = input('Enter your dictionary: ')
inp_dict = {}
temp = []
for i in inp.split(", "):
    temp = i.split(" : ")
    inp_dict[temp[0]] = temp[1]

new = {}

for keys,values in inp_dict.items():
    if values in new.keys():
        new[values].append(keys)
    else:
        new[values] = [keys]

print(new)
