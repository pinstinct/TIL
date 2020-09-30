#include <stdio.h>

/* if문을 이용한 최대값 구하기
사용자로부터 세 정수를 입력받아 그중 가장 큰 수를 출력하는 프로그램을 작성합니다.
*/
int main(void)
{
    int nInput = 0, nMax = 0;
    scanf("%d", &nMax);

    scanf("%d", &nInput);
    if (nInput > nMax)
        nMax = nInput;

    scanf("%d", &nInput);
    if (nInput > nMax)
        nMax = nInput;

    printf("MAX : %d", nMax);
    return 0;
}
