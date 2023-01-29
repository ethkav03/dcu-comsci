import java.time.LocalDate;
import java.time.Period;

enum State {
    TODO, BEGN, HALT, WAIT, DONE;
}

public class Task {
    // Attributes
    private final String title;
    private String description;
    private LocalDate scheduled;
    private LocalDate deadline;
    private State state;

    public Task(String title, State state) {   
        this.title = title;
        setState(state);
    }

    // Getters
    public String getTitle() {
        return this.title;
    }

    public String getDescription() {
        return this.description;
    }

    public LocalDate getScheduled() {
        return this.scheduled;
    }

    public LocalDate getDeadline() {
        return this.deadline;
    }

    public State getState() {
        return this.state;
    }

    // Setters
    public void setDescription(String description) {
        this.description = description;
    }

    public void setScheduled(LocalDate scheduled) {
        this.scheduled = scheduled;
    }

    public void setDeadline(LocalDate deadline) {
        this.deadline = deadline;
    }

    public void setState(State state) {
        this.state = state;
    }

    // String method
    public String toString() {
        String message = this.title + " (" + this.state + ")";
        if (scheduled != null) {
        message += " scheduled: " + scheduled;
        }
        if (deadline != null) {
        message += " deadline: " + deadline;
        }
        return message;
    }

    // Task Main method
    public static void main(String[] args) {
        // test a simple Task object works correctly
        Task t1 = new Task("T1", State.TODO);
        LocalDate now = LocalDate.now();
        LocalDate.now();
        System.out.println(t1);

        // Check Chores work correctly on DONE -> repeat
        // note s2 is Task but object is type Chore
        Task s2 = new Chore("S2", State.TODO,
        LocalDate.now(),
        LocalDate.now().plus(Period.ofDays(7)));
        System.out.println(s2);
        s2.setState(State.DONE);
        System.out.println(s2);
        // verify the scheduled date has moved by +7 days

        Task s1 = new RepeatedTask("S1", State.TODO);
        System.out.println(s1);
        s1.setState(State.DONE);
        System.out.println(s1);

        Task t2 = new SharedTask("T2", "Alice");
        System.out.println(t2);

        Task t3 = new Depdency("T3", State.TODO, t1);
        System.out.println(t3);
        t3.setState(State.DONE);
        System.out.println(t3);
        t1.setState(State.DONE);
        t3.setState(State.DONE);
        System.out.println(t3);
    }
}

class Chore extends Task {
    // think how to use inheritence to avoid repeating fields from Task
    LocalDate repeat;

    Chore(String title, State state, LocalDate scheduled, LocalDate repeat) {
        super(title, state);
        setScheduled(scheduled);
        setRepeat(repeat);
    }

    public LocalDate getRepeat() {
        return this.repeat;
    }

    public void setRepeat(LocalDate repeat) {
        this.repeat = repeat;
    }

    @Override
    public void setState(State state) {
        super.setState(state);
        if (state == State.DONE) {
            super.setState(State.TODO);
            LocalDate repeat_new = repeat.plus(Period.ofDays(7));
            setScheduled(repeat);
            setRepeat(repeat_new);
        }
    }
}

class RepeatedTask extends Task {
    RepeatedTask(String title, State state) {
        super(title, state);
    }
    @Override
    public void setState(State state) {
        if (state == State.DONE) {
            super.setState(State.TODO);
        }
        else {
            super.setState(state);
        }
    }
}

class SharedTask extends Task {
    String name;

    SharedTask(String title, String name) {
        super(title, State.WAIT);
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        String message = this.getTitle() + " (" + this.getState() + ")";
        if (name != null) {
        message += " shared with: " + name;
        }
        return message;
    }
}

class Depdency extends Task {
    Task task_dependency;
    Depdency(String title, State state, Task task_dependency) {
        super(title, state);
        this.task_dependency = task_dependency;
    }
    
    public Task getTask_dependency() {
        return task_dependency;
    }

    public void setTask_dependency(Task task_dependency) {
        this.task_dependency = task_dependency;
    }

    @Override
    public void setState(State state) {
        super.setState(state);
        if (task_dependency.getState() == State.DONE)
        {
            super.setState(State.DONE);
        }
        else
        {
            super.setState(State.HALT);
        }
    }

    public String toString() {
        String message = this.getTitle() + " (" + this.getState() + ")";
        if (task_dependency.getTitle() != null) {
            message += " dependent on: " + task_dependency.getTitle();
        }
        if (task_dependency.getState() != null) {
            message += " (" + task_dependency.getState() + ")";
        }
        return message;
    }
}