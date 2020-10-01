#include <stdio.h>

/* 피라미드 출력하기
출력 예:
                *
            *   *   *
        *   *   *   *   *
    *   *   *   *   *   *   *
*   *   *   *   *   *   *   *   *
*/
int main(void)
{
    int i, j;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5 + i; j++)
        {
            if (i + j < 4)  putchar('\t');
            else            printf("*\t");
        }
        putchar('\n');
    }
    return 0;
}