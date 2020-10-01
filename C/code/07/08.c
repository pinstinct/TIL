#include <stdio.h>

/* 1~100까지의 숫자 중 4의 배수가 몇 개이며,
이들의 총합이 얼마인지 계산해 출력하는 프로그램을 작성하세요.
*/
int main(void)
{
    int nResult = 0, i;
    for (i = 0; i <= 100; ++i)
    {
        if (i % 4 == 0) nResult += i;
    }
    printf("1~100까지의 숫자 중 4의 배수는 %d개\n", 100/4);
    printf("이들의 총합은 %d입니다.", nResult);
    return 0;
}