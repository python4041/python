class student:
    def __init__(self,name,lname,age):
        self.name=name
        self.last_name=lname
        self.age=age
    def mail(self):
        self.gmail=self.name+self.last_name+"@gmail.com"
        return self.gmail

    def Cinama(self):
        self.cinema=self.age
        if self.age>15:
            print('ok')
        else:
            print("no")
        
        return self.cinema

parsa=student('parsa','sarkhosh',19)
parsa.Cinama()