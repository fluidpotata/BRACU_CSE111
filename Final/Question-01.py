class Monster:
    def __init__(self,n,p):
        self.name = n
        self.hp = p
        self.alive = True

    def monsterAttack(self,*others):
        if len(others)!=0:
            for other in others:
                if self.alive == True:
                    if other.alive == True:
                        if self.hp>other.hp:
                            print(f"Attack successful. {self.name} defeated {other.name}.")
                            other.alive = False
                        else:
                            print(f"Attack unsuccessful. {self.name} was defeated by {other.name}.")
                            self.alive = False
                    else:
                        print(f"Can't attack. {other.name} is not alive.")
                else:
                    print(f"{self.name} is not alive to attack.")
        else:
            print("No one to attack.")

    def monsterDetails(self):
        print("Name:", self.name)
        print("Hitpoint:", self.hp)
        return f"Alive: {self.alive}"


# You are not allowed to change anything below:

godzilla = Monster("Godzilla",80)
kingkong = Monster("King Kong",60)
doge = Monster("Doge",100)
print("=========================================")
print(godzilla.monsterDetails())
print(kingkong.monsterDetails())
print(doge.monsterDetails())
print("=========================================")
godzilla.monsterAttack()
godzilla.monsterAttack(kingkong)
print(kingkong.monsterDetails())
print("=========================================")
kingkong.monsterAttack(doge)
godzilla.monsterAttack(doge)
doge.monsterAttack(kingkong)

