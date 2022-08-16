class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+        " Price: "+str(self.__price)
#write your code here

class Book(Product):
    def __init__(self,id,tit,pr,isbn,pub):
        super().__init__(id,tit,pr)
        self.__isbn = isbn
        self.__publisher = pub

    def printDetail(self):
        temp = super().get_id_title_price() + f" ISBN: {self.__isbn} Publisher: {self.__publisher}"
        return temp

class CD(Product):
    def __init__(self,id,tit,pr,band,dur,gen):
        super().__init__(id,tit,pr)
        self.__duration = dur
        self.__genre = gen
        self.__band = band


    def printDetail(self):
        tmp = super().get_id_title_price() +f" Band: {self.__band} Duration: {self.__duration} minutes Genre: {self.__genre}"
        return tmp





book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())
