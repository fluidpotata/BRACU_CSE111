many = int(input("How many lists you want to input? "))
sum = 0
inp = input("Enter your list: ").split(" ")
for i in inp:
    sum += int(i)

max = sum
max_l = inp
sum = 0
for i in range(many-1):
    inp = input("Enter your list: ").split(" ")
    for i in inp:
        sum += int(i)
    if sum>max:
        max = sum
        max_l = inp
    sum = 0
print(max)
print(max_l)
