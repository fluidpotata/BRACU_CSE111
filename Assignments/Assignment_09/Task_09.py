# Do not change the following lines of code.
class Fruit:
    Total_order=0
    def __init__(self, Order_ID, weight):
        self.Order_ID=Order_ID
        self.weight=weight
        Fruit.Total_order=Fruit.Total_order+1
    def __str__(self):
        return self.Order_ID+", Weight: "+str(self.weight)
class Mango(Fruit):
    #write your code here
    def __init__(self,Order_ID, weight,variety,price):
        super().__init__(Order_ID,weight)
        self.variety = variety
        self.price = price*weight

    def __str__(self):
        return super().__str__()+f", Variety: {self.variety}, Total Price: {self.price}"

    def __add__(self, other):
        return f"The total Price of the orders are: {self.price+other.price}"

class JackFruit(Fruit):
    #write your code here
    def __init__(self, Order_ID, weight, price):
        super().__init__(Order_ID, weight)
        self.price = price * weight

    def __str__(self):
        return super().__str__() + f", Total Price: {self.price}"

    def __add__(self, other):
        return f"The total Price of the orders are: {self.price + other.price}"




m1=Mango("Order Id 1", 5,"GopalVog",250)
print(m1)
m2=Mango("Order Id 2", 5,"HariVanga", 230)
print(m2)
j1=JackFruit("Order Id 3", 5,250)
print(j1)
j2=JackFruit("Order Id 4", 4,210)
print(j2)
print("Total number of Orders: "+str(Fruit.Total_order))
print("==================")
print(m1+m2)
print("==================")
print(j1+j2)