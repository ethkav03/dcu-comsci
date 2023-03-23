/* removes and delivers the next message from inbox */
public interface DeliverNextMessage {
    // returns an Activity, or null if there are no messages
    Activity deliverNext();
}