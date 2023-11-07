import java.util.Scanner;
class MainProgram{
    public static  String menu = "Enter option from list below:\n\t1) Display complete directory\n\t2) Enter new Car\n\t3) Search for Car\n\t4) Modify Car information\n\t5) Delete a record.\n\tQ) Quit\nEnter your option: ";
    static FleetOfCars fleet;
    private static String openMenu(){
        Scanner input = new Scanner(System.in);
        System.out.print(menu);
        String in = input.nextLine().toLowerCase();
        input.close();
        return in;
    }
    private static void enterNewCar(){
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter make and model: ");
        String makeAndModel = input.nextLine();
        System.out.println("Enter maximum number of passangers: ");
        int maximumNumberOfPassangers = input.nextInt();
        System.out.println("Enter number of doors: ");
        int numberOfDoors = input.nextInt();

        // check if car is normal, gas, or electric
        System.out.println("Enter type of car (gas, electric, or normal): ");
        String type = input.nextLine().toLowerCase();


        if (type.equals("gas")){
            System.out.println("Enter gas tank size: ");
            double gasTankSize = input.nextDouble();
            GasolineCar car = new GasolineCar(makeAndModel,maximumNumberOfPassangers,numberOfDoors,gasTankSize);
            fleet.addCar(car);
        }
        else if (type.equals("electric")){
            System.out.println("Enter battery size: ");
            double batterySize = input.nextDouble();
            ElectricCar car = new ElectricCar(makeAndModel,maximumNumberOfPassangers,numberOfDoors,batterySize);
            fleet.addCar(car);
        }
        else{
            Car car = new Car(makeAndModel,maximumNumberOfPassangers,numberOfDoors);
            fleet.addCar(car);
        }
        input.close();
    }
    public static void main(String[] args){
        String entered = "";
        fleet = new FleetOfCars();
        while (entered != "q"){
            entered = openMenu();
            switch(entered){
                case "1": //display complete directory
                    System.out.println(fleet);
                    break;
                case "2": //enter new car
                    enterNewCar();
                    break;
                case "3": //search for car
                    System.out.println("Search for Car");
                    break;
                case "4"://modify car information
                    System.out.println("Modify Car information");
                    break;
                case "5"://delete a record
                    System.out.println("Delete a record.");
                    break;
                case "q"://quit
                    break;
                default:
                    System.out.println("Invalid input");
                    break;
            }

        }
    }
}