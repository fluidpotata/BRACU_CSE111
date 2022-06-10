'''
1.From a given string, print the string in all uppercase if the number ofuppercase
letters is more than lowercase letters. Otherwise, if lowercase is greater or equal
to uppercase letters, print all lowercase. The inputs will contain letters (A-Z, a-z)
only.
======================================================================================
Sample Input        Sample Output
   HOusE                 HOUSE
   ApplE                 apple
   BaNaNa               banana
'''
word = "ApplE"
uppr = 0
lowr = 0
for i in word:
    if ord('A')<=ord(i)<=ord('Z'):
        uppr += 1

    elif ord('a')<=ord(i)<=ord('z'):
        lowr += 1

if uppr>lowr:
    print(word.upper())
else:
    print(word.lower())
