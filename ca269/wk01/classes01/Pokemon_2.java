import java.util.Arrays;
import java.util.Scanner;

class Ethan 
{
    String name = "";

    public String sayHello(String name)
    {
        return "Hello, " + name;
    }

    public Ethan(String name)
    {
        this.name = name;
    }

    public String toString()
    {
        return "Hello, " + this.name;
    }
}

public class Pokemon_1 {
    // class-only information
    static String GENERATION = "Gen-I";
    // final = no further changes allowed
    static final String LOCATION = "Kanto";
    static final String[] VERSIONS = { "RED", "GREEN", "YELLOW", "BLUE" };

    // copy for each instance
    int health_max = 100;
    int moves_max = 5;
    String type = "";
    String name = "";

    /** this is a constructor, it 'creates' objects
     * @param String name: the name of the pokemeon
     * @param String type: the type of pokemon
     * @param int health_max: the max health of that pokemon
     */
    public Pokemon_1(String name, String type, int health_max) {
        this.name = name;
        this.type = type;
        if (health_max > 0) {
            this.health_max = health_max;
        }
    }

    /** this is the "string" method that is called when we want to print
     * an instance as a string. In this case it returns the name and
     * a summary of that pokemon's type and max health
     */
    public String toString() {
        return this.name + " (" + this.type + ", " + this.health_max + ")";
    }
}