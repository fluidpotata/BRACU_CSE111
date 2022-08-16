# Write your code here
class Assassin:
    number = 0

    def __init__(self,name,sr):
        self.name = name
        self.successrate = sr
        Assassin.number += 1

    @classmethod
    def failureRate(cls,name,fr):
        temp = 100 - fr
        return cls(name,temp)

    @classmethod
    def failurePercentage(cls,name,fr):
        temp = 100 - int(fr[:-1])
        return cls(name,temp)

    def printDetails(self):
        print(f"Name: {self.name} \nSuccess rate: {self.successrate}% \nTotal number of Assassin: {self.number}")


john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()
