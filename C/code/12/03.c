#include <stdio.h>

/*
매개변수로 char*의 배열이름과 요소의 개수를 인수로 받아
오름차순으로 문자열을 정리하는 SortString( ) 함수를 작성하세요.
다음과 같은 main( ) 함수의 코드에 대한 출력 예를 참고하여 작성합니다
*/
int SortString(char** srcList, int lenList)
{
    char* nTmp;
    for (int i = 0; i < lenList; i++)
        for (int j = i + 1; j < lenList; j++)
            if (strcmp(srcList[i], srcList[j]) > 0)
            {
                nTmp = srcList[i];
                srcList[i] = srcList[j];
                srcList[j] = nTmp;
            }
    return 0;
}

int main(void)
{
    char* aList[5] = {
        "정형돈",
        "노홍철",
        "하하",
        "유재석",
        "박명수"
    };
    int i = 0;

    SortString(aList, 5);

    for (i = 0; i < 5; i++)
        puts(aList[i]);

    return 0;
}
