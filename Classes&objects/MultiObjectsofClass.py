
# Defining a class
class Employee:
    ID = 0   # define a attribute
    Tax = 0
    num =0
    
    # methof to calculate power
    def calculate_pov(self):
        print("Taxes of Employee : ",self.Tax*self.num)

# Create two objects of the Employe Class
employee_1 = Employee()
employee_2= Employee()

# Acces atributes
employee_1.ID = 1001
print(f"Empolyee ID: {employee_1.ID}")

employee_2.ID = 1001
print(f"Empolyee ID: {employee_2.ID}")

employee_1.Tax = 16000
employee_1.num = 10

employee_1.calculate_pov()
