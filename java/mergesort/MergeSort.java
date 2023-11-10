import java.util.ArrayList;
import java.lang.Comparable;


public class MergeSort{
    public static ArrayList<Integer> merge(ArrayList<Integer> a, ArrayList<Integer> b){
        ArrayList<Integer> newList = new ArrayList<Integer>();
        int nextA = 0;
        int nextB = 0;
        while (nextA < a.size() && nextB < b.size()){
            System.out.println("nextA: " + nextA + " nextB: " + nextB);
            if (a.get(nextA).compareTo(b.get(nextB)) < 0){
                System.out.println("a added: a.get(nextA): " + a.get(nextA));
                newList.add(a.get(nextA));
                nextA++;
            }
            else if (a.get(nextA).compareTo(b.get(nextB)) >= 0){
                System.out.println("b added: b.get(nextB): " + b.get(nextB));
                newList.add(b.get(nextB));
                nextB++;
            }
            System.out.println(newList);
        }
        
        newList.addAll(newList.size(), a.subList(nextA, a.size()));
        newList.addAll(newList.size(), b.subList(nextB, b.size()));
        return newList;
    }
    // redo this function for Generic type <T>
    public static <T extends Comparable<T>> ArrayList<T> merge2(ArrayList<T> a, ArrayList<T> b){
        ArrayList<T> newList = new ArrayList<T>();
        int nextA = 0;
        int nextB = 0;
        while (nextA < a.size() && nextB < b.size()){
            System.out.println("nextA: " + nextA + " nextB: " + nextB);
            if (a.get(nextA).compareTo(b.get(nextB)) < 0){
                System.out.println("a added: a.get(nextA): " + a.get(nextA));
                newList.add(a.get(nextA));
                nextA++;
            }
            else if (a.get(nextA).compareTo(b.get(nextB)) >= 0){
                System.out.println("b added: b.get(nextB): " + b.get(nextB));
                newList.add(b.get(nextB));
                nextB++;
            }
            System.out.println(newList);
        }
        
        newList.addAll(newList.size(), a.subList(nextA, a.size()));
        newList.addAll(newList.size(), b.subList(nextB, b.size()));
        return newList;
    } 

    public static ArrayList<Integer> mergeSort(ArrayList<Integer> a){
        if (a.size() < 2){return a;}
        else{
            ArrayList<Integer> left = new ArrayList<Integer>();
            ArrayList<Integer> right = new ArrayList<Integer>();
            int mid = a.size()/2;
            left.addAll(a.subList(0, mid));
            right.addAll(a.subList(mid, a.size()));
            return merge(mergeSort(left), mergeSort(right));
        }
    }
    public static <T extends Comparable<T>> ArrayList<T> mergeSort2(ArrayList<T> a){
        //System.out.println("a: " + a);
        if (a.size() < 2){return a;}
        else{
            ArrayList<T> left = new ArrayList<T>();
            ArrayList<T> right = new ArrayList<T>();
            int mid = a.size()/2;
            left.addAll(a.subList(0, mid));
            right.addAll(a.subList(mid, a.size()));
            return merge2(mergeSort2(left), mergeSort2(right));
        }
    }
}
