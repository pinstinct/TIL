# 함수 응용

## 매개변수 전달 방법

A 함수 내부에서 B 함수를 호출하는 코드가 있다면, A는 호출자이고 B는 피호출자입니다. 호출/피호출 관계로 묶이는 것이 **바인딩(binding)**입니다. 그리고 두 함수가 서로 연결되는 인터페이스는 바로 매개변수와 반환자료입니다. 그리고 함수호출 과정에서 매개변수로 전달되는 정보가 무엇이냐에 따라 **매개변수 전달방법**이 달라집니다. 값이냐 주소냐에 따라 **Call by value**와 **Call by reference**로 나뉩니다.

### 1. Call by value

다음은 전형적인 Call by value 예제입니다.
```c
#include <stdio.h>

int Add(int a, int b)
{
    return a + b;
}

int main(int argc, char* argv[])
{
    printf("%d\n", Add(3, 4));
    return 0;
}
```

### 2. Call by reference

Call by reference의 핵심은 매개변수가 **포인터**라는 점입니다. 따라서 호출자는 반드시 메모리의 **주소를 인수**로 넘겨야 합니다. 그리고 피호출자 함수는 이 매개변수를 간접지정함으로써 포인터가 가리키는 대상에 접근할 수 있습니다.

```c
#include <stdio.h>

int Add(int *a, int *b)
{
    return *a + *b;
}

int main(int argc, char* argv[])
{
    int x = 3, y = 4;
    printf("%d\n", Add(&x, &y));
    return 0;
}
```
Call by reference의 가장 큰 장점은 **배열처럼 덩치가 큰 메모리를 매개변수로 전달할 수 있다**는 점입니다.

```c
#include <stdio.h>

void GetName(char *pszName, int nSize)
{
    printf("이름을 입력하세요. : ");
    gets_s(pszName, nSize);
}

int main(int argc, char* argv[])
{
    char szName[32] = {0};
    GetName(szName, sizeof(szName));
    printf("당신의 이름은 %s입니다.\n", szName);
    return 0;
}
```
매개변수가 포인터일 때 포인터가 가리키는 대상 **메모리의 크기**를 인수로 받는 것은 보안적으로나 설계적으로 매우 중요합니다. 포인터의 가장 큰 문제는 가리키는 대상의 실제 크기를 포인터 자체만으로는 알 수가 없다는 점입니다.

매개변수 `char *pszName` 대신 `char pszName[]`라고 써도 의미가 같습니다. 문법적으로 둘 다 포인터입니다.

```c
#include <stdio.h>

// 매개변수로 주소를 받는다.
void Swap(int *pLeft, int *pRight)
{
    // 주소가 가리키는 대상의 메모리의 값을 교환
    int nTmp = *pLeft;
    *pLeft = *pRight;
    *pRight = nTmp;
}

int main(int argc, char* argv[])
{
    int x = 10, y = 20;
    Swap(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}
```
위의 예제는 Call by reference가 필요한 가장 대표적인 상황을 설명하는 예제입니다. 반드시 이해하고 넘어가야합니다.

```c
#include <stdio.h>

// 매개변수로 전달된 문자열의 길이를 반환하는 함수
int GetLength(const char *pszParam)
{
    int nLength = 0;
    while (pszParam[nLength] != '\0')
        nLength++;

    return nLength;
}

int main(int argc, char* argv[])
{
    char *pszData = "Hello";
    printf("%d\n", GetLength("Hi"));
    printf("%d\n", GetLength(pszData));
    return 0;
}
```
`const`는 **형한정어(type qualifier)**이며 `char*`인 매개변수 `pszParam`을 통해 간접지정한 대상을 상수화한다는 의미입니다. 즉, 간접지정한 대상에서 정보를 읽을 수는 있지만 쓸 수는 없다는 뜻입니다. `const` 형한정어를 잘 활용하면 피호출자 함수가 의도하지 않게 혹은 실수로 호출자가 전달한 주소의 메모리에 쓰기 연산하는 일을 방지할 수 있습니다.

[실습문제](../code/12/01.c)

