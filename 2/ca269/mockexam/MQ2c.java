class Person {
    private String name;
}

class Employee extends Person {
    private String employeeID;
}

interface VIP {
    String VIPStatus();
}

class CompanyGathering {
    public boolean admitPerson (Person person) {
        return (person instanceof Employee || person instanceof VIP);
    }
}

public class MQ2c {
    public static void main (String args[]) {

    }
}