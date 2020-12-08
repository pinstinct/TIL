#include <stdio.h>

/*
현재 경로에서 'TestFile.txt' 텍스트 파일을 연 후, 
사용자가 입력한 문자열을 뒤에 이어서 추가한 후 다시 저장하는 프로그램을 작성하세요.
*/
int main(void)
{
    FILE *fp = NULL;
    char szBuffer[128] = {0};
    
    fp = fopen("TestFile.txt", "a+");
    printf("문자열을 입력하세요.\n");
    fgets(szBuffer, sizeof(szBuffer), stdin);
    fputs(szBuffer, fp);
    fclose(fp);

    return 0;
}