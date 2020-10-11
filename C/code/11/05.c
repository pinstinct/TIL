#include <stdio.h>

/*
정수를 입력받고, 그 개수만큼 char*를 여러개 저장할 수 있는 메모리를 동적 할당합니다.
그리고 입력할 문자열의 최대 길이를 입력받고, 최대 길이의 문자열을 저장할 수 있는 크기의 메모를 동적할당하여
입력받은 문자열을 저장한 후 출력하는 프로그램을 작성합니다.
*/
int main(int argc, char* argv[])
{
    int strCount, strLength;
    printf("입력할 문자열의 개수: ");
    scanf("%d", &strCount);
    printf("입력할 문자열의 최대 길이: ");
    scanf("%d%*c", &strLength);  // 버퍼를 비워줘야 함

    char **ppstrList = NULL;
    ppstrList = (char**)malloc(sizeof(char*) * strCount);
    for (int i = 0; i < strCount; i++)
    {
        ppstrList[i] = (char*)malloc(sizeof(char) * strLength);
        printf("문자열을 입력: ");
        gets(ppstrList[i]);
    }

    for (int i = 0; i < strCount; i++)
    {
        puts(ppstrList[i]);
        free(ppstrList[i]);
    }
    free(ppstrList);
    return 0;
}
