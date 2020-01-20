'''
class
instance attributes
class attributes
self
__init__

'''

#create custom class in python

class Vehicle:
    vehicleCount = 0
    #constructor
    def __init__(self, color, vtype):
        print("I am in constructor!")
        self.color = color
        self.vtype = vtype
        Vehicle.vehicleCount += 1

    def selectVehicle(self):
        print("{0:-^30}".format("Vehicle Info"))
        print("Vehicle Color: ", self.color)
        print("Vehicle Type: ", self.vtype)

myVehicle1 = Vehicle('Red', 'SUV')
myVehicle2 = Vehicle('Black', 'Sedan')
myVehicle3 = Vehicle('Purple', 'MUV')

print("Count of vehicle instances: ", Vehicle.vehicleCount)

myVehicle1.selectVehicle()
myVehicle2.selectVehicle()
myVehicle3.selectVehicle()