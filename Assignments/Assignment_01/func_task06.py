def capitalizer(given):
    new_str = ''
    for i in range(len(given)):
        if i==0:
            new_str+=given[i].upper()
        elif given[i - 2]== '.' or given[i - 2]== '!' or given[i - 2]== '?':
            new_str+=given[i].upper()
        elif given[i]== 'i' and given[i - 1]== ' ' and given[i + 1]== ' ':
            new_str+=given[i].upper()
        else:
            new_str+=given[i]
    print(new_str)

capitalizer('my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my '
            'pet '
            'dog’s name? i love my pet very much.')
