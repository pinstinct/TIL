# 메모리와 포인터

## 컴퓨터와 메모리

**변수의 본질은 메모리**이며 모든 메모리는 자신의 위치를 **식별하기 위한 근거로 고유번호(일련번호)**를 갖는데, 이 번호를 **메모리 주소**라 합니다. 따라서 변수의 선언 및 정의는 메모리 확보를 의미하며, 선언 시 부여한 이름으로 확보한 메모리를 식별합니다.

변수를 이루는 세가지 요소는 다음과 같습니다. (예: `char ch = 'A';`)

1. 이름이 부여된 메모리 (`ch`, 식별자)
2. 그 안에 담긴 정보 (`'A'`)
3. 메모리의 주소 (`&ch`)

```c
#include <stdio.h>

int main(void)
{
    int nData = 10;
    printf("%d\n", nData);
    printf("%p\n", &nData);

    return 0;
}
```
`nData`를 대상으로 단항 연산인 주소 번지 연산(주소 연산)을 수행하여 그 결과를 메모리의 주소 형식(`%p`)으로 출력한 것입니다.

### 1. 메모리의 종류

메모리도 그 용도에 따라 스택(stack), 힙(heap), 데이터 영역(data section), 텍스트 영역(text section) 등으로 나뉩니다.

- Stack: 자동변수이고 지역변수인 변수가 사용하는 메모리 영역이며, 임시 메모리의 성격을 가진다. 크기가 작고 관리(할당 및 반환)가 자동으로 이루어지는 장점이 있다.
- Heap: **동적 할당할 수 있는 자유 메모리 영역**이며, 개발자 자신 스스로 직접 관리해야 한다. 대량의 메모리가 필요하거나 메모리의 크기를 미리 알 수 없을 때 사용한다.
- PE image (실행파일)
    - Text section: C 언어의 소스코드가 번역된 기계어가 저장된 메모리 영역이며, 기본적으로 읽기전용 메모리이다.
    - Data section
        - Read only: 상수 형태로 기술하는 문자열(예: "Hello")이 저장된 메모리 영역이며, Text 처럼 읽기는 가능하나 쓰기는 허용되지 않는다.
        - Read/Write: 정적변수나 전역변수들이 사용하는 메모리 영역이며, 별도로 초기화 하지 않아도 0으로 초기화 된다. 관리는 자동이다.

### 2. 포인터 변수의 선언 및 정의

포인터 변수는 **메모리의 주소를 저장하기 위한 전용 변수**입니다.

`nData`라는 이름이 부여된 변수(메모리)에 분명히 주소가 있지만 굳이 그것을 꼭 알아야 할 필요는 없습니다. 하지만 직접 메모리를 다루어야 할 경우도 있습니다. 메모리 주소를 알아내는 방법이 바로 단항 연산자인 주소 연산자를 사용한는 것입니다.

그리고 주소 연산과 정반대되는 개념의 연산자는 바로 '간접지정 연산자(`*`)'입니다. '지정'이라는 말은 임의 대상 메모리에 대한 길이와 해석방법(자료형)을 지정한다는 뜻입니다.

```c
#include <stdio.h>

int main(void)
{
    int x = 10;
    int *pnData = &x;   // int 형식에 대한 포인터 변수 선언 및 정의

    printf("%d\n", x);
    *pnData = 20;
    printf("%d\n", x);
    return 0;
}
```
`*pnData` 코드의 의미는 "포인터 변수 pnData에 저장된 주소를 가진 메모리를 int형 변수로 취급"한다는 뜻입니다.

### 3. 포인터와 배열

배열의 이름은 0번 요소의 주소이며, 전체 배열을 대표하는 식별자입니다. 즉, `int`형 포인터에 `int`형 변수의 주소뿐만 아니라, `int`형 배열의 이름도 담을 수 있습니다.

```c
#include <stdio.h>

int main(void)
{
    int aList[5] = {0};
    int *pnData = aList;

    printf("aList[0]: %d\n", aList[0]);
    *pnData = 20;
    printf("aList[0] : %d\n", aList[0]);
    return 0;
}
```
`int *pnData = aList`를 `int *pnData = &aList[0];`라고 수정해도 의미는 같습니다. 어차피 배열의 이름은 0번 요소의 주소에 부여한 식별자입니다.

