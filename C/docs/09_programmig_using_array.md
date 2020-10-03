# 배열을 활용한 프로그래밍 기법

## 배열 요소의 정렬

정렬 알고리즘을 공부할 때 가장 기본이 되는 두 가지는 **선택정렬(selection sort)과 버블정렬(bubble sort)**입니다. 두 알고리즘 모두 반복문 두 개를 중첩하는 것만으로 구현할 수 있으며, 다른 정렬 알고리즘보다 비교적 구조가 단순합니다.

### 1. 선택정렬로 알려진 버블정렬

배열 전체를 오름차순 정렬(ascending sort)하는 가장 쉬운 방법은 모두 정렬될 때까지 최소값을 구하는 것입니다. 이 방법이 일부 선택정렬로 알려졌으나 정확히 따지면 버블정렬입니다. 왜냐하면 각 항을 비교하여 값이 작은 것이 확인될 때마다 **즉시 교환**했기 때문입니다.

실제 선택정렬은 각 항을 비교하긴 하지만 더 작은 값이 발견되었을 때 즉시 두 항의 값을 교환하는 것이 아니라 더 작은 값이 저장된 배열의 인덱스를 따로 저장했다가 안쪽 반복문이 끝난 후, 단 한번만 두 항의 값을 교환하는 방식으로 구현합니다.

```c
#include <stdio.h>

int main(void)
{
    int aList[5] = {30, 40, 10, 50, 20};
    int i, j, nTmp = 0;

    for (i = 0; i < 4; ++i)
        for (j = i + 1; j < 5; ++j)
            if (aList[i] > aList[j])
            {
                nTmp = aList[i];
                aList[i] = aList[j];
                aList[j] = nTmp;
            }

    for (i = 0; i < 5; ++i)
        printf("%d\t", aList[i]);

    putchar('\n');
    return 0;
}
```

### 2. 버블정렬

버블정렬(bubble sort)은 서로 연접한 두 항을 계속해서 비교하는 방식으로 정렬합니다. 예를 들어, 0번째 항과 1번 항을 비교한 후에 이어서 1번 항과 2번 항을, 다시 2번 항과 3번 항을 비교합니다. 같은 방법으로 마지막 두 항을 비교한 후에 마지막 항의 정보(가장 큰 수)가 확정됩니다. 따라서 오름차순으로 정렬할 경우, 가장 큰 값을 먼저 결정하는 특징이 있습니다.

버블정렬은 앞서 설명한 '선택정렬로 알려진 버블정렬'과 효율이 같습니다.

```c
#include <stdio.h>

int main(void)
{
    int aList[5] = {30, 40, 10, 50, 20};
    int i, j, nTmp = 0;

    for (i = 4; i > 0; --i)
        for (j = 0; j < i; ++j)
            if (aList[j] > aList[j + 1])
            {
                nTmp = aList[j + 1];
                aList[j + 1] = aList[j];
                aList[j] = nTmp;
            }

    for (i = 0; i < 5; ++i)
        printf("%d\t", aList[i]);

    putchar('\n');
    return 0;
}
```
배열을 다룰 때는 항상 인덱스가 최소, 최대 경계를 벗어나는 일이 없는지 잘 생각해야 합니다.

### 3. 선택정렬

선택정렬(selection sort)의 기본 원리는 앞서 설명한 '선택정렬로 알려진 버블정렬'과 같습니다. 다른 점은 비교의 기준이 되는 왼쪽 요소(최소값이 저장된 요소)가 고정되는 것이 아니라 변경된다는 것입니다. 그리고 두 항을 비교한 후, 작은 값이 저장된 요소의 값이 아니라 배열의 '인덱스'를 따로 저장합니다. 그리고 안쪽 반복문이 끝나면 단 한번만 교환합니다.

선택정렬을 구현하려면 반드시 배열의 '인덱스'와 '요소의 값'을 분리해 생각하고 코드를 작성해야 합니다.

