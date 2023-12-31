import java.util.ArrayList;
public class FleetOfCars{
    private ArrayList<Car> cars;
    private int size;
    public FleetOfCars(){
        cars = new ArrayList<Car>();
        size = 0;
    }
    public void add(Car c){
        cars.add(c);
        size++;
    }
    public int getSize(){
        return size;
    }
    public void delete(int i){
        cars.remove(i);
        size--; //hell
    }
    public Car get(int i){
        return cars.get(i);
    }    
    public FleetOfCars search(String make){
        make = make.toLowerCase();
        FleetOfCars results = new FleetOfCars();
        for(int i = 0; i < cars.size(); i++){
            if(cars.get(i).getMakeAndModel().toLowerCase().contains(make)){
                results.add(cars.get(i));
            }
        }
        return results;
    }
    public String toString(){
        if (cars.size() == 0){
            return "No cars";
        }
        String s = "";
        for(int i = 0; i < cars.size(); i++){
            s += cars.get(i).toString() + "\n";
        }
        return s;
    }

}



/*
FleetOfCars: (25 points total)
FleetOfCars() 1 point
search(String s)→FleetOfCars 15 points
add(Car/GasolineCar/ElectricCar x) 2 points
getSize() → int 2 points
delete(int i) 5 points
get(i) → Ca
 */