그리고 `*pnData = 20;` 코드의 '간접지정 연산자'는 단항연산자이며, 사실 이 연산은 `*(pnData + 0)`을 의미합니다. 포인터 변수 `pnData`에 저장된 주소를 기준으로 오른쪽으로 `int` 0개 떨어진 위치(주소)의 메모리를 `int`형 변수로 지정한다는 것입니다.

그리고 `*(pnData + 0)`를 다른 코드로 표시하면 `pnData[0]`입니다. 배열과 포인터가 문법상 호환되는 이유는 개념적으로나 기술적으로나 사실상 같기 때문입니다. 단지 차이가 있다면 포인터 변수는 말 그대로 변수이고, 배열의 이름은 '주소상수'라는 것뿐입니다.

```c
#include <stdio.h>

int main(void)
{
    char szBuffer[16] = {"Hello"};
    char *pszData = szBuffer;
    int nLength = 0;

    while (*pszData != '\0')
    {
        pszData++;  // 포인터 한 칸 이동
        nLength++;
    }

    printf("Length: %d\n", nLength);
    printf("Length: %d\n", strlen(szBuffer));
    printf("Length: %d\n", strlen("World"));
    return 0;
}
```
위의 예제는 포인터 변수에 저장된 주소값을 계속 증가시키는 방법으로 배열의 처음부터 `\0`이 저장된 메모리가 나올 때까지 차례로 접근합니다. `pszData++` 단항 연산으로 오른쪽으로 `char`형 크기만큼 한 칸 이동(주소 증가)합니다.

```c
#include <stdio.h>

int main(void)
{
    char szBuffer[16] = {"Hello"};
    char *pszData = szBuffer;
    int nLength = 0;

    while (*pszData != '\0')
        pszData++;

    printf("Length: %d\n", pszData - szBuffer);
    return 0;
}
```
위의 예제는 주소 차이를 이용해 문자열의 길이를 측정하는 예를 보인 것입니다.

## 메모리 동적 할당 및 관리

`malloc()`과 `free()` 함수는 메모리를 동적으로 할당 및 해제하는 함수입니다. `malloc()` 함수를 이용하면 자동변수로 사용할 수 있는 메모리와는 비교할 수도 없을 만큼 큰 메모리를 자유롭게 다룰 수 있습니다. 게다가 '동적(dynamic, runtime)'으로 할 수 있습니다. 대신 반환(혹은 해제)의 책임이 따릅니다.

```c
void *malloc(size_t size);
```
- 인자: 할당받을 메모리의 바이트 단위 크기
- 반환값: 힙 영역에 할당된 메모리 덩어리 중 첫 번째 바이트 메모리의 주소
- 설명: 할당받은 메모리는 반드시 `free()` 함수를 이용하여 반환해야 하며, 메모리를 초기화하려면 `memset()` 함수를 이용해야 한다. 기본적으로는 쓰레기 값이 들어 있다.

```c
void free(void *memblock);
```
- 인자: 반환할 메모리 주소
- 반환값: 없음

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *pList = NULL, i = 0;

    // 12바이트 메모리를 동적할당
    pList = (int*)malloc(sizeof(int) * 3);

    pList[0] = 10;  // *(pList + 0) = 10;
    pList[1] = 20;  // *(pList + 1) = 20;
    pList[2] = 30;  // *(pList + 2) = 30;

    for (i = 0; i < 3; ++i)
        printf("%d\n", pList[i]);

    // 메모리 해제
    free(pList);
    return 0;
}
```
`malloc()` 함수의 반환 자료형은 `void *`이고 l-value인 `pList`의 자료형은 `int *`로 서로 다르다는 점입니다. 이 때문에 `void *`를 `int *`로 강제 형변환한 것입니다.

그리고 `void`는 길이도 해석방법도 없다는 의미입니다. 즉 포인터 것은 맞지만, 이 주소가 가리키는 대상 메모리를 어떤 형식(자료형)으로 해석할지는 아직 결정되지 않았음을 의미합니다. `void`형은 인스턴화가 허용되지 않습니다.

`free(pList);`를 통해 메모리 해제를 하지 않으면, 메모리가 사용할 수 없는 상태가 되는 **메모리 누수(memory leak)**가 발생합니다.

### 1. 메모리 초기화 및 사용(배열)

변수를 선언하면 즉시 0으로 초기화하는 것이 일반적입니다.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int *pList = NULL, *pNewList = NULL;

    // A. int형 3개 배열 선언 및 정의(0 초기화)
    int aList[3] = {0};

    // B. int형 3개를 담을 수 있는 크기의 메모리를 동적으로 할당한 후
    // 메모리를 모두 0으로 초기화
    pList = (int *)malloc(sizeof(int) * 3);
    memset(pList, 0, sizeof(int) * 3);

    // C. int형 3개를 담을 수 잇는 메모리를 0으로 초기화한 후 할당
    pNewList = (int *)calloc(3, sizeof(int) * 3);

    // 동적 할당 메모리 해제
    free(pList);
    free(pNewList);
    return 0;
}
```

