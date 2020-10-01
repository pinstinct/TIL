#include <stdio.h>

/* 5행 5열의 사각형 출력하기
while문을 두번 중첩하여 구현하며, 
안쪽 반복문에는 한 행(* * * * *)을 출력하는 코드가 들어가도록 하고,
바깥쪽 반복문에서는 각 행을 출력하는 코드가 다섯번 반복되도록 코드를 작성합니다.
*/
int main(void)
{
    int i = 0, j = 0;
    while (i < 5)
    {
        j = 0;
        while (j < 5)
        {
            printf("*\t");
            ++j;
        }
        putchar('\n');
        ++i;
    }
    return 0;
}