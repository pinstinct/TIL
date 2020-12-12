# 전처리기

전처리기(preprocessor)는 **컴파일러가 소스코드를 컴파일하기에 앞서 선행 처리하는 구문**으로 모두 `#` 기호가 앞에 붙어다니는 외형상 특징이 잇습니다. 모든 C 언어 컴파일러들은 전처리기로 정의된 것들을 소스코드에 반영한 후 컴파일합니다.

## `#include`

이 전처리기의 기능은 이름처럼 외부 파일(보통은 헤더 파일)을 현재 소스코드의 위쪽에 포함시켜서 함께 컴파일하도록 설정합니다. 헤더파일명을 `<`와 `>` 기호 사이에 기술하는데 이는 "**헤더파일을 찾을 때 시스템에 등록된 경로에서 찾으라**"는 뜻입니다. `"`(큰따옴표)를 이용한 경우에는 시스템 경로가 아니라 **프로젝트의 현재 경로에서 헤더 파일을 검색**합니다.

## 매크로

매크로(macro)는 외형상으로는 함수의 모습을 하고 있으나, **실제로는 함수가 아니라 한 행 혹은 여러 행으로 기술할 수 있는 구문(혹은 항)**입니다. 프로그램 코드 중 불연속적으로 반복되는 것을 함수로 만듭니다. 그래야 유지보수 하기 좋습니다. 그런데 대단히 자주 호출되는 함수면서 길이가 짧다면 함수로 만드는 것이 잘한 것인지 다시 생각해봐야 합니다.

왜냐하면, 함수를 호출하려면 스택 프레임에 매개변수 메모리도 지정해야 하고 인수도 복사해야 하며 제어의 흐름도 변경해야 하기 때문입니다. 정작 함수로써 수행할 코드는 얼마 안되는데 함수 호출로 인한 오버헤드(overhead)가 더 커질 수도 있습니다. 

그래서 나온 것이 **매크로와 __inline**입니다. 순서를 따지자면 매크로가 구형이고 __inline이 더 최근에 만들어진 신형이며, 매크로의 여러 단점이 보완되었습니다.

### 1. __inline 함수와 매크로

다음 예제는 함수와 매크로를 비교한 것입니다.

```c
#include <stdio.h>

// 매크로 함수 정의(실제 함수는 아님)
#define ADD(a, b) (a + b)

// 사용자 정의 함수 선언 및 정의
int Add(int a, int b)
{
    return a + b;
}

int main(void)
{
    // Add() 함수를 호출하고 반환 결과를 출력
    printf("%d\n", Add(3, 4));

    // ADD() 매크로를 '실행'하고 결과를 출력
    printf("%d\n", ADD(3, 4));
    return 0;
}
```

많은 개발자들은 일반 함수와 매크로를 구별하기 위해 매크로 이름은 모두 대문자로 기술하는 경향이 있습니다.

`printf("%d\n", Add(3, 4));` 코드는 `Add()` 함수를 call합니다. 그러나 `ADD()` 매크로의 경우에는 **3과 4를 더한 결과인 7**을 `printf()` 함수의 매개변수로 전달합니다. 즉, **함수호출 연산은 하지 않았으며 그로 인한 오버헤드도 없습니다.** 함수의 장점을 그대로 유지하고도 성능을 향상시킨 것입니다.

### 2. 매크로 특수화 연산자 `#`, `##`

오로지 매크로 내부에서만 사용할 수 있는 연산자이며 `#`은 **인수가 무엇이든 모두 문자열**로 만들어주는 연산자이고, `##`은 **두 매개변수를 한 덩어리로 묶어 코드를 만들어 주는 연산자**입니다.

```c
#include <stdio.h>

// a를 "a"(문자열)로 변경하는 매크로 정의
#define STRING(a) #a

// a와 b를 합쳐 하나로 붙여주는 매크로 정의
#define PASTER(a, b) a##b

int main(void)
{
    int nData = 10;
    
    printf("%d\n", PASTER(nDa, ta));  // 그냥 nData라고 쓴 것과 같다.
    printf("%d\n", nData);
    printf("%s\n", STRING(nData));  // "nData"로 처리
    return 0;
}
```

