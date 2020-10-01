# 기본 제어문

제어문은 프로그램의 흐름(연산이 진행되는 순서)을 변경하는 구문입니다.

## `if` 문

`if`문은 다른 말로 분기문(branching statement)이라고 합니다. `if`문은 가장 기본적인 제어문이며 사용빈도도 가장 높습니다.

### 1. 기본구조

다음 예제는 `if`문의 필요성을 보인 가장 전형적인 사례인데, 기본적으로 `if`문은 조건을 만족하는 경우 어떤 **연산을 추가**로 더 수행하려는 의도를 전제한 구문으로 볼 수 있습니다.

```c
#include <stdio.h>

int main(void)
{
    int nAge = 0;
    printf("나이를 입력하세요. : ");
    scanf("%d", &nAge);

    if (nAge >= 20)
        printf("당신의 나이는 %d세 입니다.\n", nAge);

    puts("End");
    return 0;
}
```
한 가지 주의할 점은 조건식을 묶고 있는 괄호 끝에 세미콜론이 없다는 점입니다.

### 2. 제어문과 스코프

조건식을 만족할 때 수행할 구문이 여러 개면, 반드시 '스코프(정확히는 블록 스코프)'로 묶어야 합니다. 그렇지 않으면 조건식 이후 첫 번째 구문만 `if`문으로 판단합니다.

```c
#include <stdio.h>

int main(void)
{
    int nAge = 0;
    printf("나이를 입력하세요. : ");
    scanf("%d", &nAge);

    if (nAge >= 20)
    {
        printf("처리 전, 당신의 나이는 %d세 입니다.\n", nAge);
        nAge = 20;
    }

    printf("당신의 나이는 %d세 입니다.\n", nAge);
    return 0;
}
```
C 언어에서는
- 괄호로 여러 항을 묶어 한 항으로 만들고
- 블록 스코프로 여러 구문을 묶어 한 구문으로 만들 수 있습니다.

[실습문제](../code/06/01.c)

[실습문제](../code/06/02.c)

## `if else` 문

`if`문이 조건을 만족하는 경우만 처리하는 제어문인 반면, `if else`문은 조건을 만족하는 경우와 그렇지 않은 경우 모두를 처리할 수 있는 제어문입니다.

### 1. 기본구조

`else`문의 오른쪽에는 조건식이 없습니다.

```c
#include <stdio.h>

int main(void)
{
    int nInput = 0, nSelect = 0;
    scanf("%d", &nInput);

    // nSelect = nInput <= 10 ? 10 : 20;
    if (nInput <= 10)
        nSelect = 10;
    else
        nSelect = 20;

    printf("%d\n", nSelect);
    return 0;
}
```

### 2. 중첩된 제어문

제어문을 중첩하면(세분화를 거듭하면) 훨씬 다양한 경우를 다룰 수 있습니다. 이는 2분할 검색 알고리즘의 원리와 상통합니다. 다음 예제는 이러한 2분할 방식을 이용한 학점계산 프로그램입니다. 이 프로그램의 중요한 특징은 **중간정도에 해당하는 점수를 기준으로 1차 분류**하고 이어서 같은 방법으로 세분화했다는 점입니다.

```c
#include <stdio.h>

int main(void)
{
    int nInput = 0;
    char ch = 'A';

    printf("점수를 입력하세요: ");
    scanf("%d", &nInput);

    // 1차 분류: 전체 경우 중 중간정도의 값으로 분류
    if (nInput >= 80)
    {
        // 2차 상세 분류 A~B
        if (nInput >= 90) ch = 'A';
        else ch = 'B';
    }
    else
    {
        // 2차 상세 분류 C~F
        if (nInput >= 70) ch = 'C';
        else
        {
            // 3차 분류 D~F
            ch = 'D';
            if (nInput < 60) ch =  'F';
        }
    }
    printf("%c\n", ch);
    return 0;
}
```
"조건에 의한 분류와 선택"은 매우 중요합니다. 사실 프로그램이라는 것이 조건에 따른 처리를 기술한 문서라고 할 수 있기 때문입니다. 따라서 프로그래머는 **발생 가능한 경우의 수를 나열한 후, 어떤 조건과 방법으로 그중 하나를 정확히 선택**할 수 있는지 기술할 수 있어야 합니다.

#### 프로그래밍 기본요소: 분류와 선택

```c
#include <stdio.h>

/* 나이에 따른 분류 및 요금계산
버스의 기본요금을 1,000원이라고 가정하고,
다음과 같은 연령별 분류에 따라서 별도의 할인율을 적용하여 최종요금을 계산하는 프로그램을 작성합니다.

0~3세   할인율 100%
4~13세  할인율 50%
14~19세 할인율 25%
20세이상 할인율 0%
*/
int main(void)
{
    int nAge = 0, fee = 1000;
    double rate = 0.0;

    printf("나이를 입력하세요. : ");
    scanf("%d", &nAge);

    if (nAge < 14)
    {
        if (nAge < 4)   rate = 0.0;
        else            rate = 0.5;
    }
    else
    {
        if (nAge < 20)  rate = 0.25;
        else            rate = 1.0;
    }

    printf("최종요금: %d원", (int)(fee * rate));
    return 0;
}
```

### 3. 식별자 검색순위 (스코프의 중첩)

