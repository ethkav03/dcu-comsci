#include <stdio.h>

int get_int();

int main()
{
    int tries, convs, penalties, drops;

    printf("Tries: ");
    tries = get_int();
    printf("Conversions: ");
    convs = get_int();
    printf("Penalties: ");
    penalties = get_int();
    printf("Drop-goals: ");
    drops = get_int();

    int score = (tries * 5) + (convs * 2) + (penalties * 3) + (drops * 3);

    printf("%d\n", score);

    return 0;
}

int get_int()
{
    int n = 0;
    scanf("%d", &n);
    while (n < 0)
    {
        printf("Enter positive integer: ");
        scanf("%d", &n);
    }

    return n;
}