# 파일 입출력

파일(file)은 보조기억장치에 저장되어 관리되는 정보의 단위입니다. 변수나 동적 할당한 메모리가 주기억장치를 사용하기 위한 요소라면 파일은 보조기억장치를 사용하기 위한 요소이며, **파일 시스템(file system)**이라고 부르는 별도의 관리 체계가 존재합니다.

보조기억장치는 주기억장치와 달리 용량문제에 매우 둔감합니다. 주기억장치나 보조기억장치나 같은 메모리지만 사용하는 방법이 그 속성만큼이나 서로 다릅니다.

## 파일 시스템 기본 이론

파일 시스템은 **파일 단위로 정보를 생성, 삭제, 저장, 검색할 수 있도록 정보를 구성하는 방법**을 말합니다. 이 정보에는 파일의 이름이나 위치 등에 대한 정보도 포함됩니다. 파일의 위치를 말할 때, **경로(path)**라는 말을 사용합니다.

### 1. 텍스트 파일과 바이너리 파일

파일은 크게 **텍스트 파일**과 **바이너리(binary) 파일**로 나눌 수 있습니다. 텍스트 파일은 파일에 저장된 정보가 모두 **ASCII 코드나 문자열로 해석할 수 있는 정보**들로만 구성된 파일을 말합니다. 텍스트 파일의 가장 중요한 특징 중 하나는 -1이라는 정수값을 '파일의 끝(EOF, End Of File)'으로 인식한다는 점입니다.

그리고 **텍스트 파일을 제외한 모든 파일들을 바이너리 파일**이라고 합니다.

### 2. `fopen()`, `flocse()` 함수

`fopen()` 함수는 특정 경로에 있는 파일을 열어서 접근할 수 있도록 `FILE` 구조체에 대한 주소를 반환하는 함수입니다. 사용이 끝나면 `fclose()` 함수로 닫아주어야 합니다.

```c
FILE *fopen(const char *filename, const char *mode);
```

- 인자
  - filename: 열고자 하는 대상 파일의 절대 경로 문자열
  - mode: 접근 모드를 명시한 문자열
- 반환값: `FILE` 구조체에 대한 주소 반환, 만일 에러가 발생하면 `NULL` 반환

```c
int fclose(FILE *stream);
```

- 인자: 닫을 파일에 대한 FILE 구조체의 주소
- 반환값: 함수가 성공하면 0을 반환하고 만일 에러가 발생하면 EOF 반환

```c
int _fcloseall(void);
```

- 인자: 없음
- 반환값: 닫은 파일의 개수
- 설명: 프로그램에서 열어둔 모든 파일을 닫는다.

```c
#include <stdio.h>

void main()
{
    // 파일 제어에 필요한 FILE 구조체에 대한 포인터 변수 선언 및 정의
    FILE *fp = NULL;
    // test.txt 파일을 쓰기 모드로 개방
    // 단, 같은 이름의 파일이 이미 존재하면 삭제하고 새 파일을 생성 (없다면 새로 생성)
    fp = fopen("Test.txt", "w");
    if (fp == NULL)
    {
        puts("ERROR: Failed to open file!");
        return;
    }

    // TODO: File I/O

    // 개방한 파일을 닫음
    fclose(fp);

}
```
위의 예제에서 생성할 파일의 이름만 명시하였는데 이는 상대 경로입니다. 따라서 `Test.txt`파일은 예제가 실행될 때 **현재 경로로 설정된 위치에 생성**됩니다.

#### 파일 접근 제어

만일 어떤 프로그램(혹은 시스템)이 이미 파일을 열어 두었다면, 접근이 제한될 수 있습니다. 이는 파일에 저장된 정보가 여러 프로그램에 의해 동시에 편집되어 엉키는 일이 발생하지 않도록 하기 위함입니다. 그러므로 파일을 다룰 때는 반드시 **접근 제어** 문제에 대해서 생각해야 하며, 다음 같은 사항들에 주의해야 합니다.

