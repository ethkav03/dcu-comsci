class Individual {
    public String name;

    Individual (String name) {
        this.name = name;
    }

    public String toString () {
        return this.name;
    }
}

class Person extends Individual {
    protected String nickname;

    Person (String name, String nickname) {
        super(name);
        setNickName(nickname);
    }

    public void setNickName (String nickname) {
        this.nickname = nickname;
    }

    public String getNickname () {
        return this.nickname;
    }

    public String toString () {
        return this.name + " (" + this.getNickname() + ")";
    }
}

public class MQ2a {
    public static void main (String args[]) {

    }
}