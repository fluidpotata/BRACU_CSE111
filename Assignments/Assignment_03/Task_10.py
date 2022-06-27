# Write your code here
class UberEats:
    def __init__(self,name,num,add):
        self.name = name
        self.number = num
        self.address = add
        print(f"{name}, welcome to UberEats!")
        self.items = {}

    def add_items(self,itm1,itm2,prc1,prc2):
        self.items[itm1] = prc1
        self.items[itm2] = prc2
        self.paid = prc1+prc2

    def print_order_detail(self):
        output =f"User Details: Name: {self.name}, Phone: {self.number}, Address: {self.address} \nOrders: {self.items} \nTotal Paid amount: {self.paid}"
        return output
#====================================================

order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())
