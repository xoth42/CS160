import java.util.ArrayList;
import java.lang.Integer;
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class testMergeSort {
    @Test
    public void testMerge(){
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
        assertEquals(l3, toCompare);
    }
    @Test
    public void testMerge2(){
        ArrayList<Integer> l1 = new ArrayList<Integer>();
        l1.add(1);
        l1.add(3);
        l1.add(4);
        ArrayList<Integer> l2 = new ArrayList<Integer>();
        l2.add(2);
        l2.add(5);
        l2.add(6);
        ArrayList<Integer> l3 = MergeSort.merge2(l1,l2);
        System.out.println(l3);
        ArrayList<Integer> toCompare = new ArrayList<Integer>();
        int[] addToCompare = {1, 2, 3, 4, 5, 6};
        for (int i = 0;i<addToCompare.length;i++){
            toCompare.add(addToCompare[i]);
        }
        assertEquals(l3, toCompare);
    }
    @Test
    public void timeToTestMergeSort(){
        ArrayList<Integer> l1 = new ArrayList<Integer>();
        int[] addToArray = {6, 1, 5, 2, 8, 100,-20,0,40,30,40};
        for (int i = 0;i<addToArray.length;i++){l1.add(addToArray[i]);}
        int[] correctlySorted = {-20, 0, 1, 2, 5, 6, 8, 30, 40, 40, 100};
        ArrayList<Integer> toCompare = new ArrayList<Integer>();
        for (int i = 0;i<correctlySorted.length;i++){toCompare.add(correctlySorted[i]);}
        assertEquals(MergeSort.mergeSort(l1), toCompare);
    }
    @Test
    public void timeToTestMergeSort2(){
        ArrayList<Integer> l1 = new ArrayList<Integer>();
        int[] addToArray = {6, 1, 5, 2, 8, 100,-20,0,40,30,40};
        for (int i = 0;i<addToArray.length;i++){l1.add(addToArray[i]);}
        int[] correctlySorted = {-20, 0, 1, 2, 5, 6, 8, 30, 40, 40, 100};
        ArrayList<Integer> toCompare = new ArrayList<Integer>();
        for (int i = 0;i<correctlySorted.length;i++){toCompare.add(correctlySorted[i]);}
        assertEquals(MergeSort.mergeSort2(l1), toCompare);
    }
    @Test
    public void testExampleDataTypeMergeSort(){
        ArrayList<ExampleDataType> l1 = new ArrayList<ExampleDataType>();
        l1.add(new ExampleDataType(1, false));
        l1.add(new ExampleDataType(3, true));
        l1.add(new ExampleDataType(3, false));
        l1.add(new ExampleDataType(4, false));
        
        l1.add(new ExampleDataType(2, false));
        l1.add(new ExampleDataType(5, false));
        l1.add(new ExampleDataType(2, true));
        ArrayList<ExampleDataType> sorted = MergeSort.mergeSort2(l1);
        ArrayList<ExampleDataType> toCompare = new ArrayList<ExampleDataType>();
        int[] addToCompareInt = {1, 2, 2, 3, 3, 4, 5};
        boolean[] addToCompareBool = {false, true, false, true, false, false, false};
        for (int i = 0;i<addToCompareInt.length;i++){
            toCompare.add(new ExampleDataType(addToCompareInt[i], addToCompareBool[i]));
        }
        // print both
        System.out.println("Sorted:" + sorted);
        System.out.println("Compare:" + toCompare);
        for (int i = 0;i < sorted.size();i++){
            assertEquals(true, sorted.get(i) == toCompare.get(i));
        }
        //assertEquals(sorted, toCompare);
    }
}
