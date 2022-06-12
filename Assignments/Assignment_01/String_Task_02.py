given = "jhg231j213"

number = False
word = False

for i in given:
    if ord('0')<=ord(i)<=ord('9'):
        number = True
    elif ord('A')<=ord(i)<=ord('Z') or ord('a')<=ord(i)<=ord('z'):
        word = True

if number == True and word == True:
    print('MIXED')
elif number == True:
    print("NUMBER")
elif word == True:
    print("WORD")
