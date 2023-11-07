
public class ElectricCar extends Car{
    private double batterySize;
    public ElectricCar(String makeAndModel,int maximumNumberOfPassangers, int numberOfDoors,double batterySize){
        super(makeAndModel,maximumNumberOfPassangers,numberOfDoors);
        this.batterySize = batterySize;
    }
    public double getBatterySize(){
        return batterySize;
    }
    public void setBatterySize(double batterySize){
        this.batterySize = batterySize;
    }
    public String toString(){
        return super.toString() + "\nBattery Size: " + batterySize;
    }
}
/*
ElectricCar: (11 points total)
    ElectricCar(String makeAndModel, int maximumNumberOfPassengers, int numberOfDoors, 
       double batterySize)  5 points
         toString()→ string 3 points
setBatterySize(double b) 2 point
            getBatterySize()→ double 1 poin
 */