- 파일에 접근하려면 우선 파일을 개방해야 하며, 파일에 대한 입출력을 완료한 후에는 파일을 닫아야 한다.
- 파일을 개방할 때는 반드시 목적(입출력 혹은 수정)을 명시해야 한다.
- 파일이 이미 사용 중인 경우(파일이 개방된 상태), 접근이 제한될 수 있다. 그러나 경우에 따라 읽기는 허용될 수도 있다.
- 만일 파일의 속성이 '읽기 전용'이면 쓰기모드 개방이 제한된다.
- 경우에 따라(특히, 보안상 권한 문제 때문에) 읽기조차 제한될 수 있다.

```c
#include <stdio.h>

void main()
{
    FILE *fp = NULL;
    int nClosed = 0;
    fopen("Test1.txt", "w");
    fopen("Test2.txt", "w");
    fopen("Test3.txt", "w");

    // 지금까지 개방한 파일들을 '모두' 닫는다.
    nClosed = _fcloseall();
    printf("%d\n", nClosed);
}
```
파일이 개방된 상태에서 닫지 않고 프로그램이 종료되면, 특별한 일이 없는 한 운영체제 모든 파일을 닫아버립니다. 그러나 될 수 있으면 파일을 개방하고 닫는 일은 개발자 스스로 처리하는 것이 바람직합니다.

참고로 파일을 운영체제가 닫는 것과 관련해 '특별 한 일'이라는 것은 운영체제의 커널(kernel) 영역에서 특정 파일을 붙들고 놔주지 않는 경우입니다. 이런 경우는 보동 비동기 파일 입출력을 시도했을 때 발생합니다. 이에 대한 자세한 이론들은 시스템 프로그래밍을 배 울 때 알 수 있습니다.

## 텍스트 파일 입출력

파일 입출력은 표준 입출력처럼 전용 함수를 이용합니다.

### 1. `fprintf()`, `fscanf()` 함수

```c
int fprintf(FILE *stream, const char *format [, argument]...);
```

- 인자
  - stream: `FILE` 구조체에 대한 포인터
  - format: 형식 문자열이 저장된 메모리 주소
  - [, argument]: 형식 문자열에 대응하는 가변 인자들
- 반환값: 출력된 바이트 수

```c
#include <stdio.h>
#include <stdlib.h>

void main()
{
    FILE *fp = NULL;
    // 현재 경로에 Test.txt 파일을 생성
    fp = fopen("Test.txt", "w");

    // 생성한 파일에 문자열을 출력
    fprintf(fp, "%s\n", "Test string");
    fprintf(fp, "%s\n", "Hello world!");

    // 파일을 닫고 메모장으로 확인
    fclose(fp);
    system("notepad.exe Test.txt");
}
```

```c
int fscanf(FILE *stream, const char *format [, argument ]...);
```

- 인자
  - stream: `FILE` 구조체에 대한 포인터
  - format: 형식 문자열이 저장된 메모리 주소
  - [, argument]: 형식 문자열에 대응하는 가변 인자들
- 반환값: 성공적으로 읽어 들인 항목(field)의 개수

```c
#include <stdio.h>
#include <stdlib.h>

void main()
{
    int nData = 0;
    char szBuffer[128] = {0};
    FILE *fp = NULL;

    fp = fopen("fscanfTest.txt", "w");
    fprintf(fp, "%d,%s\n", 20, "Test");
    fclose(fp);

    // 파일을 열고 저장된 내용을 읽어 온다.
    fp = fopen("fscanfTest.txt", "r");
    fscanf(fp, "%d,%s", &nData, szBuffer);
    fclose(fp);

    // 읽어온 내용을 화면에 출력
    printf("%d, %s\n", nData, szBuffer);
}
```

`fscanf()` 함수를 호출할 때 `%s` 형식으로 문자열을 읽더라도 빈칸까지만 읽어내기 때문에 단어 하나를 읽는 것은 문제없으나 문장 전체를 읽어 들이고자 하는 경우 `fgets()` 함수를 사용하여 한 행의 문자열을 모두 읽어온 후 문자열을 분석하여 원하는 정보를 뽑아내는 것이 좋습니다.

### 2. `fgetc()`, `fputc()` 함수

```c
int fgetc(char *stream);
```

- 인자: `FILE` 구조체에 대한 포인터
- 반환값: 정상적인 경우 파일에서 읽은 문자 반환, 에러가 발생하면 EOF 반환

