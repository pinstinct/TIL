#include <stdio.h>

int main(void)
{
    int nInput;

    do
    {
        printf("Input number : ");
        scanf("%d", &nInput);
    } while (nInput < 0 || nInput > 10);

    puts("End");
    return 0;
}