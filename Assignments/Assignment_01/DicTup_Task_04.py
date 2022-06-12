data={1:[".", ",", "?", "!", ":"], 2:["A", "B", "C"], 3:["D", "E", "F"], 4:["G", "H", "I"], 5:["J", "k", "L"],
      6:["M", "N", "O"], 7:["P", "Q", "R", "S"], 8:["T", "U", "V"], 9:["W", "X", "Y", "Z"], 0:[" "]}
user=input('Enter: ')
user=user.upper()
for i in user:
    for keys, values in data.items():
        for j in range(len(values)):
            if i==values[j]:
                m=0
                while m<=j:
                    print(keys, end="")
                    m+=1
