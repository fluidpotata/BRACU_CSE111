val = False
inp = input("Enter the list: ").split()
new = []

for i in range(len(inp)-1):
    x = int(inp[i]) - int(inp[i+1])
    if x<0:
        x = x*(-1)
    new.append(x)

for i in range(1,len(inp)):
    if i not in new:
        val = True

if val == False:
    print("UB Jumper")
else:
    print("Not UB Jumper")
