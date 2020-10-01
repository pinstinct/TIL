# 반복문

반복문은 일정구간의 코드를 연속적으로 반복해 실행하는 제어문입니다. 반복문에서 가장 중요한 것이 바로 반복횟수입니다. 그리고 더 중요한 점은 반복을 멈추기 위한 조건식입니다.

## `while` - 조건 기반 반복문

내부 구문이 끝나면 그 다음으로 그냥 넘어가는 것이 아니라 다시 구문의 처음으로 돌아가 조건식을 확인합니다. 그리고 조건이 참이면 계속해서 구문을 실행합니다.

### 1. 기본구조 조건에 의한 제어

#### 프로그래밍 기본요소: 반복

```c
#include <stdio.h>

int main(void)
{
    char ch = 0;

    while ((ch = getchar()) != '\n')
    {
        putchar(ch);
    }
    return 0;
}
```

[실습문제](../code/07/01.c)

### 2. 무한루프

반복문에서 가장 신경 써야 할 사항은 반복을 멈추기 위한 조건입니다. 그리고 그 조건에 영향을 줄 수 있는 연산이 반복문 내부에 포함되어야 한다는 것입니다.

### 3. 반복문 내부에 선언한 자동변수

반복문 내부에 변수를 선언하는 것은 바람직하지 않습니다.

```c
#include <stdio.h>

int main(void)
{
    char ch = 0;
    int nIndex = 0;

    while ((ch = getchar()) != '\n')
    {
        printf("%02d\t%c\n", nIndex, ch);
        ++nIndex;
    }
    return 0;
}
```
위의 예제는 정상적인 코드입니다. 이제 잘못된 코드로 변경하겠습니다.

```c
#include <stdio.h>

int main(void)
{
    char ch = 0;

    while ((ch = getchar()) != '\n')
    {
        int nIndex = 0;
        printf("%02d\t%c\n", nIndex, ch);
        ++nIndex;
    }
    return 0;
}
```
이처럼 반복문 내부에 선언 및 정의한 변수는 논리적 오류를 야기할 가능성도 높고, 무엇보다 불필요한 생성과 소멸을 반복하는 효율상의 문제도 있습니다.

### 4. 반복문의 중첩

`while`문 내부에 또 다른 `while`문을 중첩할 수 있습니다.

```c
while (조건식)  // 바깥쪽 반복문
{
    while (조건식)  // 안쪽 반복문
    {
        ...
    }
}
```

다음 예제를 실습할 때 가장 자주 발견되는 실수(논리오류)는 안쪽 반복문의 계수기 초기화 코드인 `j = 1`을 빼먹는 일입니다.
```c
#include <stdio.h>

int main(void)
{
    int i = 2, j = 1;
    while (i <= 9)
    {
        j = 1;  // 빼먹는 실수를 자주하므로 주의
        while (j <= 9)
        {
            printf("%d * %d = %d\n", i, j, i * j);
            ++j;
        }
        putchar('\n');
        ++i;
    }
    return 0;
}
```

[실습문제](../code/07/02.c)

## `for` - 계수 기반 반복문

`for`문과 `while`문은 반복문이라는 점에서 같지만, `while`문은 **조건에 기반**을 둔 측면이 강하고 `for`문은 **계수에 기반**을 둔 측면이 강합니다.

```c
#include <stdio.h>

int main(void)
{
    int i = 0;

    // 계수기 초기화; 조건식; 계수기 증가
    for (i = 0; i < 5; ++i)
    {
        printf("%dth\n", i);
    }
    return 0;
}
```

[실습문제](../code/07/03.c)

[실습문제](../code/07/04.c)

### 1. `while`문과 비교

```c
#include <stdio.h>

int main(void)
{
    int i = 0, j = 0;
    for (i = 0; i < 5; ++i)
    {
        for (j = 0; j < 5; ++j)
            printf("*\t");
        putchar('\n');
    }
    return 0;
}
```
인덱스의 시작이 0에서 출발하므로 **zero-based index**입니다. 그리고 '*'를 오른쪽에서 이어 붙여 출력하는 동안 '열(column)'의 인덱스 `j`는 증가합니다. 마찬가지로 '행(row)'의 인덱스인 `i`는 위에서 아래쪽으로 개행하면서 증가합니다.

### 2. '*'를 이용한 도형출력 실습

[실습문제](../code/07/05.c)

[실습문제](../code/07/06.c)

[실습문제](../code/07/07.c)

## `do while` 문

반복대상 단위코드를 조건과 상관없이 일단 한 번은 실행한 후, 조건을 비교합니다. 그리고 문법적으로 특이한 것은 조건식 괄호 뒤에 세미콜론(`;`)이 붙는다는 점입니다.

```c
#include <stdio.h>

int main(void)
{
    char ch = 0;
    do
    {
        ch = getchar();  // 일단 한 번은 무조건 실행
        putchar(ch);
    } while (ch != '\n');
    return 0;
}
```
이와 같은 형식의 코드를 적용하기에 가장 적절한 경우가 무엇인지를 생각해봐야 합니다. 사용자가 유효범위 값을 입력하지 않았다면 다시 입력하는 코드가 필요할 때 `do while`문을 활용하는 것도 좋은 선택입니다.

## `break`와 `continue`

`break`문은 `switch-case`문이나 반복문(`while`, `for`, `do while`)에서 사용되어 프로그램의 흐름 내부를 벗어나게 하는 제어문입니다. 그리고 `continue`문은 반복문 내부에만 사용할 수 있는 구문이며, 수행 즉시 나머지 구문들을 생략하고 다시 조건식을 비교하는 제어문입니다.

이 두 제어문이 사용되는 가장 흔한 이유는 반복문 내부에서 수행한 어떤 연산에서 예외(혹은 문제)가 발생했을 때 이에 대응하기 위함입니다.

```c
#include <stdio.h>

int main(void)
{
    int i = 0;
    for (i = 0; i < 10; ++i)
    {
        if (i > 4)
            break;
        printf("%dth\n", i);
    }
    printf("END: i == %d\n", i);  // END: i == 5
    return 0;
}
```
코드 일부가 생략된다는 점에서 `continue`문도 동일합니다. 하지만 반복문을 벗어나지는 않는다는 점에서 다릅니다. 아래는 위의 예제와 모든 것이 똑같은데, 단지 `break`문이 `continue`문으로 바뀌었을 뿐입니다. 그러나 결과는 다릅니다.

```c
#include <stdio.h>

int main(void)
{
    int i = 0;
    for (i = 0; i < 10; ++i)
    {
        if (i > 4)
            continue;
        printf("%dth\n", i);
    }
    printf("END: i == %d\n", i);  // END: i == 10
    return 0;
}
```
`continue`문이 수행됨으로 인해 반복대상 코드인 `printf("%dth\n", i);` 행은 실행하지 않았지만, 반복 수행식과 조건식은 계속 수행했고 전체 반복횟수도 달라지지 않습니다. **`break`문은 반복을 끝내자는 것이고 `continue`문은 일부 코드의 생략을 감수하고서도 계속 반복하자는 것**입니다.

그리고 '중첩된 반복문'에서 `break`문이나 `continue`문을 실행하면 구문이 속한 반복문에만 적용됩니다. 예를 들어, 안쪽 반복문 내부에서 `break`문을 실행하면 안쪽 반복문만 탈출하고 바깥쪽 반복문은 여전히 유효한 상태가 됩니다.

## 연습문제

[문제 01](../code/07/08.c)

[문제 02](../code/07/09.c)

[문제 03](../code/07/09.c)