#### 잘못된 주소 전달

운영체제에 반환했거나 곧 사라질 메모리에 대한 주소를 반환하는 일은 없어야 합니다. 예를 들어 함수 내부에 선언된 자동변수의 주소를 반환하는 것입니다.

동적 할당된 메모리나 정적변수는 함수의 호출이나 반환과 아무런 관련이 없습니다. 동적 할당된 메모리는 `free()` 함수로 해제하기 전까지 유효하며 정적변수들은 프로그램이 끝나는 순간까지 유효합니다.

그러나 자동변수는 스택 영역을 사용하며, 스택은 스코프가 닫히면 그 내부에서 선언된 것들이 사실상 사라진다고 봐야 합니다. "사라졌다"가 아니라 "사라진다고 봐야한다"는 이유는 스택 메모리가 정말로 사라지거나 해제되는 것이 아니라 가용범위가 줄어드는 것(지정해제)에 불과하기 때문입니다.

## 스택 프레임 그리는 방법

자동변수는 스택 영역 메모리를 사용합니다. 자동변수는 `auto`로 선언된 변수를 말하는데 별도로 명시하지 않는 모든 지역변수는 모두 자동변수입니다. 함수의 매개변수 역시 자동변수이고 함수의 지역변수입니다.

스택은 선형 자료구조의 일종으로 정보를 층층이 쌓아 올린 구조입니다. 그리고 이 스택 영역은 시스템이 관리합니다. 따라서 개발자가 스택 메모리의 지정(할당이 아님)과 해제에 관여할 필요도 없으며 그래서도 안됩니다. 그러나 스택이 어떤 형식으로 관리되는지 구체적으로 알아야 하는데, 그 관리 형식을 스택 프레임(stack frame)이라 합니다.

#### 스택과 메모리의 주소는 반대방향으로 그린다

스택 왼쪽에는 함수 이름과 스코프의 시작 지점을 표시하고 오른쪽에는 식별자 이름을 기술합니다. 그림에서 스택은 위로 증가합니다. 그러나 메모리의 주소는 아래로 증가합니다. 따라서 **메모리의 주소가 증가했다는 것은 스택이 줄어들었음을 의미**하고 주소값이 작아졌다는 것은 스택의 증가를 의마한다고 생각할 수 있습니다.

#### 지역 변수는 선언된 순서대로 그린다

선언된 순서대로 그렸다는 말을 정확하게 표현하자면 "먼저 스택에 Push 했다"라고 합니다. Push는 스택에 정보를 넣는 것이고 반대로 빼내는 것은 Pop이라고 합니다.

#### 포인터 변수는 별도로 표시한다

포인터 변수는 간접지정 대상이 어디인지 포인터가 가리키는 지점을 표시해야 합니다. 그러나 `NULL`로 초기화한 경우에는 그냥 `NULL`이라고 쓰고 선을 그어 표시하지 않습니다.

#### 배열의 인덱스는 아래로 증가하게 그린다.

배열의 인덱스는 주소가 증가하는 방향으로 표시해야 합니다. 따라서 0번 요소가 스택의 상단에 표시되도록 그립니다. 그리고 배열의 이름은 '주소상수'이므로 그 자체가 스택에 Push 되지 않는다는 사실에 주의합니다.

#### 동적 할당된 메모리는 따로 표시한다

만일 **메모리를 동적 할당하거나, 정적 영역을 사용하는 변수가 등장한다면 이는 스택 영역이 아니므로 별도로 그려서 표시**해야 합니다. 한 가지 주의해야 할 사항은 반드시 동적 할당된 **메모리의 크기**를 기술하고 동적 할당된 메모리의 기준주소를 포인터 변수가 가리키도록 선을 그어 표시해야 합니다.

메모리를 해제하는 코드가 등장하면 동적 할당된 메모리를 삭제표시를 해둡니다. 만일 삭제표시 없이 스택 프레임이 모두 사라졌다면 이는 **메모리 누수**입니다.

#### 매개변수는 오른쪽부터 스택에 그리며 새 스코프는 기존 스택 위에 그린다.