```c
void *memset(void *dest, int c, size_t count);
```
- 인자
    - dest: 초기화 할 대상 메모리 주소
    - c: 초기값
    - count: 초기화 대상 메모리 바이트 단위 크기
- 반환값: 대상 메모리 주소
- 설명: 동적으로 할당받은 메모리에는 쓰레기 값이 있으므로 일반적으로 0으로 초기화하여 사용한다.

```c
void *calloc(size_t num, size_t size);
```
- 인자
    - num: 요소의 개수
    - size: 각 요소의 바이트 단위 크기
- 반환값: 힙 영역에 할당된 메모리 덩어리 중 첫 번째 바이트 메모리 주소
- 설명: `malloc()` 함수와 달리 할당받은 메모리를 0으로 초기화하여 전달한다.

의도적으로 12라는 숫자 대신 `sizeof` 연산자를 사용한 이유는 그냥 12바이트라고 하면 `char[12]`수도 있고, `int[3]`일 수도 있습니다. 그러나 `sizeof(int) * 3`이라고 쓰면 동적 할당된 메모리가 `int[3]`의 형식으로 사용될 가능성을 암시할 수 있습니다.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char szBuffer[] = {"Hello"};
    char *pszBuffer = "Hello";
    char *pszData = NULL;

    pszData = (char*)malloc(sizeof(char) * 6);
    pszData[0] = 'H';
    pszData[1] = 'e';
    pszData[2] = 'l';
    pszData[3] = 'l';
    pszData[4] = 'o';
    pszData[5] = '\0';

    puts(szBuffer);
    puts(pszBuffer);
    puts(pszData);
    return 0;
}
```
`szBuffer`는 스택 메모리의 초기값이 되지만, `pszBuffer`는 데이터 영역 중 읽기전용 영역 어딘가에 "Hello"라는 문자열이 저장되고 첫 글자인 'H'가 저장된 기준주소가 포인터의 초기값이 됩니다.

### 2. 메모리 복사

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char szBuffer[12] = {"HelloWorld"};
    char szNewBuffer[12] = {0};

    memcpy(szNewBuffer, szBuffer, 4);
    puts(szNewBuffer);

    memcpy(szNewBuffer, szBuffer, 6);
    puts(szNewBuffer);

    memcpy(szNewBuffer, szBuffer, sizeof(szBuffer));
    puts(szNewBuffer);

    return 0;
}
```
각 배열의 요소만큼 반복문을 수행하여 요소별로 일일이 단순 대입 연산을 수행해야 합니다. 그러나 `memcpy()` 함수를 사용하면 귀찮은 반복을 함수가 대신해줍니다.

```c
void *memcpy(void *dest, const void *src, size_t count);
```
- 인자
    - dest: 대상 메모리 주소
    - src: 복사할 원본 데이터가 저장된 메모리 주소
    - count: 복사할 메모리의 바이트 단위 크기
