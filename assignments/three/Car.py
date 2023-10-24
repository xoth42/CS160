class Car:
    def __init__(self, makeAndModel="none assigned", numberOfDoors=4, maximumNumberOfPassengers=5):
        self.makeAndModel = makeAndModel
        self.numberOfDoors = numberOfDoors
        self.maximumNumberOfPasengers = int(maximumNumberOfPassengers)
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
        self.previous = prev
    
    def setMakeAndModel(self,make):
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
        return f"{self.makeAndModel}, {self.numberOfDoors} doors, {self.getMaximumNumberOfPasengers} max passengers"