```c
#include <stdio.h>

int main(void)
{
    int aList[5] = {30, 40, 10, 50, 20};
    int i, j, nMinIndex = 0, nTmp = 0;

    for (i = 0; i < 4; ++i)
    {
        nMinIndex = i;
        for (j = i + 1; j < 5; ++j)
            if (aList[nMinIndex] > aList[j])    nMinIndex = j;
        if (nMinIndex != i)
        {
            nTmp = aList[i];
            aList[i] = aList[nMinIndex];
            aList[nMinIndex] = nTmp;
        }
    }

    for (i = 0; i < 5; ++i)
        printf("%d\t", aList[i]);
    putchar('\n');
    return 0;
}
```

## 배열과 교차의 구현

```c
/* 출력 예:
1       2       3       4       5
10      9       8       7       6
11      12      13      14      15
20      19      18      17      16
21      22      23      24      25
*/
```

한 번은 열의 인덱스 증가방향과 일치하다가 다음 한번은 정반대가 됩니다. 그리고 이 두 가지가 규칙적으로 교차하여 2차원 배열을 채우고 있습니다. 채우는 순서가 열의 인덱스가 증가 방향이면 '순방향 채우기'라고 부르고 반대로 열의 인덱스가 감소하는 순서로 채우면 '역방향 채우기'라고 부르겠습니다.

이 교차를 구현하는 방법은 크게 세 가지가 있습니다. 가장 흔하고 쉬운 방법은 2차원 배열에 대한 열의 인덱스를 증가시키거나 감소시켜서 채우는 방법입니다. 그리고 나머지 두 가지 방법은 배열의 순방향으로만 채우면서 0번 요소의 값을 직접 계산하는 방법과 '플래그 변수'를 이용한 방법입니다.

#### [프로그래밍 기본요소: 교차](../code/09/01.c)

```c
#include <stdio.h>

int main(void)
{
    int aList[5][5] = {0};
    int i, j, nCounter = 0;

    for (i = 0; i < 5; ++i)
    {
        if (i % 2 == 0)
            for (j = 0; j < 5; ++j)
                aList[i][j] = ++nCounter;

        else
            for (j = 0; j < 5; ++j)
                aList[i][4 - j] = ++nCounter;
    }

    for (i = 0; i < 5; ++i)
    {
        for (j = 0; j < 5; ++j)
            printf("%d\t", aList[i][j]);
        putchar('\n');
    }

    return 0;
}
```
행 인덱스인 `i`를 2로 나눈 나머지가 0인 경우는 모두 순방향으로 채워야하고, 1이면 모두 역방향으로 채워야 합니다. `aList[i][4 - j]` 코드처럼 역방향으로 채워지는 행 요소들의 열 인덱스는 최대 인덱스에서 0부터 1씩 증가하는 값으로 빼는 방식으로 계산할 수도 있습니다.

```c
#include <stdio.h>

int main(void)
{
    int aList[5][5] = {0};
    int i, j, nCounter = 0, nOffset = 1;

    for (i = 0; i < 5; ++i)
    {
        // 0번열 요소의 초기값을 결정
        if (i % 2 == 0)     nCounter = i * 5;
        else                nCounter = (i + 1) * 5 + 1;

        for (j = 0; j < 5; j++)
        {
            nCounter += nOffset;
            aList[i][j] = nCounter;
        }
        nOffset = -nOffset;
    }

    for (i = 0; i < 5; ++i)
    {
        for (j = 0; j < 5; ++j)
            printf("%d\t", aList[i][j]);
        putchar('\n');
    }
    return 0;
}

```
`nCounter += nOffset` 구문은 어떨 땐 1씩 증가하지만 어떨 땐 1씩 감소합니다.

드디어 교차의 세 번째 방법입니다. 세 가지 방법 중에서 가장 중요하게 생각하는 방법입니다. 이 세 번째 방법은 **플래그(flag)라는 개념을 적용해서 교차를 구현**합니다. 앞서 설명한 두 방법과 달리 순차 증가하는 인덱스 정보가 없어도 마치 토글스위치를 작동시키는 것처럼 작동합니다.

