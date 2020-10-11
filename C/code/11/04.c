#include <stdio.h>

/* 사용자로부터 입력받은 첫 번째 문자열을 동적 할당되 메모리에 저장한 후 화면에 출력하고,
두 번째로 입력받은 문자열을 첫 번째로 동적 할당된 메모리에 덧붙여 출력하는 프로그램을 작성합니다.
*/
int main(int argc, char* argv[])
{
    char *pList = NULL, *pNewList = NULL;
    pList = (char*)malloc(sizeof(char) * 12);
    gets(pList);
    puts(pList);

    pNewList = (char*)realloc(pList, sizeof(char) * 32);
    if (pList == NULL)
        free(pList);

    // 이전에 입력의 마지막 주소에 입력받음
    gets(pNewList + strlen(pNewList));
    puts(pNewList);

    free(pNewList);
    return 0;
}