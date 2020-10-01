#include <stdio.h>

/* 구구단에서 한 단만 출력하기
사용자로부터 2~9 사이의 정수를 입력받아 해당 정수의 구구단을 출력하는 프로그램을 작성합니다.
만약 사용자가 입력한 값이 2보다 작거나 9보다 크면 "ERROR"라고 출력합니다.
*/
int main(void)
{
    int nInput = 0, i = 1;
    printf("정수를 입력하세요. : ");
    scanf("%d", &nInput);

    if (nInput > 9 || nInput < 2)
        printf("ERROR\n");
    else
    {
        while (i < 10)
        {
            printf("%d * %d = %d\n", nInput, i, nInput * i);
            i++;
        }
    }
    return 0;
}