#include <stdio.h>

/*
문자열을 비교하는 함수를 작성합니다.
만일 같으면 0을 반환하고, 그렇지 않으면 1을 반환합니다.
기본적인 기능은 strcmp() 함수와 같습니다.
단, 영문 대/소문자를 구별하지 않고 비교합니다.
*/
int Mystrcmp(char* src, char* dst)
{
    int idx = 0;
    if (strlen(src) != strlen(dst))
        return 1;

    while (src[idx] != '\0')
    {
        if (tolower(src[idx]) != tolower(dst[idx]))
            return 1;
        idx++;
    }
    return 0;
}

void main(void)
{
    char* str1 = "Block";
    char* str2 = "BLOCK";

    if (Mystrcmp(str1, str2) == 0)
        printf("%s, %s 같습니다.\n", str1, str2);
    else
        printf("%s, %s 다릅니다.\n", str1, str2);
}
