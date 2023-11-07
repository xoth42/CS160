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
    public int getMaximumNumberOfPassengers(){
        return maximumNumberOfPassangers;
    }
    public int getNumberOfDoors(){
        return numberOfDoors;
    }
    //setters
    public void setMakeAndModel(String makeAndModel){
        this.makeAndModel = makeAndModel;
    }
    public void setMaximumNumberOfPassengers(int maximumNumberOfPassangers){
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

/*
* Car: (13 points total)
Car(String makeAndModel, int maximumNumberOfPassengers, int numberOfDoors) 
5 points
setMakeAndModel(String m) 2 point
getMakeAndModel()→ string 2 point
setMaximumNumberOfPassengers(int m) 1 points
setNumberOfDoors(int m) manual check
getMaximumNumberOfPassengers()→ int 1 points
getNumberOfDoors()→ int manual check
toString()→ string 2 points

 */