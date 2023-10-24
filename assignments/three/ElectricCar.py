import Car

class ElectricCar (Car.Car):
    def __init__(self, makeAndModel="none assigned", numberOfDoors=4, maximumNumberOfPassengers=5, batterySize=-1):
        super().__init__(makeAndModel,numberOfDoors,maximumNumberOfPassengers)
        self.batterySize = batterySize
    def setBatterySize(self,newBatterySize):
        self.batterySize = newBatterySize
    def getBatterySize(self):
        return self.batterySize
    def __str__(self):
        s = super().__str__()
        s += " Battery Size: "+ str(self.getBatterySize())
        