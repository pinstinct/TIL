#include <stdio.h>

/* goto문을 제거하고 반복문을 이용해서 같은 결과를 얻을 수 있도록 프로그램을 변경합니다.
int nInput;

INPUT:
    printf("Input number : ");
    scanf("%d", &nInput);

    if (nInput < 0 || nInput > 10)
        goto INPUT;

    puts("End");
*/
int main(void)
{
    int nInput;

    do
    {
        printf("Input number : ");
        scanf("%d", &nInput);
    } while (nInput < 0 || nInput > 10);

    puts("End");
    return 0;
}