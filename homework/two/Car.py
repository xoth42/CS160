class Car:
    def __init__(self, make_model=None,make_year=None,color=None,doors=None,max_passengers=0):
        self.make_model = make_model
        self.make_year = make_year
        self.color = color
        self.num_doors = doors
        self.max_passengers = int(max_passengers)
        
    def set_make_model(self,make):
        self.make_model=make
    def get_make_model(self)->str:
        return self.make_model
    def get_num_doors(self)->int:
        return self.num_doors
    def set_num_doors(self, doors):
        self.num_doors=doors
    def set_max_passengers(self,num):
        self.max_passengers=num 
    def get_max_passengers(self)->int:
        return self.max_passengers
    def set_color(self,newColor:str):
        self.color=newColor
    def get_color(self)->str:
        return self.color
    def get_make_year(self)->int:
        return self.make_year
    def set_make_year(self, newYear:int):
        self.make_year=newYear

    def __repr__(self)->str:
        return f"{self.make_year} {self.make_model}, {self.color}, {self.num_doors} doors, {self.max_passengers} max passengers"

