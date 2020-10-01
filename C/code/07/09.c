#include <stdio.h>

/* 피라미드 출력하기
출력 예:
                                *
                        *               *
                *               *               *
        *               *               *               *
*               *               *               *               *
*/
int main(void)
{
    int i, j;
    for (i = 0; i < 5; ++i)
    {
        for (j = 0; j < i + 5; j++)
        {
            if (i + j >= 4 && (i + j) % 2 == 0)     printf("*\t");
            else                                    putchar('\t');
        }
        putchar('\n');
    }
    return 0;
}