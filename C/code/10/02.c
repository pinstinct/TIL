#include <stdio.h>

/* 기본요금과 나이를 매개변수로 받아서 나이에 따른 최종요금을 계산해 반환하는 GetFee() 함수를 작성하세요.
0~3 : 100% (무료)
4~13 : 50%
14~19 : 75%
20이상 : 0%
*/
int GetFee(int age, int fee)
{
    int nResult = 0;
    if (age >= 20)      nResult = fee;
    else if (age >= 14) nResult = fee * 75 / 100;
    else if (age >= 4)  nResult = fee * 50 / 100;
    else if (age >= 0)  nResult = 0;
    return nResult;
}

int main(void)
{
    int nAge = 0;
    scanf("%d", &nAge);
    printf("나이: %d, 요금: %d", nAge, GetFee(nAge, 1000));
    return 0;
}