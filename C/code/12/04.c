#include <stdio.h>

/*
int형 5행 4열 배열에서 각 요소의 총합을 계산하여 반환하는 GetTotal( ) 함수를 작성하세요.
*/
int GetTotal(int (*aList)[4])
{
    int total = 0;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 4; j++)
            total += aList[i][j];
    }
    return total;
}

void main(void)
{
    int aList[5][4] = {
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11,
        12, 13, 14, 15,
        16, 17, 18, 19
    };
    printf("각 요소의 총합: %d\n", GetTotal(aList));
}