`PASTER()` 매크로는 두 개의 토큰(token)을 인수로 받아 새로운 하나의 토큰으로 만들어 줍니다. 이와 같이 매크로를 잘 알아두면 '코드 생성기' 혹은 '코드 자동화'를 구현하는데 도움이 됩니다. 사실 매크로라는 것의 가장 큰 쓰임새 중 하나는 바로 '코드 생성기'를 이용한 자동화에 있습니다. 여기에 조건부 컴파일 전처리기까지 더해지면 매우 정교한 처리가 가능합니다.

## 조건부 컴파일

상수 정의에 따라 실제로 번역되는 소스코드가 달라지도록 구성하는 것을 말합니다. `#if XXX`, `#else`, `#endif` 이렇게 세 가지 전처기리를 사용해서 두 덩어리의 코드 중 하나만 선택해 베타적으로 컴파일 할 수 있습니다.

```c
#include <stdio.h>

// _MSGTEST_ 상수 정의가 됐는가, 그렇지 않은가에 따라
// MYMESSAGE 상수 정의는 달라진다.
#ifdef _MSGTEST_
#define MYMESSAGE "I am a boy."
#else
#define MYMESSAGE "You are a girl."
#endif

int main(void)
{
    puts(MYMESSAGE);
    return 0;
}
```
위의 예제에서 실제로 컴파일하는 코드는 다음과 같습니다.

```c
#include <stdio.h>

int main(void)
{
    puts("You are a girl.");
    return 0;
}
```

그러나 `#ifdef _MSGTEST_` 구문 전에 `#define _MSGTEST_`라고 기술하면 다음과 같이 달라집니다.

```c
#include <stdio.h>

int main(void)
{
    puts("I am a boy.");
    return 0;
}
```

조건부 컴파일을 이용하여 할 수 있는 가장 대표적인 것 중 하나는 문자열 처리와 관련된 것들입니다. 만일 MBCS와 유니코드 문자집합을 모두 지원하는 상황이라면 상황에 따라 '문자형'에 대한 정의를 변경해 프로그램을 빌드할 수 있습니다.

#### 문자형 선택 

```
#include<stdio.h>
#define MYUNICODE

#ifdef MYUNICODE  // 유니코드 형식에 맞춘 정보들을 정의
    typedef wchar_t TCHAR;  // 형재선언에 의해 TCHAR는 wchar_t형
    #define _T(string) L##string  // 매크로 정의, 인자로 전달된 문자열 상수를 유니코드 문자열 상수로 만든다.
    #define PRINT wprintf  // wprintf를 PRINT로 정의
#else  // MBCS 형식에 맞춘 정보들을 정의 
    typedef char TCHAR;
    #define _T(string) string
    #define PRINT printf
#endif

void main()
{
    TCHAR szData[16] = _T("Test String");
    PRINT(_T("%s\n"), szData);
    PRINT(_T("%d, %d\n"), sizeof(TCHAR), sizeof(szData));
}
```

#### 빌드 모드 선택

```c
#include <stdio.h>
// #define _DEBUG

#ifdef _DEBUG
    #define MODEMESSAGE "Debug mode"
#else
    #define MODEMESSAGE "Release mode"
#endif

int main(void)
{
    puts(MODEMESSAGE);
    return 0;
}
```
실제로 개발자들이 프로그램을 디버깅할 때 많이 사용하는 코드 입니다. 조건부 컴파일 전처리기를 구성하여 두 가지 코드를 작성하고 디버그 모드일 땐 개발자용 메시지를, 릴리즈 모드일 땐 일반 사용자가 보는 메시지를 출력되도록 할 수 있습니다.

그리고 자주 사용하는 전처리기인 `#pragma` 전처리기는 17장에서 다루겠습니다.