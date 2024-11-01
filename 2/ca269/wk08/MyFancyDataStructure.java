import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Arrays;

class Value implements Comparable<Value> {
    final int value;
    private static boolean SORT_LOWER;

    Value (int value) {
        this.value = value;
    }

    public int getValue() {
        return this.value;
    }

    public boolean isSortLower() {
        return SORT_LOWER == true;
    }

    public boolean isSortHigher() {
        return SORT_LOWER == false;
    }

    public static void setSortLower() {
        Value.SORT_LOWER = true;
    }

    public static void setSortHigher() {
        Value.SORT_LOWER = false;
    }

    public String toString() {
        return "" + this.value;
    }

    public int compareTo(Value value) {
        if (Value.SORT_LOWER) {
            return Integer.compare(this.value, value.value);
        }
        return -1 * Integer.compare(this.value, value.value);
    }
}

class PreferLowerValues implements Comparator<Value> {
    public boolean isEqual(Value val1, Value val2) {
        return val1.value == val2.value;
    }

    public boolean lessThan(Value val1, Value val2) {
        return val1.value < val2.value;
    }

    public int compare(Value val1, Value val2) {
        if (isEqual(val1, val2)) {
            return 0;
        } else if (lessThan(val1, val2)) {
            return -1;
        } else {
            return 1;
        }
    }
}

class PreferHigherValues implements Comparator<Value> {
    public boolean isEqual(Value val1, Value val2) {
        return val1.value == val2.value;
    }

    public boolean moreThan(Value val1, Value val2) {
        return val1.value > val2.value;
    }

    public int compare(Value val1, Value val2) {
        if (isEqual(val1, val2)) {
            return 0;
        } else if (moreThan(val1, val2)) {
            return -1;
        } else {
            return 1;
        }
    }
}

public class MyFancyDataStructure {

    public static void main(String args[]) {
        List<Value> list = Arrays.asList(new Value(2), new Value(3), new Value(1));

        Value.setSortLower();
        Collections.sort(list);
        System.out.println(list);
        // OUTPUT: [1, 2, 3]

        Value.setSortHigher();
        Collections.sort(list);
        System.out.println(list);
        // OUTPUT: [3, 2, 1]

        list = Arrays.asList(new Value(2), new Value(3), new Value(1));

        list.sort(new PreferLowerValues());
        System.out.println(list);
        // OUTPUT: [1, 2, 3]

        list.sort(new PreferHigherValues());
        System.out.println(list);
        // OUTPUT: [3, 2, 1]
    }
}
