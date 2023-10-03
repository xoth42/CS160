import Car
class ElectricCar(Car.Car):
    #pass
    def __init__(self, make_model = "None assigned", num_doors = 4, max_passengers = 5):
        super().__init__(make_model, num_doors, max_passengers)
        