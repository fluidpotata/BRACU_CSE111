''''''
'''A company named Sheba.xyz has recently moved from their old domain to a new domain. However, a lot of the company 
email addresses are still using the old one. Write a function in python that replaces this old domain with the new one 
in any outdated email addresses. Keep same if the email address contains the new domain. (Do not use builtin replace 
function)
Firstly, define a “replace_domain” function which accepts three parameters
*The email address to be checked
*The new domain
* The old domain (Use Default argument technique to handle this)'''

def replace_domain(mail,new,old=""):
    temp = mail.split('@')
    if temp[1] == new:
        print('Unchanged:',mail)
    else:
        print('Changed:',temp[0]+'@'+new)

replace_domain('bob@sheba.xyz', 'sheba.xyz')