- 반환값: 대상 메모리 주소

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char szBuffer[12] = {"HelloWorld"};
    char *pszData = NULL;

    pszData = (char*)malloc(sizeof(char) * 12);
    pszData = szBuffer;
    puts(pszData);
    return 0;
}
```
위의 예제는 중대한 두 가지 오류가 있습니다. 첫 번째로 동적 할당한 메모리를 해제하지 않았다는 점이고, 두 번째는 `pszData = szBuffer`행이 수행되고 나면 배열에 담긴 내용이 동적 할당한 메모리로 복사되는 것이 아니라 `pszData` 포인터 변수에 `szBuffer`라는 메모리 주소만 단순 대입하여 덮어쓰게 됩니다. 더욱이 `pszData`에 본래 담겨있던 정보가 유실됨으로써 해제할 방법을 아예 잃게 됩니다.

단순히 주소 하나를 복사하는 것이 아니라 대상 메모리가 가진 내용을 **복사(deep copy)**해야 합니다. 깊은 복사(deep copy)의 핵심은 단지 대상을 가리키는 포인터가 늘어나는 것이 아니라 실제 대상이 여러 개로 복사되는 것을 뜻합니다. 반대로 지금 위의 코드처럼 포인터만 복사하는 것을 **얕은 복사(shallow copy)**라 합니다.

```c
char *strcpy(char *strDestination, const *strSource);
```
- 인자
    - strDestination: 문자열이 복사되어 저장될 메모리의 주소
    - strSource: 원본 문자열이 저장된 메모리 주소
- 반환값: strDestination 인자로 주어진 주소 반환

```c
char *strncpy(char *strDestination, const char *strSource, size_t count);
```
- 인자
    - strDestination: 문자열이 복사되어 저장될 메모리의 주소
    - strSource: 원본 문자열이 저장된 메모리 주소
    - count: 복사할 문자열의 길이
- 반환값: strDestination 인자로 주어진 주소 반환

`strcpy()` 함수는 `memcpy()` 함수와 거의 흡사한 함수로 두 메모리의 내용을 복사하는 기능을 수행합니다. 그러나 `strcpy()` 함수는 메모리 내용이 모두 문자열이라고 한정합니다. 또한 `strcpy()`는 보안결함이 있습니다. 그러므로 윈도우에서는 `strcpy_s()` 함수를 Unix, Linux에서는 `strncpy()`를 대체 함수로 사용할 수 있습니다.

### 3. 메모리 비교(`memcmp()`, `strcmp()`)

```c
int memcmp(const void *buf1, const void *buf2, size_t count);
```
- 인자
    - buf1: 원본 메모리 주소
    - buf2: 대상 메모리 주소
    - count: 비교할 메모리의 바이트 단위 크기
- 반환값
    - 0이면 두 값은 같음
    - 0보다 크면 buf1이 큼
    - 0보다 작으면 buf2가 큼

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char szBuffer[12] = {"TestString"};
    char *pszData = "TestString";

    printf("%d\n", memcmp("teststring", pszData, 10));
    printf("%d\n", memcmp("DataString", pszData, 10));
    return 0;
}
```
`memcmp()` 함수는 두 메모리에 저장된 정보를 일정 단위로 잘라서 감산 연산한 결과가 0인 동안 계속 반복합니다.

위의 예제에서 't'가 'T'보다 크기 ASCII 숫자상 더 큰 정수이기 때문에 0보다 큰 값이 출력됩니다. 그리고 첫번째 비교에서 다르다는 점이 확인되었으므로 나머지 9바이트에 대해서는 비교하지 않고 결과를 반환합니다.

```c
int strcmp(const char *string1, const char *string2);
```
- 인자
    - string1: 비교할 문자열이 저장된 메모리 주소
    - string2: 비교할 문자열이 저장된 메모리 주소
- 반환값
    - 0이면 두 값은 같음
    - 0보다 크면 string1이 큼
    - 0보다 작으면 string2가 큼

`strcmp()` 함수는 비교의 대상이 되는 정보를 '문자열'로 가정해서 처리합니다. `strncmp()` 함수를 이용하면 문자열의 앞에서 일정 길이만 비교할 수도 있습니다.

### 4. 문자열 검색

```c
char *strstr(const char *string, const char *strCharSet);
```
- 인자
    - string: 검색 대상이 될 문자열이 저장된 메모리 주소
    - strCharSet: 검색할 문자열이 저장된 메모리 주소
- 반환값
    - 문자열을 찾으면 해당 문자열이 저장된 메모리 주소 반환, 찾지 못하면 `NULL` 반환

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char szBuffer[32] = {"I am a boy"};

    // 배열 주소 출력
    printf("%p\n", szBuffer);
    printf("%p\n", strstr(szBuffer, "am"));
    printf("%p\n", strstr(szBuffer, "boy"));

    // 인덱스 출력
    printf("Index: %d\n", strstr(szBuffer, "am") - szBuffer);
    printf("Index: %d\n", strstr(szBuffer, "boy") - szBuffer);
    return 0;
}
```

### 5. 배열 연산자 풀어쓰기

`*(기준주소 + 인덱스)`나 `기준주소[인덱스]`나 같은 의미입니다.

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char szBuffer[32] = {"You are a girl"};

    printf("%c\n", szBuffer[5]);
    printf("%c\n", *(szBuffer + 5));

    printf("%s\n", &szBuffer[4]);
    printf("%s\n", &*(szBuffer + 4));
    printf("%s\n", szBuffer + 4);
    return 0;
}
```
`printf()` 함수는 `%s`와 대응된 인수를 **메모리의 주소**로 보고 거기서 한 글자씩 0이 나올 때까지 읽어와 하나의 완성된 문자열로 출력합니다.

