"""An object has attributes, and methods that operate on those attributes

What attributes does an employee have?
what methods should operate on those attributes?
"""
class Employee:
    
    """__init__ is always the method to create a constructor in python. A constructor "sets things up". When this object is created, __init__ is run. It needs the parameter self as well (must be named self). Self is the object. It is passed automatically.
    """
    def __init__(self):
        self.name =""
        self.address = ""
        self.phone = ""
        self.department = ""
        self.hourlySalary = 15.0
        self.letsMakeSureWeUnderstandTheDifference = True
        
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return(self.name)
    
    def aMethodWithALocalVariable(self):
        letsMakeSureWeUnderstandTheDifference = False
        print("the local variable has a value of", letsMakeSureWeUnderstandTheDifference)
        print("the attribute has a value of", self.letsMakeSureWeUnderstandTheDifference)

    def someOtherMethod(self):
        self.aNewAttribute = 999
        
    def accessingTheNewAttribute(self):
        print(self.aNewAttribute)
    
if __name__ == "__main__":
    # Call methods for objects, that are instantiations for a class. Don't call methods for the class!! 
    employee1 = Employee()
    employee1.setName("Jamie")
    print(employee1.getName())
    
    employee2 = Employee()
    employee2.setName("Maria")
    print(employee1.getName())
    
    employee1.aMethodWithALocalVariable()
    employee1.someOtherMethod()
    employee1.accessingTheNewAttribute()