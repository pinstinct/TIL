#include <stdio.h>

/* 두 정수를 입력받아 평균을 계산해 출력하는 프로그램
사용자로부터 두 정수를 입력받아 두 수의 평균을 계산하여 출력하는 예제를 작성합니다.
사용자 입력은 sacanf() 함수를 통해 받고, 출력은 printf() 함수를 이용해야 합니다.
단, 반드시 소수점 둘째 자리까지만 표시해야 하며, 변수는 2개만 선언합니다.
*/
int main(void)
{
    int a = 0;
    int b = 0;

    printf("두 정수를 입력하세요.: ");
    scanf("%d%d", &a, &b);
    printf("두 수의 평균은 %.2f 입니다.", (a + b) / 2.0);

    return 0;
}