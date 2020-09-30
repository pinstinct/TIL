#include <stdio.h>

/* 버스요금 계산 프로그램
버스의 기본요금 1,000원이라고 가정하고,
나이가 20세 미만은 요금을 25% 할인해주고 20세 이상은 할인을 해주지 않기로 합니다.
요금 계산 과정에서 자료형에 주의합니다.
*/
int main(void)
{
    int nAge = 0, fee = 1000;
    printf("나이를 입력하세요.  : ");
    scanf("%d", &nAge);

    if (nAge < 20)
        fee = fee * 75 / 100;

    printf("요금 : %d\n", fee);
    return 0;
}
