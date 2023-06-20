# - - -  CLASSES - - -

class Bike:      # Bİke = the name of the class
    name = ""
    gear = 0     # attributes 


# - - - OBJECTS - - -
bike_o = Bike()    # create object of class

#bike_o is the object of the class. 
# Now, we can use this object to access the class attributes.

# - - - - - - - - - - - - - - -  - - - -  -- - - - -- - - -- - - -- - - -- - - - - -

#Access class attributes using object

bike_o.name = "Mountain Bike"

bike_o.gear = 11

print(f"Name: {bike_o.name},Gears: {bike_o.gear}")
