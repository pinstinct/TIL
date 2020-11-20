# 구조체와 공용체

구조체는 다양한 기본 자료형을 가진 요소들을 모아 새로운 자료형으로 만든 것입니다.

구조체와 배열의 공통점은 여러 개가 모여 새로운 하나가 되었다는 점입니다. 그러나 배열은 같은 것이 여러개 보여 한 덩어리를 이룬 것이고, 구조체는 서로 다른(같을 수도 있음) 것들이 여러개 모여 전혀 새로운 한 덩어리를 이룬 것이라는 점에서 다릅니다.

그리고 배열은 배열을 이루고 있는 각각을 요소라고 부르고 구조체는 **멤버**라고 부릅니다. 공용체도 구조체처럼 멤버들이 모여 하나를 이룹니다. 그런데 구조체와는 달리 한 자료에 대해 해석방법만 여러 가지를 부여한 것입니다.

## 구조체

'구조체 선언'에 의해 새로운 자료형이 만들어집니다. 그래서 구조체나 공용체 같은 것을 **사용자 정의 자료형**이라고도 합니다. **구조체 선언은 말 그대로 선언**에 불과한 것입니다. 단순한 자료구조의 설계지 절대 변수 정의가 아닙니다.

구조체는 넓은 의미에서 자료구조입니다. 예를 들어 학생 개인의 신상 정보를 관리하는 프로그램을 제작해야 한다면 특정 개인에 대한 각종 정보를 한 덩어리로 묶어서 관리해야 할 것입니다. 이렇게 묶은 한 덩어리를 **레코드(record)**라 하고 레코드의 내부를 구성하는 요소들을 **필드(field)**라고 합니다. 이 중에서 **레코드를 코드로 기술하기 가장 적절한 것이 구조체**입니다.

### 1. 구조체 선언 및 정의

```c
#include <stdio.h>
#include <string.h>

// 구조체 선언
struct USERDATA
{
    int nAge;
    char szName[32];
    char szPhone[32];
};

int main(void)
{
    // USERDATA 구조체 변수 user 선언 및 정의
    struct USERDATA user = {0, "", ""};

    // 구조체 멤버 접근 및 값 채우기
    user.nAge = 10;
    strcpy(user.szName, "Hoon");
    strcpy(user.szPhone, "010-1234-1234");

    // 구조체 멤버 접근 및 출력
    printf("%d살, %s, %s\n", user.nAge, user.szName, user.szPhone);
    return 0;
}
```

#### `typedef`를 이용한 형 재선언

구조체 변수 인스턴스를 선언 및 정의하려면 자료형에 해당하는 구조체 이름 앞에 반드시 `struct` 예약어를 붙여야 합니다. 그러나 구조체 변수를 선언할 때 매번 `struct` 예약어를 기술하는 일은 귀찮은 일입니다. 그래서 대부분 구조체를 선언 할 때 `typedef` **예약어를 이용해 형 재선언을 포함하는 것이 일반적**입니다.

```c
#include <stdio.h>
#include <string.h>

// 구조체 선언 및 형 재선언
typedef struct USERDATA
{
    int nAge;
    char szName[32];
    char szPhone[32];
} USERDATA;

int main(void)
{
    // 형 재선언 덕분에 struct 생략 가능
    USERDATA user = {0, "", ""};

    // 구조체 멤버 접근 및 값 채우기
    user.nAge = 10;
    strcpy(user.szName, "Hoon");
    strcpy(user.szPhone, "010-1234-1234");

    // 구조체 멤버 접근 및 출력
    printf("%d살, %s, %s\n", user.nAge, user.szName, user.szPhone);
    return 0;
}
```

#### 구조체 배열

보통 입문자가 신상관리 프로그램을 작성할 때 '단일 연결 리스트(single linked list)'라는 구조를 이용합니다. 다룰 수 있는 레코드의 개수에 영향을 받지 않게 하기 위합니다. 하지만 그에 앞서 (확장성은 떨어지더라도) 구조체의 배열을 이용해 간단히 관리 프로그램을 만들기도 합니다.

