class Person:
    def __init__(self,name="none assigned"):
        self.name = name
    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName
    def __repr__(self):
        return(self.getName())
    
if __name__=="__main__":
    p1 = Person("Jaime")
    print(p1)