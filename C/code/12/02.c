#include <stdio.h>
#include <string.h>

/*
기능적으로는 strstr( ) 함수와 같지만,
반환하는 자료형은 char*가 아니라 대상 메모리에 대한 인덱스를 정수형으로 반환합니다.
만일 찾는 문자열이 없다면 -1을 반환하는 함수로 정의합니다.
*/
int MyStrstr(const char *str, const char *strSearch)
{
    int idx = 0;
    while (str[idx] != NULL)
    {
        if (str[idx] == strSearch[0])
        {
            if (strncmp(str + idx, strSearch, strlen(strSearch)) == 0)
                return idx;
        }
        idx++;
    }
    return -1;
}

int main(void)
{
    char szTest[101] = { 0 };
    char szSearch[101] = { 0 };
    int iResult;

    printf("검색대상 문자열 : ");
    gets(szTest);
    printf("검색할 문자열 : ");
    gets(szSearch);

    iResult = MyStrstr(szTest, szSearch);

    if (iResult == -1)
        printf("대상 문자열에 찾는 문자열이 없습니다.\n");
    else
        printf("Index : %d\n", iResult);

    return 0;
}
