# 함수에 대한 고급 이론

함수의 이름도 배열의 이름처럼 주소상수에 부여한 식별자입니다. 그러므로 포인터 변수에 담을 수 있는 정보입니다. 응용하자면 다른 함수에 내가 만든 함수의 주소를 알려줘서 호출하도록 코드를 만들 수도 있습니다.

## 성능 향상을 위한 이론

함수를 호출하려면 비용(CPU + 메모리 사용)이 듭니다. 함수호출 그 자체가 이미 연산인데다 스택 메모리를 사용해야 합니다. 또한 프로그램의 흐름이 변경되기 위한 각종 연산이 수반됩니다. 그러므로 아주 간단한 작업을 함수로 만드는 것은 효율적이지 못합니다.

그래서 과거에는 외형상 함수지만 사실은 함수가 아니라 일반연산으로 처리될 수 있는 '매크로(Macro)'를 이용했습니다. 그러나 이제는 매크로의 단점을 보완한 `__inline` 함수가 도입되어 매크로가 아니어도 원하는 바를 이룰 수 있습니다.

### 1. 컴파일러 최적화

최근 컴파일러들은 과거와 비교하면 훨씬 더 강력한 최적화 기능을 제공합니다. 불필요한 코드를 제거하여 연산을 줄이는 수준에서 함수를 한 줄짜리 구문 정도로 만들어버리는 수준까지 향상되었습니다.

```c
#include <stdio.h>

int Add(int a, int b)
{
    int nResult = 0;
    nResult = a + b;
    return nResult;
}

int main(void)
{
    int nResult = 0;
    nResult = Add(3, 4);
    printf("%d\n", nResult);
    return 0;
}
```

`printf("%d\n", nResult);` 코드는 사실상 `printf("%d\n", 7);` 코드처럼 번역됩니다. 컴파일러가 이와 같이 최적화할 수 있었던 이유는 `Add()` 함수의 매개변수를 '상수'로 기술했기 때문입니다. 변수는 말 그대로 변할 수 있는 속성을 가졌고, 변수에 대한 연산은 그 변수에 대해 의존적일 수밖에 없습니다.

따라서 아래와 같이 코드를 수정하면, 최적화 규칙을 통해 생략될 수 없습니다.

```c
#include <stdio.h>

int Add(int a, int b)
{
    int nResult = 0;
    nResult = a + b;
    return nResult;
}

int main(void)
{
    int nResult = 0, x, y;
    scanf("%d%d", &x, &y);
    nResult = Add(x, y);
    printf("%d\n", nResult);
    return 0;
}
```

그래도 `Add()` 함수는 번역되지 않습니다. 따라서 호출할 수도 없습니다. 대신 `add edx, dword ptr[y]`라는 어셈블리어 코드가 존재함을 확인할 수 있습니다. 즉, 사용자가 입력한 정보를 덧셈만 해서 결과를 계산하도록 번역된 것입니다. 따라서 결과적으로는 함수를 호출한 것과 마찬가지가 됩니다. 이와 같이 컴파일러의 최적화 수준은 놀랍습니다.

### 2. `__inline` 함수

매크로의 가장 심각한 오류는 실제로는 함수가 아니면서 함수인척하고 있다는 사실입니다. 그리고 매개변수의 자료형을 명시할 수 없다는 점과 여러 구문을 묶거나 제어문을 포함한다든지 혹은 지역변수를 선언하는 일이 불가능하므로 논리구조를 만들어내는 데 한계가 있습니다.

그러나 인라인 함수는 매크로의 장점을 그대로 살리면서도 매개변수의 자료형 문제, 괄호 문제, 지역변수, 제어문 문제 등 다양한 문법적 단점을 극복했습니다. 그렇다고 일반 함수처럼 모든 것이 다 허용되는 것은 아닙니다.

```c
#include <stdio.h>

int Add(int a, int b)
{
    return a + b;
}

__inline int NewAdd(int a, int b)
{
    return a + b;
}

int main(void)
{
    printf("%d\n", Add(3, 4));
    printf("%d\n", NewAdd(3, 4));
    return 0;
}
```

## 함수 호출 규칙 

함수 호출 규칙(calling convention)은 호출자 함수가 피호출자 함수를 호출하는 과정에서 **매개변수를 전달하는 순서 및 매개변수가 사용한 메모리 관리방법 등에 관한 규칙**입니다. C/C++ 컴파일러의 기본 함수 규칙은 `__cdecl`입니다.

