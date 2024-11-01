public class MQ1b {
    private String title;
    private int number;
    private int marks;

    MQ1b (String title, int number, int marks) {
        setTitle(title);
        setNumber(number);
        setMarks(marks);
    }

    MQ1b () {
        setTitle("untitled");
        setNumber(0);
        setMarks(0);
    }

    public void setTitle (String title) {
        this.title = title;
    }

    public void setNumber (int number) {
        this.number = number;
    }

    public void setMarks (int marks) {
        if (marks < 0) {
            this.marks = 0;
        } else {
            this.marks = marks;
        }
    }

    public String getTitle () {
        return this.title;
    }

    public int getNumber () {
        return this.number;
    }

    public int getMarks () {
        return this.marks;
    }

    public String toString () {
        return this.getNumber() + " " + this.getTitle() + " (" + this.getMarks() + " marks)";
    }
}