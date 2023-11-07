
public class GasolineCar extends Car{
    private double gasTankSize;
    public GasolineCar(String makeAndModel,int maximumNumberOfPassangers, int numberOfDoors,double gasTankSize){
        super(makeAndModel,maximumNumberOfPassangers,numberOfDoors);
        this.gasTankSize = gasTankSize;
    }
    public double getGasTankSize(){
        return gasTankSize;
    }
    public void setGasTankSize(double g){
        this.gasTankSize = g;
    }
    public String toString(){
        return super.toString() + "\nGas Tank Size: " + gasTankSize;
    }
}
/*
GasolineCar: (11 points total)
GasolineCar(String makeAndModel, int maximumNumberOfPassengers, int numberOfDoors,
          double gasTankSize 5 points
         toString()→ string 3 points
setGasTankSize(double g) 2 points
getGasTankSize()→ double 1 point
 */