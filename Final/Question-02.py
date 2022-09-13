class Social:
    activity = ['Like', 'Comment', 'Share']

    def __init__(self,name,email):
        self.name = name
        self.email = email

    def details(self):
        return "Name: "+self.name+"\nEmail: "+self.email


class BracBook(Social):
    def __init__(self,n,m,p="Not Set"):
        super().__init__(n, m)
        self.phone = p
        self.activitylist = []

    def doactivity(self, x):
        if x in super().activity:
            self.activitylist.append(x)
            print(f"{self.name} has {x}(d/ed) a post.")

        else:
            print(f"{x} activity not found.")

    def details(self):
        x = super().details()+f"\nPhone: {self.phone}\nActivites: "
        if len(self.activitylist)==0:
            x += 'No activites found'
        else:
            x += ', '.join(self.activitylist)
        return x


print('========================')
navid = BracBook('Navid','navid@xyz.com')
navid.doactivity('Like')
david = BracBook('David','david@abc.com','017xxxxxxxx')
print('========================')
print(navid.details())
print(david.details())
david.doactivity('Create')
david.doactivity('Comment')
navid.doactivity('Share')
print('========================')
print(navid.details())
print(david.details())