우리가 자동변수를 선언할 때 `auto`를 생략해도 되는 것처럼 `__cdecl`도 생략할 수 있습니다. 따라서 아무것도 기술하지 않으면 `__cdecl`입니다.

```c
#include <stdio.h>

int __cdecl main(void)
{
    printf("Hello, World\n");
    return 0;
}
```

호출 규칙 | 매개변수 스택정리 | 매개변수 메모리
--- | --- | ---
`__cdecl` | Caller | Stack
`__stdcall` | Callee | Stack
`__fastcall` | Callee | Stack + Register

### 1. `__cdecl`

`__cdecl` 호출 규칙은 **매개변수를 오른쪽부터 스택에 Push**합니다. 그리고 **매개변수로 인해 증가한 스택을 호출자 함수가 본래 크기로 줄입니다.**

우리가 자동변수라고 알고 있었던 것들이 모두 스택 영역 메모리를 사용한다는 사실은 이미 알고 있습니다. 그런데 문제는 여기서 메모리가 자동으로 관리된다는 말의 실상은 사용되는 스택의 영역이 늘거나 줄어드는 것에 불과합니다. 힙 영역 메모리처럼 운영체제에 반환되는 형태로 관리되는 것이 아닙니다.

다음 예제의 `GetMax()` 함수는 `int`형 매개변수 3개를 받아 최대값을 반환하는 함수입니다. 따라서 매개변수로 인해 증가하는 스택의 크기는 12바이트입니다.


```c
#include <stdio.h>

int __cdecl GetMax(int a, int b, int c)
{
    int nMax = a;
    if (b > nMax) nMax = b;
    if (c > nMax) nMax = c;
    return nMax;
}

int __cdecl main(void)
{
    int nResult = 0;
    nResult = GetMax(1, 2, 3);
    return 0;
}
```

디스어셈블리 화면을 확인하면, `nResult = GetMax(1, 2, 3);` 코드에서 오른쪽 인수 3부터 스택에 Push 합니다. 그리고 Call 연산으로 `GetMax()` 함수를 호출한 후, `main()` 함수 내부에서는 `add esp,0ch`라는 연산을 수행합니다. 여기서 `0ch`는 `0x0c` 즉, 10진수 12를 의미하며, `exp(extended stack pointer)`는 스택 메모리에 대한 '포인터'입니다. 포인터이므로 당연히 주소가 들어 있는데, 이 주소에 대해 ADD 연산을 수행하면 당연히 주소는 증가합니다. 

그러니까 지금 코드에서 12바이트만큼 증가합니다. 주소가 증가했다는 것은 스택의 감소를 의미합니다. 즉, `main()` 함수에 들어가는 이 한줄의 코드로 스택은 `GetMax()` 함수호출 전 상태로 복원되는 것입니다.

### 2. `__stdcall`

`__stdcall` 호출 규칙도 `__cdecl` 호출 규칙처럼 **매개변수를 오른쪽부터 스택에 Push**합니다. 그러나 매개변수로 인해 증가한 **스택을 호출자 함수가 정리하는 것이 아니라 피호출자 함수가 정리**합니다.

```c
#include <stdio.h>

int __stdcall GetMax(int a, int b, int c)
{
    int nMax = a;
    if (b > nMax) nMax = b;
    if (c > nMax) nMax = c;
    return nMax;
}

int __cdecl main(void)
{
    int nResult = 0;
    nResult = GetMax(1, 2, 3);
    return 0;
}
```

`main()` 함수가 `GetMax()` 함수를 호출함으로써 증가한 12바이트의 스택은 피호출자 함수인 `GetMax()` 함수가 정리할 것입니다.

`GetMax()` 함수를 호출한 이후로 `mov dword ptr [nResult], eax`라는 연산이 수행되었는데 이는 `GetMax()` 함수가 반환한 값을 `nResult`에 대입하는 C 코드에 대한 어셈블리 코드입니다. 스택을 정리하는 코드는 더는 보이지 않습니다. `GetMax()` 함수 내부에서 정리하기 때문입니다.

### 3. `__fastcall`

