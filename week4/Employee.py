import Person
class Employee(Person.Person):
    def __init__(self, name="none assigned", salary=15):
        super().__init__(name)  # super() is a function that creates an object
        self.salary= salary 
    def setSalary(self, newSalary):
        if (newSalary >= 15):
            self.salary=newSalary    
    def getSalary(self):
        return self.salary
    def __repr__(self):
        return(super().__repr__() + " " + str(self.getSalary()))
            
if __name__=="__main__":
    # hello? is it me you're looking for?
    e1 = Employee("Dwight Shrute")
    print(e1.getName())
    # Beets
    e1.setSalary(15.5)
    print(e1.getSalary())
    print(e1)