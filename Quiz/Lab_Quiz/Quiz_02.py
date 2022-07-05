class PokemonTrainer:
    def __init__(self,name,*pokemons):
        self.name = name
        self.pokemons = list(pokemons)

    def catch(self,n):       
        self.pokemons.append(n)
        print("Caught Successfully")

    def info(self):
        print(f"Trainer name: {self.name} \nPokemons caught:",end=" ")
        for i in self.pokemons:
            print(i,end=" || ")
        print()

        
#Driver Code


c1 = PokemonTrainer('Ash Ketchum',"Pikachu","Bulbasaur")
print('--------------------------')
c1.info()
print('--------------------------')
c2 = PokemonTrainer("Brock","Onix","Zubat","Mudkip")
c2.info()
print('--------------------------')
c1.catch("Snortax")
c1.info()
  
  
  
