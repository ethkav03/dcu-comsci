/* receives a message and adds it to the Inbox */
public interface ReceiveMessage {
    // returns a success / failure message
    boolean receive(Activity activity);
}