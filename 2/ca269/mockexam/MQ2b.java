interface FamilyMember extends PersonalDetails {
    String getNickname();
    void setNickName(String name);
}

interface PersonalDetails {
    String getName();
    int getAge();
}

class Person implements FamilyMember {
    private String name;
    private int age;
    protected String nickname;

    Person (String name, int age, String nickname) {
        setName(name);
        setAge(age);
        setNickName(nickname);
    }

    public void setName (String name) {
        this.name = name;
    }

    public void setAge (int age) {
        this.age = age;
    }

    public void setNickName (String nickname) {
        this.nickname = nickname;
    }

    public String getName () {
        return this.name;
    }

    public int getAge () {
        return this.age;
    }

    public String getNickname () {
        return this.nickname;
    }

    public String toString () {
        return this.getName() + " (" + this.getNickname() + ")";
    }
}

public class MQ2b {
    public static void main (String args[]) {

    }
}