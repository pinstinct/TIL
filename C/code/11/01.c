#include <stdio.h>

/* 매개변수로 char*형 자료를 받아서 문자열의 길이를 계산해 반환하는 함수 */
int GetLength(char* str)
{
    int nLength = 0;
    while (str[nLength] != '\0')
        nLength++;
    return nLength;
}

int main(int argc, char* argv[])
{
    printf("문자열의 길이는 %d 입니다.", GetLength("hello"));
    return 0;
}