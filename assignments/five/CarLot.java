import java.util.ArrayList;
import java.util.List;
public class CarLot{
    /*
     * Class CarLot will have a method called processRequests. processRequests will receive as
input an object of type CarRequests. The output of processRequests will be a list (not an
array, not a CarLot) of objects of type Car, satisfying the requests being placed by
customers. These objects will come from the queues that class CarLot is keeping internally.
For example, with aCarRequests object storing a Queue with values 1,2,3,2,2
processRequests will return a list that has one car from the gasoline cars queue, one car
from the hybrid cars queue, one car from the electric cars queue, and two cars from the
hybrid cars queue, in that order. At any point that a car is placed in the list that
processRequests will return, it is taken out of the internal queue it was in. Your code must
only use valid queue operations while working with the queues that CarLot keeps internally.
If at any point the Queue inside CarRequests has a request that cannot be satisfied (for
example, a customer is requesting a hybrid car, but the queue for hybrid cars is empty) a
Car with an id of zero will be placed in the output list
     */
    private Queue<Car> gasolineCars = new Queue<Car>();
    private Queue<Car> hybridCars   = new Queue<Car>();
    private Queue<Car> electricCars = new Queue<Car>();
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
        Arraylist<Car> newCars = new ArrayList<Car>();
        while (r.hasPendingRequests()){
            int powerSource = r.getRequest();
            if (powerSource == 1){
                // gasoline
                newCars.add(gasolineCars.dequeue())
            } /....
        }
    }
}