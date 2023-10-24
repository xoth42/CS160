import Car

class GasolineCar (Car.Car):
    def __init__(self, makeAndModel="none assigned", numberOfDoors=4, maximumNumberOfPassengers=5, gasTankSize=-1):
        super().__init__(makeAndModel,numberOfDoors,maximumNumberOfPassengers)
        self.gasTankSize = gasTankSize
    def setGasTankSize(self,newGasTankSize):
        self.gasTankSize = newGasTankSize
    def getGasTankSize(self):
        return self.gasTankSize
    def __str__(self):
        s = super.__str__()
        s += " Gas Tank Size: "+ str(self.getGasTankSize())
        