`__fastcall`은 `__stdcall`처럼 매개변수는 오른쪽부터 스택에 Push하고 피호출자 함수가 스택을 정리합니다. 단, **매개변수가 여러 개면 가장 나중에 Push되어야 할 왼쪽 첫 번째, 두 번째 매개변수는 스택 대신 CPU의 레지스터(EDX, ECX)를 이용해 전달**합니다. 따라서 매개변수가 메모리에 복사되는 횟수를 줄이고 그 때문에 연산속도가 일부 향상될 수 있습니다.

```c
#include <stdio.h>

int __fastcall GetMax(int a, int b, int c)
{
    int nMax = a;
    if (b > nMax) nMax = b;
    if (c > nMax) nMax = c;
    return nMax;
}

int __cdecl main(void)
{
    int nResult = 0;
    nResult = GetMax(1, 2, 3);
    return 0;
}
```

## 함수 포인터와 역호출 구조 

함수의 이름도 배열의 이름처럼 '주소상수'에 부요한 식별자입니다. 따라서 함수의 이름도 포인터 변수에 저장할 수 있습니다. 다만, 변수의 자료형이 함수 호출에 필요한 정보(매개변수, 호출규칙, 반환 자료형)들을 포함하고 있어야 변수를 이용해서 함수를 호출할 수 있습니다. 그래서 `void *`에 함수의 이름을 저장할 수는 있으나 호출할 수는 없습니다.

아래는 함수의 이름이 주소임을 확인하기 위한 예제입니다.

```c
#include <stdio.h>

int __cdecl main(void)
{
    // void*는 주소라면 무엇이든 담을 수 있다.
    // 함수이름은 '주소'이므로 void*에 담을 수 있다.
    void *pData = main;

    // 함수의 주소를 출력
    printf("%p\n", main);
    printf("%p\n", pData);
    return 0;
}
```

변수도 함수도 사실 다 주소로 식별합니다. 다만 그 주소의 메모리를 저장공간으로 활용할것인가, 아니면 CPU가 인식하는 명령코드로 볼 것인가만 다를 뿐입니다.

### 1. 함수 포인터

함수 포인터 문법의 기본형식은 다음과 같습니다.

```c
반환 자료형(호출규칙 *변수이름)(매개변수)
```

다음 에제는 매개변수로 `int`형 자료 3개, `int`형 정보를 반환하고 함수호출 규칙이 `__cdecl`인 함수에 대한 포인터 변수를 다룬 것입니다.

```c
#include <stdio.h>

// 최대값을 반환하는 함수 선언 및 정의
int GetMax(int a, int b, int c)
{   
    int nMax = a;
    if (b > nMax) nMax = b;
    if (c > nMax) nMax = c;
    return nMax;
}

int __cdecl main(void)
{
    // int 매개변수 셋을 받아 int 자료를 반환하는 함수 포인터 선언 및 정의
    int(__cdecl *pfGetMax)(int, int, int) = GetMax;

    // 함수 포인터를 이용해 함수 호출
    printf("MAX: %d\n", pfGetMax(1, 3, 2));
    return 0;
}
```
그리고 우리가 그동안 늘 봐오던 것이지만 거론되지 않은 연산자가 있는데, 그것은 바로 **함수호출 연산자**입니다. 함수 호출연산자는 바로 **괄호**이며 **주소(매개변수)**형식입니다. 여기서 주소는 함수이름 혹은 함수 포인터입니다.

### 2. 역호출 구조

함수호출 연산자나 함수 포인터가 꼭 필요한 경우는 다음과 같습니다.

- 동적 연결 라이브러리(DLL, Dynamic Linking Library)를 활용하는 경우
- 역호출(call back) 구조를 구현하는 경우

동적 연결 라이브러리는 보통 시스템 프로그래밍 역역이기 때문에 여기서 다루지 않습니다. 

우리는 지금까지 우리가 정의한 사용자 정의 함수를 자신이 작성하는 함수에서 **직접 호출**하는 능동적인 방법으로 함수를 호출했습니다. 그런데 이 함수라는 것이 작성자 입장에서 "내가 호출하는 것이 아니라 다른 무엇에 의해 호출"될 수도 있습니다. 역호출 구조를 이해하기 위해 `qsort()` 함수에 대해 알아보겠습니다.

```c
void qsort(void *base, size_t num, size_t width, int (__cdecl *compare)(const void *, const void *));
```