`main()` 함수가 다른 사용자 정의 함수를 호출할 경우에는 **매개변수도 스택에 그려야 하는데 반드스 오른쪽 매개변수부터 먼저 Push** 하는 것으로 그립니다.

함수가 함수를 호출해 함수 몸체에 대한 스코프가 형성되면 스택에 가로선을 길게 그어 표시합니다. 피호출자 함수가 반환하면 함수의 몸체에 해당하는 스코프를 모두 닫아야 합니다. 그리고 피호출자 함수가 호출자에 반환하는 값도 별도로 표시합니다.

#### 스코프가 닫히면 그림에서 지운다

변수 이름이 중복될 경우 식별자를 검색하는 순서는 가장 최근에 형성된 스코프가 우선합니다. **스택에서 식별자를 검색할 때는 스택의 맨 위에서 아래쪽으로 검색합니다. 그리고 최대 함수 몸체 스코프까지 검색**합니다. 그래도 찾지 못하면 **전역변수**에서 찾습니다.

#### 정적변수, 전역변수는 별도로 표시한다

정적변수나 전역변수는 모두 **데이터 영역을 사용하는 변수**들입니다. 동적 할당한 경우처럼 별도의 영역에 따로 떼어 표시합니다.

지금까지 스택 프레임에 대해서 알아봤습니다. 이 내용을 제대로 이해하고 있으면 '재귀호출'을 정확히 이해할 수 있습니다.


## 재귀 호출


재귀호출(recursive function call)은 **함수가 내부에서 다시 자기 자신을 호출하는 것**입니다. **반복문과 스택 자료구조를 합친 것이 바로 재귀호출**입니다. 논리적인 코드의 구조는 반복문과 같으나 **반복 과정에서 선형 자료구조인 스택이 필요한 경우 재귀호출을 사용**합니다.

```c
#include <stdio.h>

int main(void)
{
    int i = 0, nFact = 1;
    for (i = 5; i >= 1; --i)
        nFact *= i;

    printf("5! == %d\n", nFact);
    return 0;
}
```
다음 예제는 5의 계승을 계산하는 프로그램으로 반복문을 이용해 곱셈 결과를 누적하는 방식으로 계산합니다. 이 코드를 재귀호출 방식으로 변경해봅시다.

```c
#include <stdio.h>

// 계승을 계산하고 결과를 반환하는 함수
int GetFactorial(int nParam)
{
    int nResult = 0;

    // 재귀호출을 끝내기 위한 조건식
    // 반복문의 조건식과 같다.
    if (nParam == 1)    return 1;

    // 반복문의 계수기와 같다.
    nResult = nParam * GetFactorial(nParam - 1);
    return nResult;
}

int main(void)
{
    printf("5! == %d\n", GetFactorial(5));
    return 0;
}
```
반복문에서는 조건을 만족하지 못하면 반복이 멈추지만 **재귀호출에서는 조건에 부합할 때 함수가 반환하는 방법으로 멈춥니다**. 마지막에 피호출된 `GetFactorial()` 함수의 `nParam`이 1이면 조건을 만족하므로 함수가 봔환됩니다.

### 1. 재귀호츨을 이용한 문자열 출력

재귀호츨을 사용하는 가장 흔한 경우는 **비선형 자료구조**를 다룰 때입니다. 대표적으로 **트리(tree)**가 있으며, 자료를 계층적 구조로 만든 것이 트리의 특징입니다.

```c
#include <stdio.h>

void PutData(char *pszParam)
{
    // 문자열의 끝이면 반환
    if (*pszParam == '\0')
        return;

    // 다음 두 구문의 실행 순허를 바꾸면 문자열이 뒤집어져 출력
    putchar(*pszParam);
    PutData(pszParam + 1);
}

int main(void)
{
    PutData("TestData");
    putchar('\n');
    return 0;
}
```
위의 예제에서 재귀호출부터 하고 함수가 반환한 후에 문자를 출력하도록 코드를 수정하면 문자들은 거꾸로 뒤집혀 출력됩니다.

