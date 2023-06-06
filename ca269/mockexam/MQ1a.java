public class MQ1a {
    private String title;
    private int number;
    private int marks;

    MQ1a (String title, int number, int marks) {
        setTitle(title);
        setNumber(number);
        setMarks(marks);
    }

    public void setTitle (String title) {
        this.title = title;
    }

    public void setNumber (int number) {
        this.number = number;
    }

    public void setMarks (int marks) {
        this.marks = marks;
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