- 인자
  - base: 정렬대상 배열의 기준주소
  - num: 배열요소의 개수
  - width: 배열요소의 바이트 단위 크기
  - compare: 각 요소를 비교하여 같을 경우 0, 그렇지 않을 경우 양수 혹은 음수를 반환하는 함수의 주소
- 반환값: 없음
- 설명: 퀵 정렬 알고리즘을 이용하여 배열에 담긴 요소를 정리하는 함수이다. 사용자 정의 콜백 함수를 만들어 인수를 전달하는 방법으로 각 항을 비교하는 방법을 구체화한다.

`qsort()` 함수의 네 번째 매개변수는 `const void*` **둘을 매개변수로 받고 `int`형 자료를 반환하는 함수에 대한 포인터**입니다.

```c
#include <stdio.h>
#include <stdlib.h>

// qsort() 함수가 역호출할 함수의 선언 및 정의
// main() 함수가 직접 이 함수를 호출하지 않는다!
int MyCompare(const void *pParam1, const void *pParam2)
{
    return *(int*)pParam1 - *(int*)pParam2;
}

int main(void)
{
    int aList[5] = {30, 10, 40, 50, 20};
    int i = 0;

    // 배열 요소 비교 방법을 규정한 MyCompare() 함수의 주소를
    // qsort() 함수의 인수로 전달하고 qsort() 함수 내부에서 역호출
    qsort(aList, 5, sizeof(int), MyCompare);

    for (i = 0; i < 5; ++i)
        printf("%d\t", aList[i]);
    return 0;
}
```

**역호출(call back)**이라는 이름이 붙은 이유도 `qsort()` 함수의 호출자는 `main()` 함수지만 피호출자인 `qsort()` 함수가 다시 `MyCompare()` 함수의 호출자가 되기 때문입니다.

만일 `main()` 함수의 제작자가 철수라고 가정한다면 `MyCompare()` 함수의 제작자 역시 철수라고 할 수 있습니다. 그러나 `qsort()` 함수의 제작자가 누군지는 몰라도 적어도 그는 철수가 아니라고 생각해볼 수 있습니다. 길동이로 가정한다면, 최초 철수가 만든 `main()` 함수가 길동이가 만든 `qsort()` 함수를 호출합니다. 이때, 철수는 자신이 만든 함수의 주소를 길동이에게 전달합니다. 그러면 길동이는 자신의 코드를 수행하다가 철수가 알려준 주소의 함수를 '역으로' 호출(call back)합니다.

이 예제에서 `main()` 함수가 `MyCompare()` 함수를 호출하는 코드는 없습니다. 그럼에도 `MyCompare()` 함수는 분명히 호출됩니다. 즉, 피호출자 함수에 의해 역으로 호출됩니다.이 예제의 역호출 함수처럼 "**내가 호출하는 것이 아니라 자동으로 호출된다**"라는 개념은 앞으로도 대단히 중요합니다. 문법적으로 함수 포인터가 등장하는 것은 아니지만, 함수가 자동으로 호출된다는 가정에 기반을 둔 문법이 존재하며, 이를 명확히 이해하고 제대로 사용하려면 반드시 "자동으로 호출된다"라는 의미를 활용할 수 있어야 합니다. 그리고 그것을 프로그램의 설계에 반영할 수 있어야 합니다.

## 정적 라이브러리(static library) 구현

'라이브러리'는 함수들을 모아놓은 파일을 말합니다. 그리고 '정적'이라는 것은 라이브러리를 사용한 코드를 컴파일하고 링크하는 과정에서 마치 하나의 obj 파일처럼 실행 바이너리(.exe)의 일부로 포함된다는 뜻입니다.

### 1. 라이브러리 프로젝트 생성

이번에는 지금까지 만들어온 프로젝트와 달리 정적 라이브러리 프로젝트로 예제를 작성해야 합니다.

```c
/* LibTest.c */
#include <stdio.h>

void PrintData(int nParam)
{
    printf("PrintData(): %d\n", nParam);
}

void PrintString(const char *pszParam)
{
    printf("PrintString(): %s\n", pszParam);
}
```

위의 예제를 빌드합니다. 바이너리 파일의 확장자 'exe'가 아니라 'lib'라는 점에 주의합니다.

