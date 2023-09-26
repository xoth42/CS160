class Person:
    def __init__(self,name="none assigned"):
        self.name = name
    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName
        
if __name__=="__main__":
    p1 = Person("Jaime")
    print(p1.getName())