```c
int fputc(int c, FILE *stream);
```

- 인자
  - c: 파일에 쓸 문자
  - stream: `FILE` 구조체에 대한 포인터
- 반환값: 정상적인 경우 파일에 쓴 문자 반환, 에러가 발생하면 EOF 반환

`fgetc()`, `fputc()` 함수는 각각 파일에서 한 문자를 읽어오고 쓰는 함수입니다.

```c
#include <stdio.h>

void main()
{
    FILE *fp = NULL;
    char ch;

    fp = fopen("test.txt", "w");
    fputs("Test string!", fp);
    fclose(fp);

    fp = fopen("test.txt", "r");
    if (fp == NULL)
        return;

    // 파일에서 한글자씩 읽어와 다시 한 글자씩 출력
    while ((ch = fgetc(fp)) != EOF)
        putchar(ch);
    fclose(fp);
}
```

`EOF` 상수는 -1인데 이는 파일의 끝을 의미합니다.

### 3. `fgets()`, `fgets_s()`, `fputs()` 함수

```c
char *fgets(char *string, int n, FILE *stream);
```

- 인자
  - string: 읽어 들인 문자열이 저장될 버퍼의 주소
  - n: 입력 버퍼의 바이트 단위 크기
  - stream: `FILE` 구조체에 대한 포인터
- 반환값: 정상적인 경우 `string` 인자로 전달된 주소 반환, 에러가 발생하면 `NULL` 반환

`fgets()` 함수는 파일에서 한 행의 문자열을 읽어오는 함수입니다.

```c
#include <stdio.h>
#include <string.h>

void main()
{
    FILE *fp = NULL;
    char szBuffer[512] = {0};

    fp = fopen("Test.txt", "w");
    fputs("Test\n", fp);
    fputs("String\n", fp);
    fputs("Data\n", fp);
    fclose(fp);

    fp = fopen("Test.txt", "r");
    if (fp == NULL)
        return;

    // 파일에서 '한 행'씩 끊어내서 읽어온다.
    while (fgets(szBuffer, sizeof(szBuffer), fp))
    {
        printf("%s", szBuffer);
        memset(szBuffer, 0, sizeof(szBuffer));
    }
    fclose(fp);
}
```

```c
int fputs(const char *string, FILE *stream);
```

- 인자
  - string: 출력할 문자열이 저장될 기억공간의 주소
  - stream: `FILE` 구조체에 대한 포인터
- 반환값: 정상적인 경우 음수가 아닌 값을 반환, 에러가 발생한 경우에는 EOF 반환

### 4. `fflush()` 함수

```c
int fflush(FILE *stream)
```

- 인자: `FILE` 구조체에 대한 포인터
- 반환값: 성공하면 0, 실패하면 EOF 반환

`fflush()` 함수는 특정파일에 대한 입출력 정보를 초기화하는 함수입니다. `scanf()` 함수나 `gets()` 함수를 이용하여 표준입력장치로 정보를 입력받을 때, 개행 문자가 입출력 버퍼에 남아서 오류가 발생하는 경우가 있을 때, 문제를 해결하기 위해서 `fflush()` 함수를 사용했습니다.

일반적으로 `fflush()` 함수는 출력 스트림을 플러싱(flushing)하는 기능만 제공한다고 봐야합니다. 그리고 '입출력 정보의 초기화'라는 것은 단지 '카운터'값을 초기화하는 것에 불과합니다.

```c
#include <stdio.h>


void main()
{
    // 표준입력장치 파일(stdin)을 가리키는 포인터 변수 선언 및 정의
    FILE *fp = stdin;
    printf("Input string: ");

    // 사용자로부터 '문자열'을 입력받은 후 첫 글자를 읽어와 출력
    printf("getchar() - %c\n", getchar());

    // 버퍼에 남아있는 문자의 개수와 내용에 대한 정보를 출력
    printf("[%d] %s", fp->_cnt, fp->_base);
    printf("READ: %d\n", fp->_ptr - fp->_base);

    // 다시 한 글자를 읽어온 후 달라진 내용 확인
    printf("\n\ngetchar() - %c\n", getchar());
    printf("[%d] %s", fp->_cnt, fp->_base);
    printf("READ: %d\n", fp->_ptr - fp->_base);

    // 파일 입출력 버퍼를 초기화한 후 결과 확인
    fflush(fp);
    printf("\n\nAfter flushing\n[%d] %s",
        fp->_cnt, fp->_base);
    printf("READ: %d\n", fp->_ptr - fp->_base);
}
```

