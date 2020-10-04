#include <stdio.h>

/* 사용자가 입력한 값에서 최대값 구하기와 코드 분할 */
int main(void)
{
    int aList[3] = {0};
    int nMax = -9999, i = 0;

    // 입력
    for (i = 0; i < 3; ++i)
    {
        printf("정수를 입력하세요. : ");
        scanf("%d", &aList[i]);
    }

    // 최대값 계산
    nMax = aList[0];
    for (i = 0; i < 3; ++i)
        if (aList[i] > nMax) nMax = aList[i];

    // 출력
    printf("%d, %d, %d 중 가장 큰 수는 %d 입니다.\n", aList[0], aList[1], aList[2], nMax);
    return 0;
}