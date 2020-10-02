#include <stdio.h>

/* 요소의 값을 교환하는 방식으로 배열에서 최소값 구하기
최소값이 저장되는 변수는 별도로 선언하지 않고 배열의 0번 요소(aList[0])에 저장합니다.
그러나 1~4번 요소들을 각각 비교하여 작은 값을 무조건 대입하는 것이 아니라 교환합니다.
따라서 배열 요소 중 일부 값이 유실되는 일이 없어야 합니다.
*/
int main(void)
{
    int aList[5] = {30, 40, 10, 50, 20};
    int i = 0, nTmp = 0;

    // 여기에 들어갈 코드를 작성합니다.
    for (i = 1; i < 5; ++i)
    {
        if (aList[0] > aList[i])
        {
            nTmp = aList[0];
            aList[0] = aList[i];
            aList[i] = nTmp;
        }
    }

    // 이하 코드는 수정하지 않습니다.
    for (i = 0; i < 5; ++i)
        printf("%d\t", aList[i]);
    putchar('\n');

    printf("MIN: %d\n", aList[0]);
    return 0;
}
