class Vehicle:
    def drive(self):
        print("The vehicle is being driven.")

class Bike(Vehicle):
    def drive(self):
        print("The bike is being ridden.")

class Truck(Vehicle):
    def drive(self):
        print("The truck is being driven.")

# Create instances of Bike and Truck
bike = Bike()
truck = Truck()

# Call the drive method for each instance
bike.drive()
truck.drive()