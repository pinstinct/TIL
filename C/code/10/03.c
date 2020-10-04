#include <stdio.h>

/* 다음 코드를 작성하고 11을 입력한다면 어떤 결과가 출력되는지 쓰세요.*/

int nInput = 100;

int TestFunc(void)
{
    printf("TestFunc(): %d\n", nInput);
}

int main(void)
{
    int nInput = 0;
    scanf("%d", &nInput);

    if (nInput > 10)
    {
        int nInput = 20;
        printf("%d\n", nInput);
        TestFunc();

        if (nInput >= 100)
        {
            printf("%d\n", nInput);
        }
    }
    printf("%d\n", nInput);
    return 0;
}

/* 출력:
11
20
TestFunc(): 100
11
*/