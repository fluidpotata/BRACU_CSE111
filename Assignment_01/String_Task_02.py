'''
2.Given a string, print whether it is a number, word or mixed with digit andletters.
If all the characters are numeric values, print NUMBER. If they are all letters,
print WORD. If it is mixed, print MIXED.

Sample Input    Sample Output
  213213            NUMBER
  jhg231j213        MIXED
  Hello             WORD
'''


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
