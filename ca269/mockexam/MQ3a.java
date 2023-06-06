import java.util.List;
import java.util.ArrayList;

class Student {
    private int marks;
    public int getMarks() { return this.marks; }
    public void setMarks (int marks) { this.marks = marks; }
}

class Classroom {
    private List<Student> students;

    Classroom () {
        students = new ArrayList<>();
    }

    public List<Student> getStudents () {
        return this.students;
    }

    public void addStudent (Student student) {
        this.getStudents().add(student);
    }

    public List<Student> getGradedStudents (int marks) {
        List<Student> getGradedStudents = new ArrayList<>();
        for (int i = 0; i < this.getStudents().size(); ++i) {
            if (this.getStudents().get(i).getMarks() >= marks) {
                getGradedStudents.add(this.getStudents().get(i));
            }
        }
        return getGradedStudents;
    }

    public int getAverageMarks () {
        int total = 0;
        for (int i = 0; i < this.getStudents().size(); ++i) {
            total += this.getStudents().get(i).getMarks();
        }
        return total / this.getStudents().size();
    }

    public boolean hasStudent (Student student) {
        for (int i = 0; i < this.getStudents().size(); ++i) {
            if (this.getStudents().get(i) == student) {
                return true;
            }
        }
        return false;
    }
}

public class MQ3a {
    public static void main (String args[]) {

    }
}