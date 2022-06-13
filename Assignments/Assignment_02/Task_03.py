class Joker():
    def __init__(self,name,power,psychostat):
        self.name = name
        self.power = power
        self.is_he_psycho = psychostat


j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')


subtask_2 = "The first if/else block prints Different because J1 and J2 are two different objects and they have different values. "
subtask_3 = "The second if/else block prints Same because just before the block j2.name was updated and it is the same as J1.name,"
print(subtask_2)
print(subtask_3)
