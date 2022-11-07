import os
from multiprocessing import Process, Queue, Pipe, Lock, Pool


def f(x):
    print(f'{x} - 프로세스 ID: {os.getpid()} (부모 프로세서 ID: {os.getppid()})')


def fl(lock, x):
    lock.acquire()  # lock이 unlock 상태가 될 때까지 block
    print(f'{x}번째 프로세스 실행 중')
    lock.release()  # lock 해제


def put(q, n):
    # 큐에 메시지를 송신
    q.put(f'{n}회째의 Hello World!')


def sender(conn):
    # 송신측
    conn.send('Hello World')  #다른 자식 프로세스로 Hello World라는 메시지를 송신
    conn.close()


def receiver(conn):
    # 수신측
    msg = conn.recv()
    print(f'메시지 수신: {msg}')
    conn.close()


def x(x):
    return x * x


def main():
    """프로세스 생성하기 """
    for i in range(3):
        p = Process(target=f, args=(i, ))  # target:자식 프로세스를 생성하는 대상, args: 인수
        p.start()  # 자식프로세스를 생성
    p.join()  # 자식프로세스 종료를 기다림
    print(p.is_alive())  # 프로세스가 종료되었는지 확인
    
    """프로세스 간 객체 교환하기 """
    # 프로세스 간 통신을 위해 큐(Queue)와 파이프(Pipe) 두 가지 수단이 있음

    # 큐(Queue): thread-safe, process-safe 통신 방법
    # thread-safe, process-safe: 여러 개의 스레드 및 프로세스가 동시에 병렬로 실행되어도 문제가 발생하지 않는다는 것을 의미
    # 보통 어떤 객체에 접근하는 스레드나 프로세스는 한 번에 하나로 제한
    q = Queue()
    for i in range(3):
        p = Process(target=put, args=(q, i, ))
        p.start()
    print(q.get())  # 큐로 보낸 메시지를 수신
    print(q.get())
    print(q.get())
    # print(q.get())  # 꺼낼 메시지가 없으므로 대기하게 됨
    p.join()

    # 파이프(Pipe): 양방향 통신을 가능하게 하는 기술
    # 큐보다 몇 배 더 빠르게 동작하지만, thread-safe가 아니므로 엔드 포인트가 2개 밖에 없는 경우 사용함
    parent_conn, child_conn = Pipe()  # 메시지를 송수신하는 파이프 생성
    p = Process(target=sender, args=(child_conn, ))  # 메시지 송신
    p.start()
    p = Process(target=receiver, args=(parent_conn, ))   # 메시지 수신
    p.start()
    p.join()

    """프로세스 동기화하기 """
    # 프로세스 간에 lock을 사용하여 동기화 하지 않으면 표준 출력 내용에는 각 프로세스 출력이 섞이게 됨
    for i in range(3):
        p = Process(target=f, args=(i, ))
        p.start()
    p.join()

    print('=====')
    # lock을 사용하여 프로세스 실행을 제어
    # lock을 사용하면 한 번에 하나의 프로세스만 표준 출력에 기록하도록 할 수 있음
    lock = Lock()
    for i in range(3):
        p = Process(target=fl, args=(lock, i, ))
        p.start()
    p.join()

    """동시에 실행하는 프로세스 수 제어하기 """
    # Pool 클래스가 지정된 수의 프로세스를 풀링(pooling)하여, 태스크가 들어왔을 때 비어있는 적당한 프로세스에 태스크를 할당
    p = Pool(processes=4)  # 프로세스 수 상한을 4개로 설정
    result = p.apply_async(func=x, args=[10])  # 비동기로 x(10)처리 실행
    print(result.get())  # 결과 취득

    """mutiprocessing과 threading의 차이 
    둘다 병렬처리가 기능을 제공한다.
    하지만 threading 모듈에는 GIL 제약 때문에, 한 번에 하나의 스레드밖에 실행할 수 없다는 단점이 있다.
    GIL이란, 여러 개의 스레드가 동시에 메모리에 접근하지 않도록 1인터프리터 당 1스레드를 보장하는 것이다.
    이에 반해 multiprocessing 모듈은 스레드 대신 서브 프로세스를 이용함으로써, GIL 문제를 회피하여 여러 CPU나 멀티코어 CPU의 리소스를 최대한으로 활용할 수 있다.
    """


if __name__ == "__main__":
    main()
    