```c
#include <stdio.h>
#include <string.h>

// 구조체 선언 및 형 재선언
typedef struct USERDATA
{
    int nAge;
    char szName[32];
    char szPhone[32];
} USERDATA;

int main(void)
{
    // USERDATA 구조체 변수 user 선언 및 정의
    USERDATA userList[4] = {
        {10, "kim", "1234"},
        {11, "jung", "2345"},
        {17, "ju", "3456"},
        {12, "lim", "4567"}
    };
    int i = 0;

    // 배열 연산으로 각 USERDATA 인스턴스 멤버 값을 출력
    for (i = 0; i < 4; ++i)
        printf("%d살\t%s\t%s\n",
        userList[i].nAge,
        userList[i].szName,
        userList[i].szPhone);
    return 0;
}
```

### 2. 구조체 동적 할당

구조체는 사용자가 그 구조를 설계한 자료형입니다. 따라서 **메모리를 해석하는 방법**이라고 봐야 합니다. 구조체를 자동변수 형태로 선언 및 정의할 수도 있고 전역변수로 선언하는 것도 가능합니다. 물론 `malloc()` 함수를 이용해 동적 할당하는 것도 가능합니다.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct USERDATA
{
    int nAge;
    char szName[32];
    char szPhone[32];
} USERDATA;

int main(void)
{
    // USERDATA 구조체에 대한 포인터 변수 선언 및 정의
    USERDATA *pUser = NULL;

    // USERDATA 구조체가 저장될 수 있을 수 있는 크기의 메모리 동적 할당
    pUser = (USERDATA*)malloc(sizeof(USERDATA));

    // 포인터 이므로 '.'이 아니라 '->' 연산자로 멤버에 접근
    pUser->nAge = 10;
    strcpy(pUser->szName, "Hoon");
    strcpy(pUser->szPhone, "9876");

    printf("%d살\t%s\t%s\n",
    pUser->nAge,
    pUser->szName,
    pUser->szPhone);

    // 동적 할당한 메모리 해제
    free(pUser);
    return 0;
}
```

### 3. 반환자료, 매개변수 구조체

구조체도 함수의 반환 자료형이나 매개변수가 될 수 있습니다.

```c
#include <stdio.h>

// 구조체 선언 및 형 재선언
typedef struct USERDATA
{
    int nAge;
    char szName[32];
    char szPhone[32];
} USERDATA;

// 구조체 형식을 반환하는 함수 선언 및 정의
USERDATA GetUserData(void)
{
    USERDATA user = {0};
    // %*c는 '\n'을 제거하기 위함
    scanf("%d%*c", &user.nAge);
    gets(user.szName);
    gets(user.szPhone);
    return user;
}

int main(void)
{
    USERDATA user = {0};

    // 함수가 반환한 구조체를 저장하고 출력
    user = GetUserData();

    printf("%d살\t%s\t%s\n",
    user.nAge,
    user.szName,
    user.szPhone);

    return 0;
}
```
그런데 이와 같이 **구조체 변수를 매개변수나 반환 자료형식으로 사용하는 것은 비효울**적입니다. 복사해야 할 정보의 양이 기본 자료형에 비해 크기 때문입니다. 그렇기 때문에 **구조체가 매개 변수나 반환형이 될 때는 Call by reference 형식으로 처리**하는 것이 좋습니다. 위의 예제에서 선언 및 정의 된 `USERDATA` 구조체 변수(`USERDATA user = {0};`)의 개수는 모두 두 개입니다. 그런데 다음과 같이 코드를 변경한다면 하나를 제거할 수 있습니다.

```c
#include <stdio.h>

typedef struct USERDATA
{
    int nAge;
    char szName[32];
    char szPhone[32];
} USERDATA;

// 구조체 인스턴스가 아니라 구조체에 대한 '포인터'를 매개변수로 받는다.
USERDATA GetUserData(USERDATA *pUser)
{
    scanf("%d%*c", &pUser->nAge);
    gets(pUser->szName);
    gets(pUser->szPhone);
}

