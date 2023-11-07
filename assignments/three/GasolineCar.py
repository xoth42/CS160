from Car import Car

class GasolineCar (Car):
    def __init__(self, makeAndModel="none assigned", numberOfDoors=4, maximumNumberOfPassengers=5, gasTankSize=-1):
        super().__init__(makeAndModel,numberOfDoors,maximumNumberOfPassengers)
        self.gasTankSize = gasTankSize
    def setGasTankSize(self,newGasTankSize:int):
        self.gasTankSize = newGasTankSize
    def getGasTankSize(self)->int:
        return self.gasTankSize
    def __str__(self):
        s = super().__str__()
        s += ", Gas Tank Size: "+ str(self.getGasTankSize())
        return s
    
if __name__=="__main__":
    c1 = GasolineCar("Toyota Corolla 2000", 4,6,8)
    print(c1)
    
        