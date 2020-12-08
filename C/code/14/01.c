#include <stdio.h>

/*
표준입력장치(stdin)에서 문자열을 입력받은 후, 표준출력장치(stdout)로 출력하는 프로그램을 작성하세요.
단, 반드시 fgets()와 fputs() 함수를 사용하세요.
*/
void main()
{
    printf("문자열을 입력하세요.\n");
    char szBuffer[512] = {0};
    fgets(szBuffer, sizeof(szBuffer), stdin);
    fputs(szBuffer, stdout);
}