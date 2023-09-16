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
        
    def __str__(self):
        toReturn = "Make and Model: " + car1.get_make_model() + "\nNumber of doors: " +str(car1.get_num_doors()) + "\nMaximum number of passengers: "+str(car1.get_max_passengers())
        return toReturn
    
if __name__=="__main__":
    car1 = Car()
    car1.set_make_model("Dodge Dart")
    car1.set_num_doors(5)
    car1.set_max_passengers(7)
    # print("Model", car1.get_make_model(),"doors",car1.get_num_doors(),"max passengers",car1.get_max_passengers())
    print(car1)