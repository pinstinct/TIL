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
