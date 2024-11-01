#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 4; i++)
    {
        for (int j = (i * 5) + 30; j < (i * 5) + 35; j++)
        {
            float cms = (float)j / 2.54;
            printf("%.2f ", cms);
        }
        printf("\n");
    }
}