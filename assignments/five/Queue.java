import java.util.ArrayList;
// first in, first out
public class Queue<T>{
    private ArrayList<T> elements;
    public Queue(){
        elements = new ArrayList<T>();
    }
    public void enqueue(T o){
        elements.add(o);
    }
    public T dequeue(){
        if (elements.size() == 0){
            return null;
        }
        else{
        return elements.remove(0);
        }
    }
    public boolean isEmpty(){
        return elements.size() == 0;
    }
    public T peek(){
        if (isEmpty()){
            return null;
        }
        return elements.get(0);
    }
}