블록 스코프는 여러 구문을 한 덩어리로 묶어주는 역할과 범위를 제한하는 역할을 합니다. 보통 변수의 통용범위는 그 변수를 선언한 블록 스코프로 제한됩니다. 그리고 스코프를 벗어난 변수는 사라집니다. 왜냐하면 그 변수들은 기본적으로 스코프에 속한 '지역(local)변수'이면서 동시에 '자동(auto)변수'기 때문입니다. 핵심만 요약하면 가장 최근에 형성된 스코프가 우선하며, 스코프가 닫히면 그 내부에 선언된 변수는 사라진다는 말로 요약할 수 있습니다.

## 다중 `if` 문

2분할에 의한 단계별 분류가 '피라미드'라면 다중 `if`문은 '계단'이라 할 수 있습니다. 첫 번째에 가장 높은 기준을 이어서 그다음 높은 수준의 기준을 순차적으로 적용할 수 있기 때문입니다.

위의 금액 계산문제도 다중 `if`문으로 구현해 볼 수 있습니다. 다만, 둘 중 어느 것이 효율적인가에 대해 고민해봐야 합니다. **2분할에 의한 단계별 분류 방식**이 다중 `if`문을 이용한 단계별 분류 방식보다 우수합니다. 특히 고려해야 할 경우의 수가 늘어날수록 성능차이는 더 벌어집니다. 이는 '2분 검색(binary search)'과 '순차 검색(sequential search)'의 차이와 같습니다. 물론 2분 검색을 하기 위해서는 규칙에 맞게 정보가 정렬된 구조여야 합니다.

#### 프로그래밍 기본요소: 분류와 선택

```c
#include <stdio.h>

/* 단계별 분류에 따른 버스요금 계산
버스의 기본요금을 1,000원이라고 가정하고,
다음과 같은 연령별 분류에 따라서 별도의 할인율을 적용하여 최종요금을 계산하는 프로그램을 작성합니다.

0~3세   할인율 100%
4~13세  할인율 50%
14~19세 할인율 25%
20세이상 할인율 0%
65세이상 할인율 100%
*/
int main(void)
{
    int nAge = 0, fee = 1000;
    double rate = 0.0;

    printf("나이를 입력하세요. : ");
    scanf("%d", &nAge);

    if (nAge >= 65)         rate = 0.0;
    else if (nAge >= 20)    rate = 1.0;
    else if (nAge >= 14)    rate = 0.75;
    else if (nAge >= 4)     rate = 0.5;
    else                    rate = 0.0;

    printf("최종요금: %d원", (int)(fee * rate));
    return 0;
}
```
단계별로 분류하므로 나이가 많은 경우부터 처리하거나 반대로 나이가 어린 경우에서 큰 경우로 처리하는 것이 좋습니다.

## `switch-case` 문

```c
switch(변수 혹인 식)
{
    case 정수1:
        구문;
        break;
    case 정수2:
        구문;
        break;
    ...
    default:
        구문;
}
```
정보를 '분류'하는데 사용하는 제어문입니다. 그런데 switch-case문은 기존 if문과 달리 조건식을 단계별 혹은 중첩한 경우를 선택하지 않고 **단 한 번의 연산(혹은 변수)으로 특정한 경우 하나를 선택**한다는 것입니다.

```c
#include <stdio.h>

int main(void)
{
    char cOperator = 0;  // 정수형식인 `char`형
    int x = 0, y = 0, nResult = 0;

    scanf("%d%c%d", &x, &cOperator, &y);

    switch (cOperator)
    {
        case '+':
            nResult = x + y;
            break;
        case '-':
            nResult = x - y;
            break;
        case '*':
            nResult = x * y;
            break;
        case '/':
            nResult = x / y;
            break;
        default:
            puts("ERROR: 알 수 없는 산술 연산입니다.");
    }
    printf("Result: %d\n", nResult);
    return 0;
}
```
`case`에 대응할 수 있는 값이 **반드시 정수형식**으로 명시돼야 합니다. 각 `case`에 대응하는 값과 `switch`문에 기술한 값을 비교하는 상등연산(`==`)을 수행하기 때문입니다. 정수와 실수 혹은 실수와 실수간의 상등연산은 **부동소수점 오차**로 인한 문제가 발생할 수 있기 때문에 문법상 허용하지 않습니다.

`case`문 끝에 `;`이 아니라 `:`이 기술됩니다. C 언어에서는 '레이블(lable)'이 존재합니다. 그 자체가 연산식은 아니고, **코드의 위치**를 기술하는 것입니다.

`break`문은 연산을 즉시 멈추고 자신이 속한 스코프를 벗어나도록 흐름을 변경하는 제어문입니다.

## `goto` 문

특정 위치로 프로그램의 흐름을 '즉시' 변경합니다. `goto`문은 사용자가 레이블(lable)로 명시한 위치면 어디든 이동할 수 있습니다. 따라서 아무 제한 없이 코드의 흐름을 변경할 수 있습니다.

이것은 장점처럼 보이지만, 사실은 매우 심각한 단점입니다. 코드의 흐름을 뒤죽박죽으로 만들어서 논리적으로 심각한 결함이 있음에도 불구하고 해결하기 어려운 상태가 되도록 할 가능성이 높기 때문입니다. 그러므로 `goto`문은 사용하지 않는 것이 바람직합니다.