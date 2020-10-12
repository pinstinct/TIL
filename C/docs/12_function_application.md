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

## 스택 프레임 그리는 방법

## 재귀 호출

### 1. 재귀호츨을 이용한 문자열 출력

### 2. 재귀호출의 장/단점

## 문자/문자열 처리 함수

### 1. 문자 처리 함수

### 2. 문자열 처리 함수

### 3. 유니코드 문자열

## 유티리티 함수

### 1. `atoi()`, `atol()`, `atof()` 함수

### 2. `time()`, `localtime()`, `ctime()` 함수

### 3. `srand()`, `rand()` 함수

### 4. `system()`, `exit()` 함수