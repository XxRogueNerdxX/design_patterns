from abs import ABC 
from enum import Enum


"""
Create a base interface Vehicle with a method rent().
Implement two classes Car and Bike that implement the Vehicle 
interface and provide specific implementations for the rent() method.
Create factory classes CarFactory and BikeFactory that produce 
instances of Car and Bike, respectively.
Implement a VehicleRentalSystem class that uses these factory 
classes to create instances of Car and Bike.
Demonstrate how to add a new vehicle type, Scooter, using the 
factory pattern without modifying the existing VehicleRentalSystem code.
"""

class Vehicle(ABC):
    def rent(self, amount):
        pass

class VehicleFactory(ABC):
    def rent_vehicle(self, amount):
        pass

class Car(Vehicle):
    def rent(self, amount):
        print(f"The cars rent would be {amount}")

class Bike(Vehicle):
    def rent(self, amount):
        print(f"The bike amount would be {amount}")

class CarFactory(VehicleFactory):
    def rent_vehicle(self, amount):
        print("The vehicle you are renting is a car")
        return Car() 

class BikeFactory(VehicleFactory):
    def rent_vehicle(self, amount):
        return super().rent_vehicle(amount)



