public class CarRequests{
    private Queue<Integer> requests = new Queue<Integer>();
    public void addRequest(int powerSource){
        requests.enqueue(powerSource);
    }
    public Integer getRequest(){
        return requests.dequeue();
    }
    public boolean hasPendingRequests(){
        return !requests.isEmpty();
    }
}