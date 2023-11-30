import java.util.ArrayList;
// first in, first out
public class Queue<T>{
    private T t;
    ArrayList<T> elements = new ArrayList<T>();
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
    public ArrayList<T> peek(){
        return new ArrayList<T>(elements);
    }
}
