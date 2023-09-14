#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle): #__init__ gets called when the object is created
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car") #super is the parent
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("driving my", self.enginetype, "car at ", self.speed)

class Motorcycle(Vehicle):
    def __init__(self,enginetype, hassidecar):
        super().__init__("Motorcycle")
        self.doors = 0
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels =2
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("driving my", self.enginetype, "motorcycle at", self.speed)

mini = Car("gas")
escape = Car("hybrid")
leaf = Car("electric")
r100rs = Motorcycle("gas", False)

leaf.drive(35)
escape.drive(30)
r100rs.drive(40)