lowrcase = False
upprcase = False
digit = False
spclchr = False

inp = input("Enter the new password: ")
spclchrctr = "_$#@"
for i in inp:
    if i in spclchrctr:
        spclchr = True
    elif ord('a')<=ord(i)<=ord('z'):
        lowrcase = True
    elif ord('A')<=ord(i)<=ord('Z'):
        upprcase = True
    elif ord('0')<=ord(i)<=ord('9'):
        digit = True

output = ""
if lowrcase == False:
    output += "Lowercase Missing,"
if upprcase == False:
    output += "Uppercase Missing,"
if digit == False:
    output += "Digit Missing,"
if spclchr == False:
    output += "Special character Missing,"
if spclchr == True and lowrcase == True and upprcase == True and digit == True:
    output = "OK,"

print(output[:-1])
