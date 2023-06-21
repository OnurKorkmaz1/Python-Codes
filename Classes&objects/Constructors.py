#  <<<<<  Python Constructors  >>>>>


class Door:
    name = ""

door_Int = Door()

# However, we can also initialize values using the constructors. 
# For example,

class Window:
    # constructor function __init__
    def __init__(self, name =""):
        self.name = name

window_h = Window()

class Car:
    def __init__(self,make , model, year , color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("this car is driving")

    def stop(self):
        print("this car is stopped")