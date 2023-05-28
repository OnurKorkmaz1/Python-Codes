
class Matematik:
    def topla(self, sayi1,sayi2):
        return sayi1 +sayi2

    def carp(self, sayi1,sayi2):
        return sayi1 * sayi2

    def bol(self, sayi1,sayi2):
        return sayi1 / sayi2

matematik=Matematik()
print("toplam=" + str(matematik.topla(2,78)))



class person:
    def __init__(self,firstname,lastname,age):

        self.firstname=firstname
        self.lastname=lastname
        self.age=age
person1=person("onur","korkmaz","22")
print(person1.age)

class worker(person):
    def __init__(self,salary):
        self.salary=salary
class customer(person):
    def __init__(self,creditcardnumber):
        self.creditcardnumber=creditcardnumber       

ahmet=worker()
mehmet=customer()

ahmet.salary