### 6. `realloc()`, `sprintf()` 함수

```c
void *realloc(void *memblock, size_t size);
```
- 인자
    - memblock: 기존 동적 할당된 메모리 주소, 이 주소가 `NULL`이면 `malloc()` 함수와 동일하게 동작
    - size: 다시 할당받을 메모리 바이트 단위 크기
- 반환값: 다시 할당된 메모리 덩어리 중 첫 번째 바이트의 메모리 주소, 실패하면 `NULL`을 반환하는데 이 경우 첫 번째 인자로 전달된 메모리를 수동으로 해제해야 함
- 설명: 이미 할당된 메모리 영역에서 크기를 조절할 수 있다면, 반환된 주소는 첫 번째 인자로 전달된 주소와 같다. 그러나 불가능하다면 기존의 메모리를 해제하고 새로운 영역에 다시 할당한 후, 새로 할당된 메모리 주소를 반환한다.

```c
int sprintf(char *buffer, const char *format [, argument] ...);
```
- 인자
    - buffer: 출력 문자열이 저장될 메모리 주소
    - format: 형식 문자열이 저장될 메모리 주소
    - [, argument]: 형식 문자열에 대응하는 가변 인자들
- 반환값: 출력된 문자열의 개수
- 설명: 형식 문자열에 맞추어 특정 메모리에 문자열을 저장하는 함수

`sprintf()` 함수는 `printf()` 함수와 거의 흡사합니다. 다만 문자열이 콘솔 화면에 출력되는 것이 아니라 특정 주소의 메모리에 출력됩니다.

```c
#include <stdio.h>
// #include <malloc.h>
#include <string.h>

int main(void)
{
    char *pszBuffer = NULL, *pszNewBuffer = NULL;

    pszBuffer = (char*)malloc(12);
    sprintf(pszBuffer, "%s", "TestString");
    printf("[%p] %d %s\n", pszBuffer, _msize(pszBuffer), pszBuffer);

    pszNewBuffer = (char*)realloc(pszBuffer, 32);
    if (pszNewBuffer == NULL)
        free(pszBuffer);
    sprintf(pszNewBuffer, "%s", "TestStringData");
    printf("[%p] %d %s\n", pszNewBuffer, _msize(pszNewBuffer), pszNewBuffer);
    free(pszNewBuffer);
    return 0;
}
```
확장에 실패하면 `realloc()` 함수는 다른 주소를 반환합니다. 다른 주소를 반환할 경우 첫 번째 인수로 전달된 메모리를 해제하고 새 주소를 반환합니다. 그러나 `realloc()` 함수가 아예 실패할 경우 `NULL`을 반환하며, 첫 번째 인수로 전달된 메모리를 해제해주지 않습니다.

## 잘못된 메모리 접근

문자열이 깨졌을 경우 가장 흔한 실수는 메모리의 경계를 넘긴 입/출력을 수행했거나 자신에게 할당된 메모리가 아닌 전혀 엉뚱한 메모리에 대해 입/출력을 수행한 경우입니다.

## 포인터의 배열과 다중 포인터

포인터가 어려운 이유는 포인터 그 자체도 '변수'라는 사실 때문입니다. 변수는 메모리이고 메모리는 주소가 부여되어 있습니다. 포인터는 **변수 자체의 주소**와 **변수에 저장된 주소**, 두 개의 주소가 공존합니다.

- 일반변수 이름: 주소 + 값
- 포인터 이름: 주소 + 주소

다중 포인터는 포인터가 가리키는 것이 포인터 변수입니다. `int`형 변수에 대한 포인터는 `int *`로 기술하며, `int *` 변수에 대한 포인터는 `int **`로 기술합니다. 그리고 선언된 포인터 변수에 대해 간접지정연산을 수행한 결과는 포인터의 대상 자료형에서 `*` 하나를 지운것과 같습니다.

### 1. `char*`의 배열

### 2. 다중 포인터

### 3. 다차원 배열에 대한 포인터

## 변수와 메모리

### 1. 정적변수 `static`

### 2. 레지스터 변수 `register`
