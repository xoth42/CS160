import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.List;
public class CarLotTests{
    @Test
    public void testCarLots(){
        CarLot cl = new CarLot();
        CarRequests cr = new CarRequests();
        cr.addRequest(1);
        cr.addRequest(2);
        cr.addRequest(3);
        cr.addRequest(0);
        cl.addCar(new Car(1));
        cl.addCar(new Car(2));
        cl.addCar(new Car(3));
        cl.addCar(new Car(1));
        cl.addCar(new Car(2));
        List<Car> output = cl.processRequests(cr);
        assertEquals(1, output.get(0).getPowerSource());
        assertEquals(2, output.get(1).getPowerSource());
        assertEquals(3, output.get(2).getPowerSource());
        assertEquals(0, output.get(3).getId());
    }
}