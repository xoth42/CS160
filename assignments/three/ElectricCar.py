from Car import Car
class ElectricCar (Car):
    def __init__(self, makeAndModel="none assigned", numberOfDoors=4, maximumNumberOfPassengers=5, batterySize=-1):
        super().__init__(makeAndModel,numberOfDoors,maximumNumberOfPassengers)
        self.batterySize = batterySize
    def setBatterySize(self,newBatterySize:int):
        self.batterySize = newBatterySize
    def getBatterySize(self)->int:
        return self.batterySize
    def __str__(self):
        s = super(ElectricCar,self).__str__()
        s += ", Battery Size: "+ str(self.getBatterySize())
        return s

if __name__=="__main__":
    c1 = ElectricCar("Tesla X 2023",2,4,10)
    print(c1)