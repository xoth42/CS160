import Car
class FleetOfCars:
    def __init__(self,cars=[]):
        self.cars = cars.copy()
    def getCarsCopy(self)->list:
        return self.cars.copy()
    def __repr__(self)->str:
        out = ""
        for car in self.cars:
            out += str(car) + "\n"
        return out
    def addCar(self, newCar:Car.Car):
        self.cars.append(newCar)
    def removeCar(self, carToRemove:Car.Car):
        self.cars.remove(carToRemove)
    def totalMaxPassengers(self)->int:
        sum = 0
        for car in self.cars:
            sum +=car.get_max_passengers()
        return sum
    def totalCars(self)->int:
        return len(self.cars)
    def totalMakeModel(self, makeModelToSearch:str)->int:
        sum = 0
        for car in self.cars:
            if car.get_make_model() == makeModelToSearch:
                sum += 1
        return sum
    
        
            
