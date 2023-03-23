import java.util.ArrayList;
import java.util.List;

public class ClientOutbox implements Outbox {
    private List<Activity> messages;

    ClientOutbox () {
        messages = new ArrayList<>();
    }

    public int getCount () {
        return messages.size();
    }

    public boolean send (Activity activity) {
        return messages.add(activity);
    }

    public Activity deliverNext () {
        return (this.getCount() > 0) ? messages.remove(0) : null;
    }
}
