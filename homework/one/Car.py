class Car:
    def __init__(self, mm="None assigned",doors=4,max_passengers=5):
        self.make_model = mm
        self.num_doors = doors
        self.max_passengers = max_passengers
        
    def set_make_model(self,make):
        self.make_model=make
    def get_make_model(self):
        return self.make_model
    def get_num_doors(self):
        return self.num_doors
    def set_num_doors(self, doors):
        self.num_doors=doors
    def set_max_passengers(self,num):
        self.max_passengers=num 
    def get_max_passengers(self):
        return self.max_passengers