기존의 예제와 달리 `main()` 함수가 없고, 결과 바이너리 파일의 형식이 lib 파일임을 직접확인 했을 것입니다. lib 파일은 단독으로 실행하는 것이 아니라 링크타임에 exe 파일을 생성할 때 필요한 파일입니다.

### 2. 헤더파일의 구성

함수는 원형 선언과 정의로 나눌 수 있는데 일반적으로 확장자가 '.c'인 소스파일에는 정의가 들어가고 '.h'인 헤더파일에는 원형 선언이 들어갑니다. 만일 소스코드가 아니라 빌드된 결과 바이너리 파일로 정의가 제공될 때는 '.lib' 파일로 제공됩니다. 따라서 헤더와 라이브러리 파일은 한 세트로 생각할 수 있습니다.

앞서 만든 함수들의 원형 선언이 들어갈 헤더파일을 만듭니다.

```c
/* LibTest.h */
#pragma once

void PrintData(int);
void PrintString(const char *);
```
`#pragma once` 코드의 의미는 헤더파일이 중복 `include`되었을 때, 한번만 유효한 것으로 처리하도록 컴파일러에게 알리는 역할을 합니다.

이번 실습의 결과로 만들어진 **헤더파일과 라이브러리 파일은 한 세트**입니다. 이 라이브러리에 들어 있는 함수들을 사용하는 프로그램은 이 두 파일이 필요한데 헤더파일은 컴파일타임에 필요하며 라이브러리 파일은 링크타임에 필요합니다.

### 3. 정적 라이브러리 사용하기

함수들을 따로 모아서 라이브러리 파일로 만드는 이유는 모듈화(modulization)에 의한 장정 때문입니다. 모듈화를 하면
- 함수의 원형만 공개하고 실제 코드는 감출 수 있으며
- 프로그램일 작성하는 데 필요한 함수들은 마치 부품처럼 관리할 수 있습니다.
- 그리고 한 프로그램의 주요 기능을 여러 명의 개발자가 동시에 개발할 수 있습니다.

```c
/* TestApp.c */
#include "LibTest.h"

#pragma comment(lib, "LibTest")

int main(void)
{
    PrintData(10);
    PrintString("Test String");
    return 0;
}
```

TestApp 프로젝트에 위의 예제를 작성하고, 앞서 만들어둔 LibTest.lib 파일과 LibTest.h 파일을 TestApp 프로젝트 폴더에 복사한 후 빌드합니다.

`#pragma comment(lib, "LibTest")` 코드는 Visual studio에 설정된 기본 라이브러리 외에 다른 라이브러리가 사용되었음을 컴파일러에 알리고 함께 링크되도록 설정하는 코드입니다.

## 가변인자 사용하기

`printf()` 함수나 `scanf()` 함수는 **가변인자**라는 매우 독특한 기능을 제공합니다. 이 가변인자를 사용자 정의 함수에서도 사용할 수 있습니다. 

`GetMax()` 함수의 왼쪽 첫 번재 인자는 고정 인자로서 가변이 될 수 없고, 나머지 오른쪽 인자들의 개수가 전달되어야 합니다.

```c
#include <stdio.h>
#include <stdarg.h>  // 가변인자 사용을 위해 include

int GetMax(int nCount, ...)
{
    int nMax = -9999, nParam = 0, i = 0;
    va_list pList = {0};  // va_list는 char*를 형 재선언 한 것

    // va_start() 매크로를 통해 첫 번째 매개변수 이후의 매개변수가
    // 저장된 Stack 메모리의 주소를 pList에 저장
    va_start(pList, nCount);
    for (i = 0; i < nCount; i++)
    {
        // 가변인자들의 자료형이 int 형이라고 가정하고
        // va_arg() 매크로를 통해 pList가 가리키는 메모리의 내용을 해석해 int 형 변수 nParam에 대입
        // 이때, va_arg() 매크로 내부에서 pList의 주소값을 다음 매개변수가 저장된 메모리의 주소로 변경
        nParam = va_arg(pList, int);  
        if (nParam > nMax) nMax = nParam;
    }
    va_end(pList);  // pList를 0으로 초기화
    return nMax;
}

int main(void)
{
    printf("MAX: %d\n", GetMax(3, 10, 30, 20));
    printf("MAX: %d\n", GetMax(4, 40, 10, 30, 20));
    printf("MAX: %d\n", GetMax(5, 40, 10, 50, 30, 20));
    return 0;
}
```

