str1 = 'dean'
str2 = 'tom'
new = ""
for i in str1:
    if i in str2:
        new += i
for i in str2:
    if i in str1:
        new += i

if new == "":
    print("Nothing in common")
else:
    print(new)
