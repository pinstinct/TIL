#include <stdio.h>

/*
요소의 자료형이 int형이고 길이가 5인 배열을 선언한 후, 사용자가 5개의 정수로 초기화합니다.
그 중에서 가장 큰 수와 가장 작은 수를 출력하는 프로그램일 작성합니다.
*/
int main(void)
{
    int aList[5] = {0};
    int i, max, min;

    for (i = 0; i < 5; i++)
        scanf("%d", &aList[i]);

    max = aList[0];
    min = aList[0];
    for (i = 1; i < 5; i++)
    {
        if (aList[i] > max)     max = aList[i];
        if (aList[i] < min)     min = aList[i];
    }

    printf("MIN: %d, MAX: %d\n", min, max);
    return 0;
}