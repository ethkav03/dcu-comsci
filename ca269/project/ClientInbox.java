import java.util.ArrayList;
import java.util.List;

public class ClientInbox implements Inbox {
    private List<Activity> messages;

    ClientInbox () {
        messages = new ArrayList<>();
    }

    public int getCount () {
        return messages.size();
    }

    public Activity readNext () {
        return (this.getCount() > 0) ? messages.remove(0) : null;
    }

    public boolean receive(Activity activity) {
        return this.messages.add(activity);
    }
}
