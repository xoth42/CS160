
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