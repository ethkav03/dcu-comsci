/* sends a message and adds it to the Outbox */
public interface SendMessage {
    boolean send(Activity activity);
}