#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
난수를 구하는 함수를 사용하여 가위바위보 게임을 구현합니다.
0~2 범위의 숫자를 발생시켜서 0은 '가위', 1은 '바위', 2는 '보’라고 가정합니다.
게임 방식은 사용자로부 터 0~2 범위의 정수를 입력받은 후,
이에 대응하는 0~2 범위의 난수를 발생시켜 사용자가 입력한 정보와 비교하는 방식으로 게임을 진행합니다.
반드시 사용자, 컴퓨터가 선정한 것이 무엇이며 누가 승자인지 표시해야 합니다.
*/
void main(void)
{
    int user = 0, program = 0;
    char *p_ment[] = {"user win", "program win", "same"};
    printf("가위는 0, 바위는 1, 보는 2 중 하나를 선택하세요.: ");
    scanf("%d", &user);

    srand((unsigned)time(NULL));
    program = rand() % 3;

    printf("user: %d, program: %d, %s\n",
    user, program, p_ment[(user - program + 2) % 3]);
}
