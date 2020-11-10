#include <stdio.h>
#include <time.h>

/*
오늘을 기준으로 10일 후와 100일 후의 날짜를 계산하여 출력하는 프로그램을 작성하세요.
*/
void main(void)
{
    struct tm *ptime = {0};
    time_t t = 0;

    t = time(NULL);
    t += 10 * 24 * 60 * 60;  // 10일 후
    ptime = localtime(&t);
    printf("%04d-%02d-%02d\n",
        ptime->tm_year + 1900,
        ptime->tm_mon + 1,
        ptime->tm_mday);

    t = time(NULL);
    t += 100 * 24 * 60 * 60;  // 100일 후
    ptime = localtime(&t);
    printf("%04d-%02d-%02d\n",
        ptime->tm_year + 1900,
        ptime->tm_mon + 1,
        ptime->tm_mday);
}
