import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class CarTests{
    @Test
    public void testCar(){
        Car c = new Car(1);
        assertEquals(1, c.getPowerSource());
        Car c1 = new Car(1, 1, 1);
        assertEquals(1, c1.getId());
    }
}