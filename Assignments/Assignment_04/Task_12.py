# Write your code here
class TaxiLagbe:
    def __init__(self,a,b):
        self.taxinum = a
        self.taxiarea = b
        self.passengers = []
        self.fare = 0

    def addPassenger(self,*n):
        if len(self.passengers)>=4:
            print('Taxi Full! No more passengers can be added.')
        else:
            for i in n:
                x = i.split('_')
                print(f'Dear {x[0]}! Welcome to TaxiLagbe.')
                self.passengers.append(x[0])
                self.fare += int(x[1])


    def printDetails(self):
        count = len(self.passengers)
        print(f"Trip info for Taxi number: {self.taxinum} \nThis taxi can cover only {self.taxiarea} area.")
        print(f"Total passengers: {count}")
        print('Passenger lists:')
        for i in range(count):
            if i==count-1:
                print(self.passengers[i])
            else:
                print(self.passengers[i],end=", ")
        print(f"Total collected fare: {self.fare} Taka")




# Do not change the following lines of code.

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()
