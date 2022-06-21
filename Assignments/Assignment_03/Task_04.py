class Vehicle:
    def __init__(self,x=0,y=0):
        self.x = int(x)
        self.y = int(y)

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def print_position(self):
        output = tuple((self.x,self.y))
        print (output)


car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()
