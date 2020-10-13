#include <stdio.h>

/*
메모리 주소 두 개를 매개변수로 받아 문자열을 복사(deep copy)하는 MyStrcpy() 함수를 작성합니다.
*/
int MyStrcpy(char* pszDst, int nDstSize, char* pszSrc)
{
    int i = 0, nLenSrc = 0;

    nLenSrc = strlen(pszSrc);
    if (nLenSrc + 1 > nDstSize)
        return nDstSize - (nLenSrc + 1);

    while (pszSrc[i] != NULL)
    {
        pszDst[i] = pszSrc[i];
        ++i;
    }
    pszDst[i] = '\0';  // 문자열의 끝에 반드시 '\0'을 넣어준다.
    return nLenSrc;
}

int main(int argc, char* argv[])
{
    char szBufferSrc[12] = {"TestString"};
    char szBufferDst[12] = {0};

    MyStrcpy(szBufferDst, sizeof(szBufferDst), szBufferSrc);
    puts(szBufferDst);
    return 0;
}
