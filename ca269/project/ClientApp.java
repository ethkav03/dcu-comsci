public class ClientApp implements App {
    private Inbox inbox;
    private Outbox outbox;

    ClientApp () {
        inbox = new ClientInbox();
        outbox = new ClientOutbox();
    }

    public Inbox getInbox () {
        return this.inbox;
    }

    public Outbox getOutbox () {
        return this.outbox;
    }

    public String demo () {
        return "";
    }

    public static void main (String args[]) {
        Person p1 = new Person("https://www.w3.org/ns/activitystreams#Object", "Ethan Kavanagh", "kavane39", "Person 1");
        System.out.println("Person 1 added\n" + p1);
        
        Person p2 = new Person("https://www.w3.org/ns/activitystreams#Object", "Jamie Kavanagh", "kavanj49", "Person 2");
        System.out.println("Person 2 added\n" + p2);
    }
}