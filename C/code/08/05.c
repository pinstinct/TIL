#include <stdio.h>

/*
사용자로부터 문자열을 입력받은 후 문자열의 길이를 출력하는 프로그램을 작성합니다.
단, 입력되는 문자열이 한글이라고 가정하고 한글 문자의 개수를 출력해야 합니다.
사용자가 영문이나 숫자를 입력하는 문제는 고려할 필요가 없으며 무조건 한글만 입력한다고 가정합니다.
그리고 글자 사이의 공백이나 탭 같은 화이트스페이스는 없는 것으로 합니다.
*/
int main(void)
{
    char szData[] = {0};
    int nLength = 0;

    gets(szData);

    while (szData[nLength] != '\0')
        nLength++;

    printf("%d\n", nLength / 3);
    return 0;
}