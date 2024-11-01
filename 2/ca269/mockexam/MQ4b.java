/**
 * @author kavane39
 * Date: 18/04/2023 
 */

/**
 * Exceptio for no cake
 */
class NoCakeFoundException extends Exception {
    NoCakeFoundException () { }
    NoCakeFoundException (String e) { }
    /**
     * @return String
     */
    public String toString () {
        return "The Cake is a Lie!";
    }
}

class Cake {
    /**
     * @return void
     */
    public void getCake () throws NoCakeFoundException {
        throw new NoCakeFoundException();
    }

    /**
     * @return void
     */
    public void eatCake () {
        try {
            this.getCake();
        } catch (NoCakeFoundException e) {
            System.out.println(e);
        }
    }
}

public class MQ4b {
    public static void main (String args[]) {

    }
}