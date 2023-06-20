# - - - Python Inheritance - - -

class Animal:

    def eat(self):
        print("I can eat")
    
    def sleep(self):
        print("I can sleep")

class Dog(Animal):

    def bark(self):
        print("I can bark!! wooof wooof")



dog1 = Dog()   # create object of Dog class

dog1.eat()     # calling member of the base class
dog1.sleep()  

dog1.bark()    # calling member of the derived class