```c
#include <stdio.h>

int main(void)
{
    int aList[5][5] = {0};
    int i, j, nCounter = 0, nFlag = 1;

    for (i = 0; i < 5; ++i)
    {
        if (nFlag)
        {
            for (j = 0; j < 5; j++)
                aList[i][j] = ++nCounter;
            nFlag = 0;
        }
        else
        {
            for (j = 0; j < 5; ++j)
                aList[i][4 - j] = ++nCounter;
            nFlag = 1;
        }
    }


    for (i = 0; i < 5; ++i)
    {
        for (j = 0; j < 5; ++j)
            printf("%d\t", aList[i][j]);
        putchar('\n');
    }
    return 0;
}
```

## 달팽이 배열 채우기

```c
#include <stdio.h>

/* 출력 예:
1       2       3       4       5
16      17      18      19      6
15      24      25      20      7
14      23      22      21      8
13      12      11      10      9
*/
int main(void)
{
    int aList[5][5] = {0};
    int x = -1, y = 0, nCounter = 0;
    int i, j, nLength = 9, nDirection = 1;

    for (nLength = 9; nLength > 0; nLength -= 2)
    {
        for (i = 0; i < nLength; ++i)
        {
            if (i < nLength / 2 + 1)    x += nDirection;
            else                        y += nDirection;
            aList[y][x] = ++nCounter;
        }
        nDirection = -nDirection;
    }

    for (i = 0; i < 5; ++i)
    {
        for (j = 0; j < 5; ++j)
            printf("%d\t", aList[i][j]);
        putchar('\n');
    }
    return 0;
}
```
배열을 채울 때 안쪽 반복문의에서 채우는 요소의 개수가 9, 7, 5, 3, 1로 끝납니다. 따라서 `nLength` 변수가 의미하는 것은 '채워지는 요소의 개수'입니다. 그리고 행의 인덱스가 증감하고 이후로는 열의 인덱스가 증감합니다. 이를 나눈 근거가 `if`문의 조건식입니다.

## Lookup 배열

**선택이라는 개념을 구현하는데 배열을 사용**할 수도 있습니다. 다음 예제가 배열로 선택을 구현한 것입니다.

```c
#include <stdio.h>

int main(void)
{
    double aRate[10] = {
        0.0, 0.1, 0.25, // 1~3세 0%, 10%, 25%
        0.5, 0.5,       // 4~5세 50%
        0.6, 0.65,      // 6~7세 60%, 65%
        0.8, 0.82, 0.97 // 8~10세 80%, 82%, 97%
    };
    int nAge = 0, i = 0, nFee = 1000;

    printf("요금표\n");
    for (i = 1; i <= 10; ++i)
        printf("%d세 요금 :\t%d원\n", i, (int)(nFee * aRate[i - 1]));
    putchar('\n');

    printf("나이를 입력하세요. : ");
    scanf("%d", &nAge);
    if (nAge < 1)       nAge = 1;
    else if (nAge > 10) nAge = 10;

    printf("최종요금 : %d\n", (int)(nFee * aRate[nAge - 1]));
    putchar('\n');
    return 0;
}
```
배열을 이용해 경우의 수를 선택할 수 있음을 볼 수 있습니다. 만일 이 예제와 똑같은 기능을 수행하는 프로그램을 중첩된 `if else`문이나 다중 `if`문 혹은 `switch-case`문으로 구현했다면 경우의 수가 너무 많아져서 함수가 세로로 무척 길게 늘어났을 것이고 구조도 지금보다 복잡해질 것입니다.

이 예제의 경우, 배열 자체가 제어문을 대신했다 할 수 있습니다. 이처럼 **정보검색 기능을 제공할 목적으로 사용할 배열을 'Lookup 배열'**이라고 합니다. 이와 같은 방법을 알아두면 코드가 매우 간결해지는 것은 물론이고 복잡한 제어문을 사용한 프로그램보다 훨씬 효율이 좋은 프로그램일 작성할 수 있습니다.
