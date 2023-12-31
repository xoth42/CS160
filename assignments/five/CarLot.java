import java.util.ArrayList;
import java.util.List;
public class CarLot{
    
    private Queue<Car> gasolineCars;
    private Queue<Car> hybridCars;
    private Queue<Car> electricCars;
    public CarLot(){
        gasolineCars = new Queue<Car>();
        hybridCars   = new Queue<Car>();
        electricCars = new Queue<Car>();
    }
    public boolean addCar(Car c){
        if (c.getPowerSource() == 1){
            gasolineCars.enqueue(c);
            return true;
        }
        else if (c.getPowerSource() == 2){
            hybridCars.enqueue(c);
            return true;
        }
        else if (c.getPowerSource() == 3){
            electricCars.enqueue(c);
            return true;
        }
        else{
            return false;
        }
    }
    public List<Car> processRequests(CarRequests r){
        ArrayList<Car> newCars = new ArrayList<Car>();
        while (r.hasPendingRequests()){
            int powerSource = r.getRequest();
            switch (powerSource) {
                case 1:
                    if (gasolineCars.isEmpty()){
                        newCars.add(new Car(0));
                    }
                    else{
                        newCars.add(gasolineCars.dequeue());
                    }
                    break;
                case 2:
                    if (hybridCars.isEmpty()){
                        newCars.add(new Car(0));
                    }
                    else{
                        newCars.add(hybridCars.dequeue());
                    }
                    break;
                case 3:
                    if (electricCars.isEmpty()){
                        newCars.add(new Car(0));
                    }
                    else{
                        newCars.add(electricCars.dequeue());
                    }
                    break;
                default:
                    newCars.add(new Car(0));
                    break;
            }
        }
        return newCars;
    }
}