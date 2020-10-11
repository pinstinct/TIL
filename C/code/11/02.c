#include <stdio.h>
#include <stdlib.h>

/* 논리적 오류 두 가지를 찾고 수정하세요. */
int main(void)
{
    char szBuffer[12] = {"HelloWorld"};
    char *pszData = NULL;

    pszData = (char*)malloc(sizeof(char) * 12);
    // pszData = szBuffer;
    memcpy(pszData, szBuffer, sizeof(szBuffer));
    puts(pszData);
    free(pszData);  // 추가
    return 0;
}