```shell
Input string: TestData
getchar() - T
[8] TestData

READ: 1

getchar() - e
[7] TestData

READ: 2

After flushing
[0] TestData

READ: 0
```

`FILE` 구조체의 `_cnt` 멤버는 파일의 입출력 버퍼에서 읽어올 수 있는 남은 문자의 개수입니다. `_base` 멤버는 파일의 입출력 버퍼의 시작 주소이며, `_ptr` 멤버는 읽어올 문자가 저장된 메모리 주소입니다.

## 바이너리 파일 입출력

바이너리 파일(binary file)은 텍스트 파일을 제외한 모든 파일입니다. 파일을 바이너리 모드로 개방할 때는 **접근 모드 문자열에 반드시 `b`를 포함**해야 합니다.


### 1. `fread()`, `fwrite()` 함수

`fread()`와 `fwrite()` 함수는 `fgets()`와 `fputs()` 함수와 달리 입출력의 길이가 일정한 메모리 덩어리입니다. 바이너리 모드로 파일 입출력을 시도할 때는 **정해진 길이**만큼 읽고 써야 합니다.

```c
size_t fread(void *buffer, size_t size, size_t count, FILE *stream);
```

- 인자
  - buffer: 파일에서 읽어 들인 내용을 저장할 버퍼의 주소
  - size: 한 번에 읽을 메모리 블록의 크기
  - count: 읽어 들일 메모리 블록의 수
  - stream: `FILE` 구조체에 대한 포인터
- 반환값: 함수가 성공하면 파일에서 읽어 들인 메모리 블록의 수를 반환


```c
size_t fwrite(const void *buffer, size_t size, szie_t count, FILE *stream);
```

- 인자
  - buffer: 파일에 쓸 내용이 저장된 버퍼의 주소
  - size: 한 번에 쓰고자 하는 메모리 블록의 크기
  - count: 쓰고자 하는 메모리 블록의 수
  - stream: `FILE` 구조체에 대한 포인터
- 반환값: 쓰기에 성공한 메모리 블록의 수를 반환

한 사람에 대한 정보로 이름과 전화번호가 있다고 가정할 때, 이를 문자열로 처리하여 행 단위로 저장할 수도 있지만 이 예제처럼 구조체 덩어리를 통째로 저장할 수도 있습니다. 물론 문자열로 저장하는 방법에 비해 메모리 낭비가 발생한다는 단점이 있으나 처리 속도가 빠르고 개발이 훨씬 편리해질 수 있는 장점이 있습니다.

```c
#include <stdio.h>

typedef struct _USERDATA
{
    char szName[16];
    char szPhone[16];
} USERDATA;

void main()
{
    FILE *fp = NULL;
    USERDATA UserData = {"Ho-sung", "123-1234"};

    // 바이너리 쓰기 모드로 파일을 생성
    fp = fopen("Test.dat", "wb");
    if (fp == NULL) return;

    // 구조체를 한 번에 바이너리모드로 파일에 쓴다.
    fwrite(&UserData, sizeof(USERDATA), 1, fp);
    fclose(fp);
}
```

```c
#include <stdio.h>

typedef struct _USERDATA
{
    char szName[16];
    char szPhone[16];
} USERDATA;

void main()
{
    FILE *fp = NULL;
    USERDATA UserData = {0};

    // 바이너리 읽기 모드로 파일 열기
    fp = fopen("Test.dat", "rb");
    if (fp == NULL) return;

    // 파일에서 바이너리 모드로 구조체를 한 번에 읽고 출력
    fread(&UserData, sizeof(USERDATA), 1, fp);
    puts(UserData.szName);
    puts(UserData.szPhone);
    fclose(fp);
}
```

`fread()` 함수가 반환하는 값이 무엇인가입니다. 파일에서 `USERDATA` 구조체의 길이만큼의 메모리를 1회 읽는 데 성공했다면 반환하는 값은 1입니다. 읽어 들일 수 있는 정보의 길이가 `USERDATA` 구조체의 길이보다 작다면 이 함수는 실패하여 0을 반환합니다.

