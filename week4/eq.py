class Person:
    def __init__(self,name="1"):
        self.name = name

    def getName(self):
        return self.name
    def __eq__(self, o):
        return (self.getName() ==o.getName())
    def setName(self,newName):
        self.name=newName
    def __repr__(self):
        return self.getName()
if __name__=="__main__":
    p1 = Person("hello")
    p2 = p1
    print(p1.getName())
    p2.setName("joe")
    p3 = Person("hello")
    # breaking oop - encapsulation, and information hiding
    print(p1 == p2)
    print(p1==p3)
    print(p1.getName())
    l = [p1,p2,p3]
    for p in l:
        if (p.getName()=="joe"):
            print("hello joe", p)