int main(void)
{
    USERDATA user = {0};

    // Call by reference로 변경
    GetUserData(&user);

    printf("%d살\t%s\t%s\n",
    user.nAge,
    user.szName,
    user.szPhone);

    return 0;
}
```

구조체는 선언하기에 따라 그 크기가 달라질 수 있습니다. 그런데 덩치가 큰 구조체를 주소로 넘기지 않고 일반 변수처럼 Call by value 형식으로 처리하면 스택을 많이 사용하는 코드가 되어버립니다. 게다가 함수 호출과정에서 메모리를 계속해 복사하는 연산도 수행해야 합니다. 아무래도 효율이 떨어질 수 밖에 없습니다.

그러므로 **구조체를 함수의 인수로 전달할 때는 Call by reference 방식을 사용하는 것이 현명**합니다.

### 4. 구조체를 멤버로 가지는 구조체

```c
#include <stdio.h>

// MYBODY 구조체 선언 및 형 재선언
typedef struct MYBODY
{
    int nHeight;
    int nWeight;
} MYBODY;

// MYBODY 구조체를 멤버로 가지는 USERDATA 구조체 선언
typedef struct USERDATA
{
    char szName[32];
    char szPhone[32];
    MYBODY body;
} USERDATA;

int main(void)
{
    USERDATA user = {
        "Hoon",
        "1234",
        {175, 70}  // MYBODY 구조체 멤버 초기화
    };
    printf("%s\t%s\t%d\t%d\n",
    user.szName, user.szPhone,
    // 멤버 접근 연산을 두 번 함
    user.body.nHeight, user.body.nWeight);
    return 0;
}
```

#### 자기 참조 구조체

구조체의 멤버로 구조체에 대한 포인터 변수를 선언할 수도 있습니다. 그 포인터가 가리키는 대상이 바로 자기 자신이면 **자기 참조 구조체**라고 부릅니다.

참고로 연결 리스트에서 링크(연결)되어야 할 대상을 **노드(node)**라고 부르는데, 이 노드를 기술하는 문법이 바로 자기 참조 구조체입니다.

```c
#include <stdio.h>

// USERDATA 구조체 선언 및 형 재선언
typedef struct USERDATA
{
    char szName[32];
    char szPhone[32];
    // USERDATA 구조체를 가리킬 수 있는 포인터를 멤버로 선언
    struct USERDATA *pNext;
} USERDATA;

int main(void)
{
    // 두 개의 USERDATA 구조체 인스턴스 선언 및 정의
    USERDATA user = {"kim", "1234", NULL};
    USERDATA newUser = {"jung", "2345", NULL};

    // pNext 멤버를 이용해 두 인스턴스를 연결
    user.pNext = &newUser;

    printf("%s, %s\n", user.szName, user.szPhone);
    // pNext 멤버를 이용해 구조상 다음 인스턴스에 접근
    printf("%s, %s\n", user.pNext->szName, user.pNext->szPhone);
    return 0;
}
```
`user.pNext = &newUser;` 코드를 실행함으로써 두 구조체 변수(노드)는 논리적으로 연결됩니다. `user.pNext->szName`처럼 `user`의 `pNext` 멤버를 통해 '다음노드'에 접근할 수 있고, 다시 구조체의 멤버접근 연산을 통해 다음 노드의 멤버까지도 접근할 수 있습니다.

아래는 좀 더 실제 연결 리스트에 가까운 예제입니다. 배열로 선언된 네 개의 USERDATA 구조체 변수들을 **단일 연결 리스트** 형태로 묶고 리스트를 구성하고 있는 전체 노드를 반복문을 이용해 접근하는 방법을 보인 예제입니다.

```c
#include <stdio.h>

// 자기참조 구조체 선언
typedef struct USERDATA
{
    char szName[32];
    char szPhone[32];
    struct USERDATA *pNext;
} USERDATA;