### 2. `fseek()`, `rewind()`, `ftell()` 함수

파일은 논리적으로 봤을 때, 마치 배열처럼 하나로 이어진 선형 메모리라고 할 수 있습니다. 그러나 배열과 달리 파일의 길이가 늘어날 수 있습니다. 파일을 처음 생성했을 때는 길이가 0이지만 파일에 정보를 쓰면 그만큼 파일의 길이는 자동으로 늘어납니다. 쓰기가 거듭되어 파일의 최대 길이를 넘어서면 자동으로 증가하여 정보를 저장합니다.

그리고 중요한 것은 실제 **파일 입출력이 완료된 위치를 저장하고 있는 포인터**가 존재하는데 이것을 **파일 입출력 포인터**라고 합니다. 파일 입출력 포인터는 파일에 입출력이 발생하는 위치를 의미합니다.

```c
int fseek(FILE *stream, long offset, int origin);
```

- 인자
  - stream: `FILE` 구조체에 대한 포인터
  - offset: 기준 위치에 대한 바이트 단위 오프셋
  - origin: 기준 위치(SEEK_SET: 처음, SEEK_CUR: 현재, SEEK_END: 끝)
- 반환값: 성공하면 0을 반환하며, 실패하면 음수를 반환
- 설명: 특정 위치로 파일 포인터를 이동

```c
long ftell(FILE *stream);
```

- 인자: `FILE` 구조체에 대한 포인터
- 반환값: 성공하면 파일 포인터의 현재 위치(0 이상)를 반환, 실패하면 -1L 반환
- 설명: 파일 포인터의 위치를 알아내는 함수이며, 이를 이용하여 파일의 크기를 계산

`fopen()` 함수로 파일을 열면 파일 입출력 포인터는 최초 맨 앞(0번)에 위치합니다. 그러나 `fseek()` 함수를 이용하여 파일 입출력 포인터를 강제로 맨 끝으로 이동시킬 수 있습니다. 그리고 이어서 `ftell()` 함수를 호출하여 현재 위치를 알아내는 방법으로 파일의 크기를 알아 낼 수 있습니다.

```c
#include <stdio.h>

void main()
{
    FILE *fp = NULL;
    // 바이너리 읽기 모드로 열기
    fp = fopen("Test.dat", "rb");

    // 파일 입출력 포인터를 파일의 끝으로 이동
    fseek(fp, 0, SEEK_END);
    // 파일 크기
    printf("size of Test.dat: %u\n", ftell(fp));
    fclose(fp);
}
```

`rewind()` 함수는 파일 포인터가 현재 어디에 있든지 상관없이 **맨 앞으로 강제로 이동**시키는 함수입니다. 

```c
void rewind(FILE *stream);
```

- 인자: `FILE` 구조체에 대한 포인터
- 반환값: 없음

### 3. 기타 알아 두면 좋은 함수

- `feof()`: 파일 포인터가 맨 끝에 있는지 확인하는 함수
- `_access()`: 특정 파일이 존재하는지, 그렇다면 읽기/쓰기 전용 모드인지 확인 (리눅스에서는 `access()` 사용)

```c
int feof(FILE *stream);
```

- 인자: `FILE` 구조체에 대한 포인터
- 반환값: 파일 포인터가 끝에 있는 것이 아니면 0 반환

```c
int _access(const char *path, int mode);
```

- 인자
  - path: 접근 검사를 할 파일이 저장된 경로가 저장된 메모리에 대한 포인터
  - mode: 접근 검사 값(00: 파일 존재 유무만 확인, 02: 쓰기 전용 모드인지 확인, 04: 읽기 전용 모드인지 확인, 06: 읽기/쓰기 모두 가능한지 확인)
- 반환값: 0을 반환하면 파일에 대한 mode 인자로 전달된 접근 허용, -1을 반환하면 파일이 존재하지 않거나 접근할 수 없음을 의미
- 설명: 이 함수는 ANSI 함수가 아니라는 사실에 주의

## 연습문제

[문제 01](../code/14/01.c)
