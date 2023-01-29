import java.util.Scanner;

public class VowelAge
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        System.out.print("");
        String name = input.nextLine();

        System.out.print("");
        String age = input.nextLine();

        int vowels = count_vowels(name);

        String aom = find_aom(Integer.parseInt(age));

        print_output(name, vowels, aom);
    }

    public static int count_vowels(String name)
    {
        return name.replaceAll("[^aeiouAEIOU]", "").length();
    }

    public static String find_aom(int age)
    {
        return age < 18 ? "a minor" : "an adult";
    }

    public static void print_output(String name, int cnt, String aom)
    {
        System.out.println("Hello " + name + ", you have " + cnt + " vowels, and you are " + aom);
    }
}