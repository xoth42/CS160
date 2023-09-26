import Person
class Student(Person.Person):
    def __init__(self,name="none assigned",major="none declared"):
        super().__init__(name)
        self.major = major
    def getMajor(self):
        return self.major
    def setMajor(self,newMajor):
        self.major=newMajor
        