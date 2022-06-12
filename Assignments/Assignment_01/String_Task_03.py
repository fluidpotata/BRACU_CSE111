given = "coDIng"
new = ""
stat = False
for i in given:
    if stat == True:
        new+= i
    if ord('A')<=ord(i)<=ord('Z'):
        if stat == False:
            stat = True
        elif stat == True:
            stat == False
            new = new[:-1]
            break

if new == "":
    print('BLANK')
else:
    print(new)
