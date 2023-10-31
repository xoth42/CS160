
import ElectricCar, GasolineCar, LinkedList, unittest
# Unit testing
class testCases(unittest.TestCase):
    def testLinkdedListDelete(self):
        tesla = ElectricCar.ElectricCar("Tesla X 2023",2,4,10)
        toyota = GasolineCar.GasolineCar("Toyota Corolla 2000", 4,6,8)
        what = GasolineCar.GasolineCar("the Car 100", 1,2,3)
        Cars = LinkedList.LinkedList()
        Cars.add(tesla)
        Cars.add(toyota)
        Cars.add(what)
        Cars.delete(2)
        
        self.assertEqual(str(Cars),"List size: 2\nTesla X 2023, 2 doors, 4 max passengers, Battery Size: 10\nToyota Corolla 2000, 4 doors, 6 max passengers, Gas Tank Size: 8")
        Cars.add(tesla)
        Cars.add(toyota)
        Cars.delete(2)

        self.assertEqual(str(Cars),"List size: 3\nTesla X 2023, 2 doors, 4 max passengers, Battery Size: 10\nToyota Corolla 2000, 4 doors, 6 max passengers, Gas Tank Size: 8\nToyota Corolla 2000, 4 doors, 6 max passengers, Gas Tank Size: 8")
        
        Cars.delete(0)
        self.assertEqual(str(Cars),"List size: 2\nToyota Corolla 2000, 4 doors, 6 max passengers, Gas Tank Size: 8\nToyota Corolla 2000, 4 doors, 6 max passengers, Gas Tank Size: 8")
    def testLinkedListInsert(self):
        c1 = ElectricCar.ElectricCar("c1",1,1,1)
        c1str = str(c1)

        c2 = ElectricCar.ElectricCar("c2",2,2,2)
        l = LinkedList.LinkedList()
        for i in range(5):
            l.add(c1)
        l.insert(2,c2)
        st1 = "List size: 6\n" + c1str + "\n" + c1str + "\n" + str(c2) + "\n" + c1str + "\n" + c1str + "\n" + c1str
        
        self.assertEqual(str(l),st1)
        l.insert(0,c2)
        st2 = "List size: 7\n" + str(c2) + "\n" + c1str + "\n" + c1str + "\n" + str(c2) + "\n" + c1str + "\n" + c1str + "\n" + c1str
        self.assertEqual(str(l),st2)
        
        l.insert(7,c2)
        st3 = "List size: 8\n" + str(c2) + "\n" + c1str + "\n" + c1str + "\n" + str(c2) + "\n" + c1str + "\n" + c1str + "\n" + c1str + "\n" + str(c2)
        self.assertEqual(str(l),st3)


def main():
    tesla = ElectricCar.ElectricCar("Tesla X 2023",2,4,10)
    toyota = GasolineCar.GasolineCar("Toyota Corolla 2000", 4,6,8)
    what = GasolineCar.GasolineCar("the Car 100", 1,2,3)
    Cars = LinkedList.LinkedList()
    Cars.add(tesla)
    Cars.add(toyota)
    Cars.add(what)
    print(Cars)
    Cars.delete(2)
    print(Cars)
    '''
    tesla = ElectricCar.ElectricCar("Tesla X 2023",2,4,10)
    toyota = GasolineCar.GasolineCar("Toyota Corolla 2000", 4,6,8)
    what = GasolineCar.GasolineCar("the Car 100", 1,2,3)
    print(tesla,toyota,what) #Tesla X 2023, 2 doors, 4 max passengers, Battery Size: 10 Toyota Corolla 2000, 4 doors, 6 max passengers, Gas Tank Size: 8 the Car 100, 1 doors, 2 max passengers, Gas Tank Size: 3

    Cars = LinkedList.LinkedList()
    Cars.add(tesla)
    print(Cars)
    Cars.insert(0,toyota)
    print(Cars)
    Cars.delete(2)
    tesla = ElectricCar.ElectricCar("Tesla X 2023",2,4,10)
    toyota = GasolineCar.GasolineCar("Toyota Corolla 2000", 4,6,8)
    what = GasolineCar.GasolineCar("the Car 100", 1,2,3)
    Cars2 = LinkedList.LinkedList()
    Cars2.add(tesla)
    Cars2.add(toyota)
    Cars2.add(what)
    Cars2.delete(2)
    print(Cars2)'''
    # print(Cars)
    # the_tests = [1,5,7,32,4,6]
    # l = LinkedList.LinkedList()
    # for num in the_tests:
    #     l.add(num)
    # print(l)
    # l.insert(6,100)
    # print(l)
    # print(l.__getitem__(4))
if __name__ == "__main__":
    #unittest.main()
    main()