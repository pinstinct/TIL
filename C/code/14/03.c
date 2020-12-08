#include <stdio.h>

/*
현재 경로에서 'TestFile.txt' 테스트 파일을 연 후, 
원본 파일에서 행 단위로 문자열을 읽어 들여 대상 파일에 복사하는 프로그램을 작성하세요.
*/
void main()
{
    FILE *orgFp = fopen("TestFile.txt", "r");
    FILE *dstFp = fopen("DstFile.txt", "w");
    char szBuffer[512] = {0};

    if (orgFp == NULL || dstFp == NULL)
        return;

    while (fgets(szBuffer, sizeof(szBuffer), orgFp))
        fputs(szBuffer, dstFp);
    
    fclose(orgFp);
    fclose(dstFp);
}