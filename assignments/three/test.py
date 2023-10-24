import ElectricCar, GasolineCar, LinkedList
tesla = ElectricCar.ElectricCar("Tesla X 2023",2,4,10)
toyota = GasolineCar.GasolineCar("Toyota Corolla 2000", 4,6,8)
what = GasolineCar.GasolineCar("the Car 100", 1,2,3)
Cars = LinkedList.LinkedList()
Cars.add(tesla)
print(Cars)
Cars.insert(0,toyota)
print(Cars)