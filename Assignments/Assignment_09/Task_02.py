class myList:
    def __init__(self,*lst):
        self.lst = list(lst)

    def sum(self):
        print('Sum:',sum(self.lst))

    def merge(self,*nums):
        # for num in nums:
        #     self.lst.append(num)
        self.lst.extend(list(nums))

    def average(self):
        if len(self.lst)==0:
            out = 0
        else:
            out = (sum(self.lst)/len(self.lst))
        print('Average:',out)

#====================================================
l1 = myList(2,3,4,5,6) #you might need a list inside your class to store the values
l1.sum()
l1.merge(4,5,9)
l1.sum()
l1.average()
print('-----------------------------')
l2 = myList()
l2.average()
l2.merge(1,2,4,8)
l2.sum()