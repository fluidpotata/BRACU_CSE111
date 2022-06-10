'''
3.In a given string, there will be two uppercase letters in between some lowercase
letters. Print the substring from the first uppercase letter to the last uppercase
letter excluding them. If there are no letters in between them, print the word
BLANK. It is guaranteed that there will be only two uppercase letters in the
string.

Sample Input      Sample Output
  baNgladEsh          glad
  coDIng              BLANK
  '''

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
    