스택은 LIFO(Last In First Out) 구조입니다. 이러한 구조가 자주 사용되는 이유는 '되돌리기(undo)'기능과 같은 것을 구현하기 좋기 때문입니다.

### 2. 재귀호출의 장/단점

재귀호출은 "반복문과 스택 자료구조의 조합"으로 정의할 수 있습니다. 재귀 호출을 사용하면 개발자의 편의를 도모할 수도 있고 코드가 간단해질 수도 있습니다. 그러나 반복문에 비해 훨씬 더 많은 연산이 수행됩니다. 그리고 가장 큰 단점은 기본 설정을 유지했을 때 1MB 정도에 불과한 **스택 메모리를 순식간에 대량으로 소모할 가능성이 높다**는 것입니다. 그리고 스택 메모리를 모두 소진하면 **스택 오버플로우(stack overflow)** 오류에 의해 프로그램은 비정상 종료됩니다.

재귀호출을 사용하는것은 신중을 기해야 합니다. 반복문으로 할 수 있다면 반복문을 쓰는 것이 맞습니다. 그러나 비선형 자료구조인 트리를 다룰 때는 대부분 재귀호출을 사용합니다. 그리고 그것이 맞습니다.

## 문자/문자열 처리 함수

CRL(C-Runtime Library)은 많은 표준함수를 제공합니다. 표준함수는 호환성이나 안정성이 이미 오랜 시간 동안 검증된 좋은 코드이므로, 알아 두었다가 그런 기능이 필요할 때 잘 사용하면 됩니다.

### 1. 문자 처리 함수

- `isalpha()`: A~Z, a~z에 속하는 문자인지 검사하는 함수이다.
- `isdigit()`: 0~9에 속하는 문자(char)인지 검사하는 함수이다.
- `isxdigit()`: 0-9, A-F, a-f에 속하는 문자(char)인지 검사하는 함수이다.
- `isalnum()`: 0~9, A~Z, a~z에 속하는 문자(char)인지 검사하는 함수이다.
- `islower()`: 영운 소문자인지 검사하는 함수이다.
- `isupper()`: 영문 대문자인지 검사하는 함수이다.
- `isspace()`: Ox09~0x0D 혹은 Ox20에 속하는 화이트 스페이스 문자인지 검사하는 함수이다.
- `toupper()`: 영문 소문자를 대문자로 변환하는 함수이다.
- `tolower()`: 영운 대문자를 소문자로 변환하는 함수이다.

### 2. 문자열 처리 함수

`gets()`, `puts()`, `printf()`, `scanf()` 함수들도 모두 문자열 처리 함수들입니다.


#### `strcat()`, `strncat()` 함수를 이용한 문자열 붙이기

```c
char *strcat(char *strDestination, const char *strSource);
```
- 인자
    - strDestination: 문자열을 추가(append)하여 저장할 메모리 주소
    - strSource: 추가할 문자열이 저장된 메모리 주소
- 반환값
    - strDestination: 인자로 주어진 주소 반환

```c
char *strncat(char *strDestination, const char *strSource, size_t count);
```
- 인자
    - strDestination: 문자열을 추가(append)하여 저장할 메모리 주소
    - strSource: 추가할 문자열이 저장된 메모리 주소
    - count: 추가할 문자열 길이
- 반환값
    - strDestination: 인자로 주어진 주소 반환

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char szPath[128] = {"C:\\Program Files\\"};
    char szBuffer[128] = {0};
    printf("Input path: ");
    gets(szBuffer);

    strcat(szPath, szBuffer);
    puts(szPath);
    return 0;
}
```

보통 `strcat()` 함수가 반환한 주소값은 잘 사용하지 않습니다. 함수를 호출할 때 첫 번째 인수로 기술한 주소를 그대로 반환하기 때문입니다.

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char szPath[128] = {"C:\\Program Files\\"};

    strcat(szPath, "CHS\\");
    strcat(szPath, "C programming");
    puts(szPath);

    strcpy(szPath, "C:\\Program Files\\");
    strcat(szPath + strlen("C:\\Program Files\\"), "CHS\\");
    strcat(szPath + strlen("C:\\Program Files\\CHS\\"), "C programming");
    puts(szPath);
    return 0;
}
```
위의 예제의 `strlen()` 함수는 사실상 필요 없습니다. `strcat()` 함수가 내부적으로 호출하여 문자열의 끝을 스스로 계산하기 때문입니다. 참고로 `strlen()` 함수는 문자열의 깅리를 측정하기 위해 내부적으로 `while`문을 이용합니다. 결국 **문자열의 길이가 늘어날수록 길이를 측정하기 위해 반복해야 한 횟수가 늘어나고 그만큼 효율을 떨어뜨립니다**.

