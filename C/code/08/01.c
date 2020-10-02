#include <stdio.h>

/* 배열에서 최대값 구하기
추가로 새로운 변수를 선언하지 않고, 아래 코드를 완성합니다.
*/
int main(void)
{
    int aList[5] = {30, 40, 10, 50, 20};
    int i = 0;

    // 여기에 들어갈 코드를 작성합니다.
    for (i = 1; i < 5; ++i)
        if (aList[i] > aList[0])
            aList[0] = aList[i];

    // 이하 코드는 수정하지 않습니다.
    for (i = 0; i < 5; ++i)
        printf("%d\t", aList[i]);
    putchar('\n');

    printf("MAX: %d\n", aList[0]);
    return 0;
}
