public class Car{
    String makeAndModel;
    int maximumNumberOfPassangers;
    int numberOfDoors;
    //constructor 
    public Car(String makeAndModel,int maximumNumberOfPassangers, int numberOfDoors){
        this.makeAndModel = makeAndModel;
        this.maximumNumberOfPassangers = maximumNumberOfPassangers;
        this.numberOfDoors = numberOfDoors;
    }
    //getters
    public String getMakeAndModel(){
        return makeAndModel;
    }
    public int getMaximumNumberOfPassangers(){
        return maximumNumberOfPassangers;
    }
    public int getNumberOfDoors(){
        return numberOfDoors;
    }
    //setters
    public void setMakeAndModel(String makeAndModel){
        this.makeAndModel = makeAndModel;
    }
    public void setMaximumNumberOfPassangers(int maximumNumberOfPassangers){
        this.maximumNumberOfPassangers = maximumNumberOfPassangers;
    }
    public void setNumberOfDoors(int numberOfDoors){
        this.numberOfDoors = numberOfDoors;
    }
    //toString
    public String toString(){
        return "Make and Model: " + makeAndModel + "\nMaximum Number of Passangers: " + maximumNumberOfPassangers + "\nNumber of Doors: " + numberOfDoors;
    }
}