결국 대안으로 직접 새로운 `strcat*()` 함수를 만드는 것입니다. 문자열을 이어 붙인 후 **맨 마지막 문자(`\0`이 아닌 문자)가 저장된 메모리 주소를 반환**합니다. 그러면 두 번째로 이어 붙일 때는 문자열의 길이를 처음부터 측정하지 않을 수 있습니다.

```c
#include <stdio.h>
#include <string.h>

char* mystrcat(char *pszDst, char *pszSrc)
{
    while (*pszDst != '\0')
        ++pszDst;

    while (*pszSrc != '\0')
        *pszDst++ = *pszSrc++;

    *++pszDst = '\0';
    return --pszDst;
}

int main(void)
{
    char szPath[128] = {0};
    char *pszEnd = NULL;

    pszEnd = mystrcat(szPath, "C:\\Program Files\\");
    pszEnd = mystrcat(pszEnd, "CHS\\");
    pszEnd = mystrcat(pszEnd, "C programming");

    puts(szPath);
    return 0;
}
```

#### `sprintf()` 함수를 이용한 문자열 붙이기

`printf()` 함수와 거의 같습니다. 다만 문자열을 콘솔 화면이 아니라 '메모리'에 출력한다는 점이 다릅니다.

#### `strpbrk()` 함수를 이용한 구문 분석

'문자들' 중 하나가 있는지 검색합니다. 예를 들어, 검색 대상 문자열에서 "ABC"를 검색하면 "ABC"라는 문자열을 검색하는 것이 아니라, 'A', 'B', 'C'가 있는지 대상 문자열에서 검색합니다. 그리고 한 글자라도 일치하는 것을 찾으면 그 주소를 반환합니다.

```c
char *strpbrk(const char *string, const char *strCharSet);
```
- 인자
    - string: 검색 대상 문자열이 저장되 메모리 주소
    - strCharSet: 검색할 문자집합
- 반환값
    - 찾으면 해당 문자가 저장된 메모리 주소 반환
    - 찾지 못하면 `NULL` 반환

#### `strtok()` 함수를 이용한 구문분석

몇몇 골치아픈 문제가 있기 때문에 가급적 사용은 자제하기 바랍니다.

```c
char *strtok(char *strToken, const char *strDelimit);
```
- 인자
    - strToken: 토큰화 할 문자열이 저장된 메모리 주소
    - strDelimit: 토큰의 기준이 되는 구분자 문자집합
- 반환값: 해당 문자가 저장된 메모리의 내용을 `NULL`로 바꾸고 문자열의 시작 주소를 반환

임의의 문자열을 토큰화하는 함수입니다. '토큰화(tokenize)'라는 말은 긴 문자열을 규칙에 따라 잘게 자르는 것을 의미하는데, 이 말의 구체적인 의미는 **문자열 중간에 `NULL`을 집어넣는 것**입니다. `strtok()` 함수는 검색 대상 메모리에 '쓰기'를 시도(`NULL` 삽입)하는 데다 내부적으로 정적변수를 사용하기 때문에 멀티스레드 환경에서 문제가 발생할 수 있습니다.

### 3. 유니코드 문자열

