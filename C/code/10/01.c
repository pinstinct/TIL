#include <stdio.h>

/* 사용자가 입력한 값에서 최대값 구하기와 코드 분할
main() 함수의 코드를 다음과 같이 수정해도 01_before.c와 같은 실행결과가 나오도록
3개의 사용자 정의 함수를 추가합니다.
*/
int GetData(void)
{
    int nData = 0;

    printf("정수를 입력하세요. : ");
    scanf("%d", &nData);
    return nData;
}

int GetMax(int a, int b, int c)
{
    int nMax = a;

    if (b > nMax)   nMax = b;
    if (c > nMax)   nMax = c;
    return nMax;
}

void PrintData(int a, int b, int c, int max)
{
    printf("%d, %d, %d 중 가장 큰 수는 %d 입니다.\n", a, b, c, max);
}

int main(void)
{
    int aList[3] = {0};
    int nMax = -9999, i = 0;

    // 입력
    for (i = 0; i < 3; ++i)
        aList[i] = GetData();

    // 최대값 계산
    nMax = GetMax(aList[0], aList[1], aList[2]);

    // 출력
    PrintData(aList[0], aList[1], aList[2], nMax);
    return 0;
}