#include <stdio.h>
#include <string.h>

/* strrev() 함수의 사용방법에 대해 찾아보고 이 함수와 동일한 기능을 수행할 수 있는 함수를 작성하세요.
*/
char* MyStrrev(char* str)
{
    int strLength = strlen(str);
    if (strLength == 0)
        return NULL;

    int strMiddle = strLength >> 1;
    for (int i = 0; i < strMiddle; i++)
    {
        char temp = str[i];
        str[i] = str[(strLength - 1) - i];
        str[(strLength - 1) - i] = temp;
    }
    return str;
}

int main(int argc, char* argv[])
{
    char myString[12] = "Hello";
    printf("문자열을 거꾸로 뒤집는 함수 실행 결과: %s\n", MyStrrev(myString));
    return 0;
}