C 언어에서 문자열은 두 종류로 구별할 수 있는데, 첫 번째는 MBCS(Multi-bytes Character Sets) 문자열이고 두 번째는 유니코드(UNICODE) 문자열입니다. MBCS에서 영문 한 글자는 1바이트, 한글 한 글자는 2바이트를 사용합니다. 그리고 `char`형으로 문자를 표현합니다. 그러나 "문자열"이라는 한글 문자열은 길이가 6이긴 한데, 문자의 개수는 3개 입니다. 즉, **문자열의 문자 개수와 길이가 서로 다르다는 문제가 발생**합니다.

이러한 문제들을 극복하기 위해 유니코드가 등장했습니다. 유니코드는 문자 하나를 표현하기 위해 16비트 혹은 32비트 자료형을 사용합니다. 따라서 유니코드 형식인 `wchar_t`형은 2바이트(1바이트=8비트)입니다.

유니코드는 상수 형식으로 표기할 때 문자열 앞에 'L'을 붙여 `L"String"` 형식으로 표기합니다. 따라서 `L"String"`의 자료형은 `wchar_t[7]`이며 바이트 단위 크기는 14바이트입니다. 그리고 `L"문자열"`의 자료형은 `wchar_t[4]`입니다. 메모리의 크기는 8바이트입니다. 유니코드에서는 영문, 한글에 상관없이 필요한 메모리 크기가 '(문자열의 길이 + 1) * `sizeof(wchar_t)`'로 통일됩니다.

#### `wprintf()`, `wcscpy()` 함수

유니코드 문자열은 **유니코드 문자열 전용 함수**를 사용해야 합니다. `printf()` 대신 `wprintf()` 함수를 사용하고, `strcpy()` 대신 `wcscpy()` 함수를 사용합니다. 모든 문자열처리 함수에 대해 MBCS 버전과 UNICODE 버전이 함께 존재합니다.

#### `wcstombs()`, `mbstowcs()` 함수

```c
size_t wcstombs(char *mbstr, const wchar_t *wcstr, size_t count);
```

- 인자
    - mbstr: MBCS로 변환한 문자열을 저장할 메모리 주소
    - wcstr: MBCS로 변환할 유니코드 문자열이 저장된 메모리 주소
    - count: MBCS로 변환할 문자열의 최대 크기
- 반환값: MBCS로 변환된 문자열 길이 (mbstr 인수가 `NULL`이면 변환을 위해 필요한 메모리 길이 반환)
- 설명: 유니코드 문자열을 MBCS 문자열로 변환하는 함수

```c
size_t mbstowcs(wchar_t *wcstr, const char *mbstr, size_t count);

```
- 인자
    - wcstr: 유니코드로 변환한 문자열을 저장할 메모리 주소
    - mbstr: 유니코드로 변환할 MBCS 문자열이 저장된 메모리 주소
    - count: 유니코드로 변환할 문자열의 최대 크기
- 반환값: 유니코드로 변환된 문자열 길이 (wcstr 인수가 `NULL`이면 변환을 위해 필요한 메모리 길이 반환)
- 설명: MBCS 문자열을 유니코드 문자열로 변환하는 함수

## 유티리티 함수

### 1. `atoi()`, `atol()`, `atof()` 함수

`atoi()` 함수 이름의 의미는 'ASCII to integer'입니다. 사용빈도가 높은 함수입니다.

```c
int atoi(const char *string);
```
- 인자: 변환할 문자열이 저장된 메모리 주소
- 반환값: 변환된 `int` 값, 실패할 경우 `0`
- 설명: 정수 문자열을 실제 정수로 변환하는 함수

```c
long atol(const char *string);
```
- 인자: 변환할 문자열이 저장된 메모리 주소
- 반환값: 변환된 `long` 값, 실패할 경우 `0L`
- 설명: `long`형 숫자 문자열을 실제 `long` 숫자로 변환하는 함수

```c
double atof(const char *string);
```
- 인자: 변환할 문자열이 저장된 메모리 주소
- 반환값: 변환된 값, 실패할 경우 `0.0`
- 설명: 실수 문자열을 실제 실수로 변환하는 함수

