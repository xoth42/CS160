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
        if (fleet.getSize() == 0){
            System.out.println("The directory is empty");
            return;
        }
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
                    searchResults.get(i).setMaximumNumberOfPassengers(newMax);
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
        if (searchResults.getSize() == 0){
            System.out.println("No records found.");
        }
        return searchResults;
    }
    private static void searchForCars(){
        if (fleet.getSize() == 0){
            System.out.println("The directory is empty");
            return;
        }
        FleetOfCars searchResults = promptSearch();
        if (searchResults.getSize() != 0){  
            System.out.println(searchResults);
        }
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

        if (type.equals("gas")|type.equals("g")){
            System.out.print("Enter gas tank size: ");
            double gasTankSize = Double.parseDouble(input.nextLine());
            GasolineCar car = new GasolineCar(makeAndModel,maximumNumberOfPassangers,numberOfDoors,gasTankSize);
            fleet.add(car);
        }
        else if (type.equals("electric")|type.equals("e")){
            System.out.print("Enter battery size: ");
            double batterySize = Double.parseDouble(input.nextLine());
            ElectricCar car = new ElectricCar(makeAndModel,maximumNumberOfPassangers,numberOfDoors,batterySize);
            fleet.add(car);
        }
        else {
            Car car = new Car(makeAndModel,maximumNumberOfPassangers,numberOfDoors);
            fleet.add(car);
        }
    }
    private static void deleteRecord(){
        if (fleet.getSize() == 0){
            System.out.println("The directory is empty");
            return;
        }
        System.out.print("Enter the index of the record you want to delete: ");
        int index;
        try{
            index = Integer.parseInt(input.nextLine());
        }
        catch (NumberFormatException e){
            //System.out.println(fleet);
            System.out.println("Invalid enter a number from 0 to " + (fleet.getSize()) + ".");
            return;
        }

        // todo handle this error: java.lang.IndexOutOfBoundsException
        try {
            System.out.print(fleet.get(index) + "\nAre you sure you want to this?: ");
            if (promptYesNo()){
                fleet.delete(index);
            }
        }
        catch (IndexOutOfBoundsException e){
            //System.out.println(fleet);
            System.out.println("Invalid index. There are " + fleet.getSize() + " cars in the directory.");
        }
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