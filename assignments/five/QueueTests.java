import org.junit.Test;
import static org.junit.Assert.assertEquals;
public class QueueTests{
    @Test
    public void testQueue(){
        Queue<Integer> q = new Queue<Integer>();
        q.enqueue(1);
        q.enqueue(2);
        // ArrayList<int> check = q.peek();
        assertEquals((Integer)1, q.dequeue());
    }
}
