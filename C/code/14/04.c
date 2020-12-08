#include <stdio.h>

#define COPYSIZE 1024*4  //한번에 복사할 데이터양 4KB
#define CHKSIZE  1024*1024*100  //100MB

/*
main() 함수의 인자로 두 바이너리 파일의 경로를 입력받아 바이너리 모드로 열고, (./04 /org.txt /dst.txt)
원본 파일의 내용을 읽어들여 대상 파일로 복사하는 프로그램을 작성하세요.
단, 복사의 진행 과정을 백분율로 화면에 출력하고, 한 번에 4KB 단위로 복사합니다.
그리고 대상 파일의 존재 유무에 상관없이 무조건 생성하며, 파일의 크기가 최대 100MB 이상인 경우는 고려하지 않습니다.
*/
void main(int argc, char* argv[])
{
    if (argc != 3)
    {
        printf("바이너리 파일의 경로 2개 입력해주세요.\n");
        return;
    }
    FILE *orgFp = fopen(argv[1], "rb");
    FILE *dstFp = fopen(argv[2], "wb");
    int nFileSize = 0;
    int fiop = 0;
    double CPcnt = 0.0, CPrate = 0.0;
    char szBuffer[1024*4] = {0};

    if (orgFp == NULL || dstFp == NULL)
    {   
        printf("빈 파일입니다.\n");
        return;
    }
    fseek(orgFp, 0, SEEK_END);
    nFileSize = ftell(orgFp);
    if (nFileSize > CHKSIZE)
    {
        printf("100MB가 넘습니다.\n");
        return;
    }

    fseek(orgFp, 0, SEEK_SET);
    printf("test1\n");
    while (fread(szBuffer, COPYSIZE, 1, orgFp))
    {
        fiop = ftell(orgFp);  // 마지막으로 4KB 단위로 읽은 데이터 포인터 저장
        fwrite(szBuffer, COPYSIZE, 1, dstFp);
        CPcnt += (double)COPYSIZE;
        CPrate = (CPcnt/nFileSize) * 100.0;
        printf("%dByte 진행률: %4.2f%%\n", nFileSize, CPrate);
    }
    // 4KB 단위로 읽지 못해 남은 데이터 복사
    fseek(orgFp, -(nFileSize - fiop), SEEK_END);
    fread(szBuffer, nFileSize - fiop, 1, orgFp);
    fwrite(szBuffer, nFileSize - fiop, 1, dstFp);
    printf("복사완료\n");
    
    fclose(orgFp);
    fclose(dstFp);
}