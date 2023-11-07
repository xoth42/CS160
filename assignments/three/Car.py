class Car:
    def __init__(self, makeAndModel="none assigned", numberOfDoors=4, maximumNumberOfPassengers=5):
        self.makeAndModel = makeAndModel
        self.numberOfDoors = numberOfDoors
        self.maximumNumberOfPasengers = int(maximumNumberOfPassengers)
        # self must not have next or previous, because node will handle this.
        '''
        # for linked list

        self.next = None
        self.previous = None
        
    #Linked stuff
    def getNext(self):
        return self.next
    def getPrevious(self):
        return self.previous
    def setNext(self,next):
        self.next = next
    def setPrevious(self,prev):
        self.previous = prev'''
    
    def setMakeAndModel(self,make:str):
        self.makeAndModel=make
    def getMakeAndModel(self)->str:
        return self.makeAndModel
    def getNumberOfDoors(self)->int:
        return self.numberOfDoors
    def setNumberOfDoors(self, doors):
        self.numberOfDoors=doors
    def setMaximumNumberOfPasengers(self,num):
        self.maximumNumberOfPasengers=num 
    def getMaximumNumberOfPasengers(self)->int:
        return self.maximumNumberOfPasengers
    
    def __str__(self)->str:
        return f"{self.makeAndModel}, {self.numberOfDoors} doors, {self.getMaximumNumberOfPasengers()} max passengers"
    
    """Car.getMakeAndModel()() works correctly (0/1)
Car.getMaximumNumberOfPasengers() works correctly (0/1)
Car constructor takes correct arguments (0/5)
Car.setMakeAndModel() and Car.getMakeAndModel() work correctly (0/1)
what the hell is going on here

"""


if __name__=="__main__":
    c1 = Car()
    print(c1)
    print("make:", c1.getMakeAndModel())