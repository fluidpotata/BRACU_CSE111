class Bird:
    def __init__(self,name,fly=False):
        self.name = name
        self.fly_stat = fly
        self.type = 'Flightless Birds'

    def fly(self):
        if self.fly_stat==True:
            print(self.name,'can fly')
        else:
            print(self.name,'can not fly')

    def setType(self,type):
        self.type = type

    def printDetail(self):
        print('Name:', self.name)
        print('Type', self.type)



#===========================================
ostrich = Bird('Ostrich')
duck = Bird("Duck", True)
owl = Bird('Owl', True)
print('###########################')
ostrich.fly()
duck.fly()
owl.fly()
duck.setType('Water Birds')
owl.setType('Birds of Prey')
print('=========================')
ostrich.printDetail()
print('=========================')
duck.printDetail()
print('=========================')
owl.printDetail()