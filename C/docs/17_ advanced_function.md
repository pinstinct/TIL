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