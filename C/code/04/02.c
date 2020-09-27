#include <stdio.h>

/* 초를 '시:분:초'로 변환하는 프로그램
시, 분, 초는 모두 두 자리 정수로 표시되어야 하며,
한 자리 숫자인 경우 앞에 0을 붙여 출력해야 합니다.
*/
int main(void)
{
    int input = 0;
    scanf("%d", &input);
    printf("%d초는 %02d시간 %02d분 %02d초 입니다.\n",
        input, input/3600, input%3600/60, input%60);
    return 0;
}