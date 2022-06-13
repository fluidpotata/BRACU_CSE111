def function(given) :
  out = ''
  for i in given :
    if 97<=ord(i)<= 122 :
      out += i
  out1 = out[-1::-1]
  if out1 == out :
    return "palindrome"
  else :
    return "not palindrome"
inp = input()
store = function(inp)
print(store)
