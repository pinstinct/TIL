#include <stdio.h>

/* 1에서 10까지의 총합 구하기*/
int main(void)
{
    int i = 0, nResult = 0;
    while (i < 10)
        nResult += ++i;

    printf("Total: %d\n", nResult);
    return 0;
}