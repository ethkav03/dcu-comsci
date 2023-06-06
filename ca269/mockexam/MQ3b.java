import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Collections;
import java.util.Map;
import java.util.HashMap;

enum Grade {
    GradeFail,
    GradePass,
    GradeDistinction
}

class Student implements Comparable<Student> {
    private int marks;

    public int getMarks() {
        return this.marks;
    }

    public void setMarks (int marks) {
        this.marks = marks;
    }

    public int compareTo (Student student) {
        if (this.getMarks() > student.getMarks()) {
            return 1;
        } else if (this.getMarks() < student.getMarks()) {
            return -1;
        } else {
            return 0;
        }
    }
}

class Classroom {
    private List<Student> students;
    private Map<Grade, Integer> gradedStudents;

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

    public Queue<Student> getGraduatingStudents () {
        List<Student> graduatingStudents = new ArrayList<>();
        for (int i = 0; i < this.getStudents().size(); ++i) {
            if (this.getStudents().get(i).getMarks() >= 40) {
                graduatingStudents.add(this.getStudents().get(i));
            }
        }

        Collections.sort(graduatingStudents);

        Queue<Student> graduatedStudents = new LinkedList<>();
        for (Student student : graduatingStudents) {
            graduatedStudents.add(student);
        }

        return graduatedStudents;
    }

    public void calculateGradeStatistics () {
        int countFail = 0;
        int countPass = 0;
        int countDist = 0;
        for (Student student : this.getStudents()) {
            if (student.getMarks() < 40) {
                countFail++;
            } else if (student.getMarks() >= 75) {
                countDist++;
            } else {
                countPass++;
            }
        }

        if (gradedStudents == null) {
            gradedStudents = new HashMap<>();
        }

        gradedStudents.put(Grade.GradeFail, countFail);
        gradedStudents.put(Grade.GradePass, countPass);
        gradedStudents.put(Grade.GradeDistinction, countDist);
    }
}

public class MQ3b {
    public static void main (String args[]) {

    }
}