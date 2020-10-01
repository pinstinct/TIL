#include <stdint.h>

/* 두 번째 직각 삼각형 출력하기
'*'가 출력되지 않은 왼쪽 여백은 '\t'를 출력합니다.
출력 예:
                *
            *   *
        *   *   *
    *   *   *   *
*   *   *   *   *
*/
int main(void)
{
    int i, j;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            if (i + j < 4)  printf("\t");
            else    printf("*\t");
        }
        putchar('\n');
    }
    return 0;
}