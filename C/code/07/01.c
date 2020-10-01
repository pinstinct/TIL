#include <stdio.h>

/* 사용자가 입력한 숫자만큼 '*' 출력하기
사용자로부터 1~9 범위의 정수를 입력받아 그 수만큼 '*'를 출력하는 프로그램일 작성합니다.
사용자 입력이 범위를 벗어났다면 1이나 9로 강제 보정합니다.
예를 들어 -1을 입력했다면 1로 12를 입력했다면 9로 보정한 후 출력합니다.
*/
int main(void)
{
    int nInput = 0;
    printf("숫자를 입력하세요. : ");
    scanf("%d", &nInput);

    if (nInput > 9)         nInput = 9;
    else if (nInput < 1)    nInput = 1;

    while (nInput)
    {
        putchar('*');
        nInput--;
    }
    putchar('\n');
    return 0;
}