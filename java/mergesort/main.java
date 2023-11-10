import java.util.ArrayList;
class main{
    public static void main(String[] args){
        ArrayList<Integer> l1 = new ArrayList<Integer>();
        l1.add(1);
        l1.add(3);
        l1.add(4);
        ArrayList<Integer> l2 = new ArrayList<Integer>();
        l2.add(2);
        l2.add(5);
        l2.add(6);
        ArrayList<Integer> l3 = MergeSort.merge(l1,l2);
        System.out.println(l3);
        ArrayList<Integer> toCompare = new ArrayList<Integer>();
        int[] addToCompare = {1, 2, 3, 4, 5, 6};
        for (int i = 0;i<addToCompare.length;i++){
            toCompare.add(addToCompare[i]);
        }
        ArrayList<ExampleDataType> l4 = new ArrayList<ExampleDataType>();
        l4.add(new ExampleDataType(1, false));
        l4.add(new ExampleDataType(100, true));
        l4.add(new ExampleDataType(100, false));
        l4.add(new ExampleDataType(2, false));
        l4.add(new ExampleDataType(100, true));
        ArrayList<ExampleDataType> l5 = MergeSort.mergeSort2(l4);
        System.out.println(l5);
    }

    
}