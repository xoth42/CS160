import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
public class QueueTests{
    @Test
    public void testQueue(){
        Queue<Integer> q = new Queue<Integer>();
        q.enqueue(1);
        q.enqueue(2);
        // ArrayList<int> check = q.peek();
        assertEquals((Integer)1, q.dequeue());
        assertEquals((Integer)2, q.dequeue());
        assertEquals(null, q.dequeue());
        q.enqueue(14);
        assertEquals((Integer)14, q.peek());
        q.dequeue();
        assertEquals(null, q.peek());
        assertEquals(null, q.dequeue());
        q.enqueue(10);
        q.enqueue(11);
        q.enqueue(12);
        q.enqueue(13);
        assertEquals((Integer)10, q.dequeue());
        assertFalse(q.isEmpty());
        assertEquals((Integer)11, q.peek());
        assertEquals((Integer)11, q.dequeue());
        assertEquals((Integer)12, q.dequeue());
        assertEquals((Integer)13, q.dequeue());
        assertTrue(q.isEmpty());
    }
}
