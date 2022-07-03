# Write your code here.
class ParcelKoro:
    def __init__(self,name='No name set',weight=0):
        self.name = name
        self.product_weight = weight

    def calculateFee(self,location=None):
        if location==None:
            del_fee = 50
        else:
            del_fee = 100

        if self.product_weight==0:
            self.fee=0
        else:
            self.fee = (self.product_weight * 20) + del_fee

    def printDetails(self):
        print(f"Customer Name: {self.name} \nProduct Weight: {self.product_weight} \nTotal fee: {self.fee}")







#===============================
print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()
