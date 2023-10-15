import unittest, Car, FleetOfCars

def FleetOfTests():
    red_car = Car.Car("Sudan","1996","yellow","4","6")
    #print(red_car)
    blue_car = Car.Car()
    #print(blue_car)
    cars = FleetOfCars.FleetOfCars([red_car,blue_car,red_car])
    # print(cars)
    # cars.removeCar(blue_car)
    # print(cars)
    cars.addCar(Car.Car("Toyota",1930,"polka dot",5,90))
    # print(cars.totalMaxPassengers())
    # print(cars)
    # print(cars.totalMakeModel("Sudan"))
    print(cars.totalCars())
FleetOfTests()