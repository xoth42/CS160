import java.lang.Comparable;
class ExampleDataType implements Comparable<ExampleDataType>{
    int value = 0;
    boolean isDifferent = false;
    public ExampleDataType(int value, boolean isDifferent){
        this.value = value;
        this.isDifferent = isDifferent;
    }
    private int getValue(){
        return this.value;
    }
    public int compareTo(ExampleDataType other){
        if (this.getValue() == other.getValue()){
            // if they are different from eachother, then the one that is different is less than the other
            if (this.isDifferent && !other.isDifferent){
                return -1;
            }
            else if (!this.isDifferent && other.isDifferent){
                return 1;
            }
            else{
                return 0;
            }
        }
        else{
            return this.getValue() - other.getValue();
        }
    }
    public String toString(){
        return "value: " + this.value + " isDifferent: " + this.isDifferent;
    }
    public boolean equals(ExampleDataType other){
        return this.value == other.value && this.isDifferent == other.isDifferent;
    }
}