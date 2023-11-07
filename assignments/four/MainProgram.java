import java.util.Scanner;
import java.lang.Integer;
import java.lang.Double;
class MainProgram{
    public static  String menu = "Enter option from list below:\n\t1) Display complete directory\n\t2) Enter new Car\n\t3) Search for Car\n\t4) Modify Car information\n\t5) Delete a record.\n\tQ) Quit\nEnter your option: ";
    static FleetOfCars fleet;
    static Scanner input;
    private static void startUp(){
        input = new Scanner(System.in);
    }
    private static void shutDown(){
        input.close();
    }
    private static String openMenu(){
        System.out.print(menu);
        String in = input.nextLine().toLowerCase();
        return in;
    }
    private static boolean promptYesNo(){
        String in = input.nextLine().toLowerCase();
        return (in.equals("y") || in.equals("yes"));
    }
    private static void modifyCars(){
        FleetOfCars searchResults = promptSearch();
        for (int i = 0;i < searchResults.getSize();i++){
            System.out.print(searchResults.get(i) + "\nDo you want to modify this record?: ");
            
            if (promptYesNo()){
                System.out.print("Do you want to change the make and model?: ");
                if (promptYesNo()){
                    System.out.print("Enter new make and model: ");
                    String newMake = input.nextLine();
                    searchResults.get(i).setMakeAndModel(newMake);
                }
                System.out.print("Do you want to change the maximum number of passengers?: ");
                if (promptYesNo()){
                    System.out.print("Enter new maximum number of passengers: ");
                    int newMax = Integer.parseInt(input.nextLine());
                    searchResults.get(i).setMaximumNumberOfPassangers(newMax);
                }
                System.out.print("Do you want to change the number of doors?: ");
                if (promptYesNo()){
                    System.out.print("Enter new number of doors: ");
                    int newDoors = Integer.parseInt(input.nextLine());
                    searchResults.get(i).setNumberOfDoors(newDoors);
                }
            

            }
        }
    }
    private static FleetOfCars promptSearch(){
        System.out.print("Enter make and model to search: ");
        String query = input.nextLine();
        FleetOfCars searchResults = fleet.search(query);
        return searchResults;
    }
    private static void searchForCars(){
        FleetOfCars searchResults = promptSearch();
        System.out.println(searchResults);
    }
    private static void enterNewCar(){        
        System.out.print("Enter make and model: ");
        String makeAndModel = input.nextLine();
        System.out.print("Enter maximum number of passangers: ");
        int maximumNumberOfPassangers = Integer.parseInt(input.nextLine());
        System.out.print("Enter number of doors: ");
        int numberOfDoors = Integer.parseInt(input.nextLine());

        // check if car is normal, gas, or electric
        System.out.print("Enter type of car (gas, electric, or normal): ");
        String type = input.nextLine().toLowerCase();

        String carStr;

        if (type.equals("gas")){
            System.out.print("Enter gas tank size: ");
            double gasTankSize = Double.parseDouble(input.nextLine());
            GasolineCar car = new GasolineCar(makeAndModel,maximumNumberOfPassangers,numberOfDoors,gasTankSize);
            fleet.addCar(car);
            carStr = car.toString();
        }
        else if (type.equals("electric")){
            System.out.print("Enter battery size: ");
            double batterySize = Double.parseDouble(input.nextLine());
            ElectricCar car = new ElectricCar(makeAndModel,maximumNumberOfPassangers,numberOfDoors,batterySize);
            fleet.addCar(car);
            carStr = car.toString();
        }
        else {
            Car car = new Car(makeAndModel,maximumNumberOfPassangers,numberOfDoors);
            fleet.addCar(car);
            carStr = car.toString();
        }
        System.out.println("Created new car" + carStr);
    }
    private static void deleteRecord(){
        System.out.print("Enter the index of the record you want to delete: ");
        int index = Integer.parseInt(input.nextLine());

        // todo handle this error: java.lang.IndexOutOfBoundsException
        System.out.print(fleet.get(index) + "\nAre you sure you want to this?: ");
        if (promptYesNo()){fleet.delete(index);}
    }
    public static void main(String[] args){
        String entered = "";
        fleet = new FleetOfCars();
        startUp();
        while (!entered.equals("q")){
            // note on https://piazza.com/class/lkbviu05tay3ia/post/299
            // switch statements are not gonna work
            entered = openMenu();
            if (entered.equals("1")){
                //display complete directory
                System.out.println(fleet);}
            else if (entered.equals("2")){ //enter new car
                enterNewCar();}
            else if (entered.equals("3")){ //search for car
                searchForCars();
            }
            else if (entered.equals("4")){//modify car information
                modifyCars();
            }
            else if (entered.equals("5")){//delete a record
                deleteRecord();
            }
            else{
                System.out.println("Invalid input");
            }
            
            

        }
        shutDown();
    }
}