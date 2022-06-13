inp=str(input('Enter n and k: ')).split(" ")
student = int(inp[0])
time = int(inp[1])
count =0
lst = str(input('Enter: ')).split(" ")
for i in range(len(lst)):
  lst[i]=int(lst[i])+time
for j in range(len(lst)):
  if lst[j]<=5:
    count+=1
print(count//3)