int main(void)
{
    // 배열로 USERDATA 구조체 인스턴스 선언 및 정의
    USERDATA userList[4] = {
        {"kim", "1234", NULL},
        {"jung", "2345", NULL},
        {"ju", "3456", NULL},
        {"lim", "4567", NULL}
    };
    // 연결 리스트의 첫 번째 인스턴의 주소를 저장할 포인터
    USERDATA *pUser = NULL;

    // pNuext 멤버를 배열의 순서상 다음 구조체 인스턴스의 주소로 정의
    userList[0].pNext = &userList[1];
    userList[1].pNext = &userList[2];
    userList[2].pNext = &userList[3];
    userList[3].pNext = NULL;  // 마지막 인스턴스는 뒤에 아무것도 없으므로 NULL로 초기화

    // 연결된 리스트의 첫 번째 인스턴스를 가리키도록 포인터 정의
    pUser = &userList[0];
    while (pUser != NULL)
    {
        // 포인터가 가리키는 인스턴스의 멤버를 출력
        printf("%s, %s\n", pUser->szName, pUser->szPhone);
        // 현재 가리키고 있는 인스턴스의 다음 인스턴스를 가리키도록
        // 포인터를 다음으로 '이동'
        pUser = pUser->pNext;
    }
    return 0;
}
```
`pUser = pUser->pNext;` 코드가 수행되면 `pUser`가 가리키는 대상이 다음 노드로 변경됩니다. 그리고 마지막 노드를 지나면서 `NULL`에 이릅니다.

나중에 연결리스트에 대해 배울 때는 노드의 개수를 지금 예제처럼 배열로 정해놓고 시작하는 것이 아니라 **메모리를 동적 할당하는 방식**으로 계속 리스트에 추가할 수 있도록 코드를 작성합니다.

### 5. 구조체 멤버 맞춤

```c
#include <stdio.h>

typedef struct USERDATA
{
    char ch;
    int nAge;
} USERDATA;

typedef struct MYDATA
{
    char ch;
    int nAge;
    double dData;
} MYDATA;

int main(void)
{
    printf("%d\n", sizeof(USERDATA));
    printf("%d\n", sizeof(MYDATA));
    return 0;
}
```
실행결과로 5와 13을 예상했겠지만, 결과는 8과 16입니다. 이런 형상이 벌어진 이유는 **구조체 멤버 맞춤(structure member alignment)** 때문입니다. 배열은 각 요소가 연접하여 붙어있습니다. 그러나 구조체는 연접할 수도 있고 그렇지 않을 수도 있습니다. 즉 두 멤버 사이에 일정 크기의 공백기 껴들어 갈 수 있습니다.

**구조체 멤버 맞춤(struct member alignment)에 대한 Visual Stdio의 기본설정은 8바이트(64비트)** 입니다. 그런 것이 있다는 것만 알고 변경하지 않는 것이 좋습니다.

프로그램을 개발하다 보면, 이 구조체들의 멤버 구성을 어떻게 했건 상관없이 모든 멤버가 연접하도록 해야 할 때가 있습니다. 이럴 때는 구조체 멤버 맞춤을 1바이트 단위로 수정하면 됩니다. 다음 예제와 같이 `#pragma pack` 전처기를 이용하면 특정 구조체만 멤버를 1바이트로 맞출 수 있습니다.

```c
#include <stdio.h>

#pragma pack(push, 1)
typedef struct USERDATA
{
    char ch;
    int nAge;
} USERDATA;

typedef struct MYDATA
{
    char ch;
    int nAge;
    double dData;
} MYDATA;
#pragma pack(pop)

int main(void)
{
    printf("%d\n", sizeof(USERDATA));
    printf("%d\n", sizeof(MYDATA));
    return 0;
}
```
구조체를 통째로
- 파일에 저장하거나 읽어오는 경우
- 네트워크로 전송하거나 수신하는 경우

멤버 맞춤에 의한 오류가 발생할 가능성은 없는지 반드시 확인해야 합니다.

## 비트필드

비트필드(bit field)는 구조체 멤버가 바이트 단위가 아닌 **비트 단위 데이터를 다루는 멤버**로 선언되는 구조체입니다.