```c
#include <stdio.h>
#include <stdlib.h>

void main(void)
{
    char szBuffer[32];
    int nResult = 0;

    printf("Input String: ");
    gets(szBuffer);

    nResult = atoi(szBuffer);
    printf("%d\n", nResult);
}
```
자료의 표현번위를 벗어나는 경우에는 표현할 수 있는 최대값을 반환합니다. 이와 같은 오류가 발생했을 때 프로그램이 비정상 종료되는 것이 아니라 프로그램은 멀쩡한 데 연산 결과가 바르지 못한 경우가 되어 오류를 찾아내기 매우 까다롭습니다.

### 2. `time()`, `localtime()`, `ctime()` 함수

컴퓨터에서 시간을 표시할 때는 UTC(Universal Time Coordinated)나 GMT(Greenwich Mean Time)를 기준으로 표시합니다. GMT는 하루가 정확히 24시간으로 이루어졌다고 가정하여 시간을 계산합니다. 문제는 실제로 지구의 하루가 정확히 24시간이 아니라는데 있습니다. 이런 이유로 많은 **컴퓨터가 UTC를 기준으로 시간을 표시**하고 있습니다.

C 언어 표준 라이브러리 함수인 `time()` 함수는 1970년 1월 1일 자정부터 현재(컴퓨터에 설정된 시간)까지 흘러간 시간을 초 단이로 계산해주는 함수입니다. 반환값으로 결과를 알 수 있으므로 대부분 `NULL`을 인자로 호출합니다.

```c
time_t time(time_t *timer);
```

```c
struct tm *localtime(const time_t *timer);
```

```c
char *ctime(const time_t *timer);
```

```c
#include <stdio.h>
#include <time.h>

void main()
{
    struct tm *ptime = {0};
    time_t t = 0;

    t = time(NULL);
    ptime = localtime(&t);

    printf("%d\n", t);
    printf("%s", ctime(&t));
    printf("%04d-%02d-%02d\n",
        ptime->tm_year + 1900,  // 과거에는 연도를 두 자리 숫자로 표기
        ptime->tm_mon + 1,  // months since January - [0, 11]
        ptime->tm_mday);
}
```

### 3. `srand()`, `rand()` 함수

`rand()` 함수는 난수(0~0x7FFF)를 발생하는 함수입니다. 참고로 0x7FFFF를 십진수로 변환하면 32767입니다. 그리고 난수의 최대값은 `RAND_MAX`라는 상수를 사용합니다.

그리고 `rand()` 함수를 호출하기 앞서 반드시 `srand()` 함수를 호출하여 초기값을 설정해야 늘 다른 값을 반환합니다. 그렇지 않으면 시작할 때마다 매번 같은 순서의 난수가 발생합니다.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main()
{
    int i = 0;
    srand((unsigned)time(NULL));
    for (i = 0; i < 10; ++i)
        printf("%6d\n", rand());  // RAND_MAX 범위에서 난수 발생

    for (i = 0; i < 10; ++i)
        printf("%6d\n", rand() % 10);  // 0에서 10미만의 난수 발생
}
```
난수의 범위는 '나머지 연산자'를 통해 제한할 수 있습니다. 만일 가위바위보 게임 같은 것을 개발하고자 한다면 난수의 범위를 0~2로 제한하면 됩니다.

### 4. `system()`, `exit()` 함수

`system()` 함수는 명령 프롬프트를 통해 명령을 내리는 것과 같은 기능을 제공합니다.

```c
#include <stdio.h>
#include <stdlib.h>

void main()
{
    char szCommand[512] = {0};
    printf("Input command: ");
    gets(szCommand);
    system(szCommand);
}
```

`exit()` 함수는 프로그램을 즉시 종료하는 함수입니다.

```c
#include <stdio.h>
#include <stdlib.h>

void main()
{
    char ch;
    printf("Do you want to EXIT? (Y/N)\n");
    ch = getchar();

    if (ch == 'y' || ch == 'Y')
    {
        puts("EXIT");
        exit(1);
    }
    puts("End of main()");
}
```


## 연습문제

[문제 01](../code/12/02.c)

[문제 02](../code/12/03.c)

[문제 03](../code/12/04.c)

[문제 04](../code/12/05.c)

[문제 05](../code/12/06.c)