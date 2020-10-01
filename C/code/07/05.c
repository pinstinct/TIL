#include <stdio.h>

/* 첫 번째 직각 삼각형 출력하기
출력 예:
*
* *
* * *
* * * *
* * * * *
*/
int main(void)
{
    int i = 0, j = 0;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < i + 1; j++)
            printf("*\t");
        putchar('\n');
    }
    return 0;
}