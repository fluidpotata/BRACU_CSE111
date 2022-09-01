class Transport:
    total_traveller = 0

    def __init__(self, name, fare):
        self.name = name
        self.baseFare = fare

    def __str__(self):
        s = "Name: " + self.name + ", Base fare: " + str(self.baseFare)
        return s

class Bus(Transport):
    def __init__(self,name,fare):
        super().__init__(name,fare)
        print(f"Bus fare of {self.name} is {self.baseFare} taka.")
        self.passengers = {}

    def addPassengerWithBags(self,*args):
        tmp = 0
        for i in range(0,len(args),2):
            if args[i + 1]<=2:
                tmp = self.baseFare
            elif args[i+1]<5:
                tmp = self.baseFare+60
            elif args[i+1]>5:
                tmp = self.baseFare + 105
            self.passengers[args[i]] = tmp
            Transport.total_traveller += 1

    def __str__(self):
        x = f"Name: {self.name}, Base fare: {self.baseFare}\nTotal Passenger(s): {len(self.passengers.keys())}\nPassenger details:\n"
        for k,v in self.passengers.items():
            x += f"Name: {k}, Fare: {v}\n"
        return x

class Train(Transport):
    def __init__(self,name,fare):
        super().__init__(name,fare)
        print(f"Bus fare of {self.name} is {self.baseFare} taka.")
        self.passengers = {}

    def addPassengerWithBags(self,*args):
        tmp = 0
        for i in range(0,len(args),2):
            if args[i + 1]<=2:
                tmp = self.baseFare
            elif args[i+1]<5:
                tmp = self.baseFare+60
            elif args[i+1]>5:
                tmp = self.baseFare + 105
            self.passengers[args[i]] = tmp
            Transport.total_traveller += 1

    def __str__(self):
        x = f"Name: {self.name}, Base fare: {self.baseFare}\nTotal Passenger(s): {len(self.passengers.keys())}\nPassenger details:\n"
        for k,v in self.passengers.items():
            x += f"Name: {k}, Fare: {v}\n"
        return x


# Write your codes here.
# Do not change the following lines of code.
t1 = Bus("Volvo", 950)
print("=================================")
t1.addPassengerWithBags("David", 6, "Mike", 1, "Carol", 3)
print("=================================")
print(t1)
print("=================================")
t2 = Train("Silk City", 850)
print("=================================")
t2.addPassengerWithBags("Bob", 2, "Simon", 4)
print("=================================")
print(t2)
print("=================================")
print("Total Passengers in Transport: ", Transport.total_traveller)
