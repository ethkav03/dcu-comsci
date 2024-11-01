import java.util.Scanner;

public class AlarmClock
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        String alarm = input.nextLine();
        int alarm_minutes = minutes(alarm);

        int false_alarms = false_alarms(input, alarm, alarm_minutes);

        print_falses(false_alarms);
    }

    public static int minutes(String alarm)
    {
        String[] time = alarm.split(" ", 2);
        return Integer.parseInt(time[0]) * 60 + Integer.parseInt(time[1]);
    }

    public static int false_alarms(Scanner input, String alarm, int alarm_minutes)
    {
        int cnt = 0;
        int minutes = 0;

        do
        {
            alarm = input.nextLine();
            minutes = minutes(alarm);
            cnt++;
        }
        while (minutes < alarm_minutes);
        
        return cnt - 1;
    }

    public static void print_falses(int false_alarms)
    {
        System.out.println("false alarms: " + false_alarms);
    }
}