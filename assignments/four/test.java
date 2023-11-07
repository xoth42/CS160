// Unit tests for FleetOfCars.java delete, and add
import static org.junit.Assert.assertEquals;
import org.junit.Test;
public class test {
    @Test
    public void testAddAndDelete() {
        FleetOfCars test = new FleetOfCars();
        Car car = new Car("test", 1, 1);
        test.add(car);
        assertEquals(1, test.getSize());
        test.delete(0);
        assertEquals(0, test.getSize());
        for (int i = 0; i < 3; i++) {
            test.add(car);
        }
        assertEquals(3, test.getSize());
        test.delete(2);
        assertEquals(2, test.getSize());
        String expected = car.toString() + "\n" + car.toString() + "\n";
        assertEquals(expected, test.toString());    
    }
    @Test
    public void testAdd() {
        FleetOfCars test = new FleetOfCars();
        Car car = new Car("test", 1, 1);
        test.add(car);
        assertEquals(1, test.getSize());
        String expected = car.toString() + "\n";
        assertEquals(expected, test.toString());
    }
}