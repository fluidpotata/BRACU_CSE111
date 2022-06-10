'''
5. Again, you have lost your USIS password!! You went to the registrar office
and requested for a new password. This time, you need to follow some rules to
set your password. Otherwise, they won't change it. The rules are
    At least one lowercase letter
    At least one uppercase letter
    At least one digit (0-9)
    At least one special character (_ , $ , #, @)
    
Your task is to find whether a given password follows all those rules. If it breaks
any rule, you have to print Lowercase Missing, Uppercase Missing, Digit Missing
or Special Missing respective to the missing case. For more than one rule break,
print all the rules that were broken (order doesn't matter). If the password is ok,
print OK.
===================================================================================
Sample Input              Sample Output
ohMyBR@CU                 Digit missing
ohmybracu          Uppercase character missing, Digit missing, Special character missing
OhMyBR@CU20                    OK
'''

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
