import logging
from logging.config import dictConfig


"""세 가지 로깅 설정 방법 
- logging으로 루트 로거 설정: 한 모듈로만 구성되는 소규모 소프트웨어
- 로거와 핸들러 등을 조합한 모듈 방식으로 설정: 여러 모듈로 구성되는 중~대규모 소프트웨어
- dictConfig() 등을 사용하여 특정 자료구조에서 일괄적으로 설정: 여러 모듈로 구성되는 중~대규모 소프트웨어
"""

"""표준으로 정의된 로그 레벨 
https://docs.python.org/3/library/logging.html#logging-levels
지정한 로그 레벨보다 낮은 값을 가진 로그 레벨 메시지의 출력을 제한할 수 있다.
"""
def main():
    """logging 모듈에서 로그 다루기 """
    # import 직후 logging 모듈에서 로그 출력 메서드를 출력하면 다음과 같이 동작
    # 메시지는 표준 오류 출력된다.
    # 출력 포맷은 <로그레벨>:<로거이름>:<메시지>
    # 로그 레벨은 logging.WARNING으로 설정되어 있다.
    logging.debug('debug message')  # 로그 레벨로 인해 출력되지 않음
    logging.warning('warning message')  # 출력됨
    # 로그 메시지에 변수를 출력하는 예
    favorite_thing = 'bouldering'
    logging.error(f'I love {favorite_thing}')
    # 9-1-logging.py

    """모듈 방식으로 로깅 설정하기 """
    print('=====')
    # 로깅을 구성하는 부품
    # 로거: 로그 출력 인터페이스 제공 
    # 핸들러: 로그의 송신 대상을 결정
    # 필터: 로그의 필터링 기능 제공
    # 포매터: 로그 출력 포맷 결정
    logger = logging.getLogger('hoge.fuga.piyo')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('test.log')  # 파일을 출력 대상으로 하는 핸들러 작성
    handler.setLevel(logging.INFO)  # 로그 레벨 필터는 로거와 핸들러에 의해 동작
    filter = logging.Filter('hoge.fuga')  # 로거 이름이 hoge.fuga에 일치할 때만 출력하는 필터 생성
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 조합
    handler.setFormatter(formatter)  # 핸들러에 포메터 설정
    handler.addFilter(filter)  # 핸들러에 필터 설정
    logger.addHandler(handler)  # 로거에 핸들러 설정
    logger.addFilter(filter)  # 로거에 필터 설정
    logger.debug('debug message')
    logger.info('info message')
    """
    [로거의 계층 구조]
    logging.getLogger()에는 인수로 로거 이름을 전달할 수 있다.
    이 로거 이름의 문자열에 dot가 포함되면 계층 구조가 만들어진다.
    'hoge.fuga.piyo': root -> hoge -> fuga -> piyo
    모든 로거의 계층 구조에는 공통 부모 로거가 존재하며 이것을 가르켜 "루트 로거"라고 부른다.

    로거 계층 구조를 이용한 관용구
    logging.getLogger(__name__): __name__은 패키지나 모듈 구조가 문자열로 저장되어 있기 때문에, 로거 이름을 보면 어느 패키지/모듈에서 출력한 로그인지 직감적으로 알 수 있다.
    로거이름을 __name__으로 하는 로거를 "모듈 레벨 로거"라고 한다.

    자식 로거는 메시지를 부모 로거의 핸들러로 전달한다.

    [필터를 통한 로그 출력 제어]
    logging.Filter('hoge.fuga')와 같이 생성된 필터는 로거나 핸들러에 설정하여 로그 레벨과는 다른 기준을 적용하는 필터링 기능을 제공
    """

    """사전이나 파일로 로깅 설정하기 """
    # 사전 형식으로 작성한 설정 정보로 로깅을 설정
    # 좋은 샘플 코드: https://docs.djangoproject.com/en/4.1/topics/logging/#examples
    config = {
        'version': 1,  # 1만 지원됨
        'disable_existsing_loggers': False,  # False면 기존 로깅설정을 무효화하지 않음
        'formatters':{  # 포매터 설정을 구성하는 사전
            'example': {  # 포매터 이름
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'filters': {  # 필터 설정을 구성하는 사전
            'hoge-filter': {  # 필터 이름
                'name': 'hoge.fuga',  # 필터 대상 로거 이름
            },
        },
        'handlers': {  # 핸들러를 구성하는 사전
            'file': {  # 핸들러 이름
                'level': 'INFO',  # 핸들러 로그 레벨 지정
                'class': 'logging.FileHandler',  # 핸들러의 클래스
                'filename': 'test.log',  # 출력 파일 경로
                'formatter': 'example',  # 핸들러에 설정하는 포메터 이름
                'filters': ['hoge-filter', ],  # 핸들러에 설정하는 필터 이름 리스트
            },
        },
        'loggers': {  # 로거 설정을 구성하는 사전
            'hoge': {  # 로거 이름
                'handlers': ['file', ],  # 로거가 이용하는 핸들러 이름 리스트
                'level': 'INFO',  # 로거의 로그 레벨
                'propagate': True,  # True이면 자식 로거에 설정을 전달함
            }
        },
    }
    dictConfig(config)
    logger = logging.getLogger('hoge.fuga.piyo')
    logger.debug('debug message')
    logger.info('info message')


if __name__ == "__main__":
    main()
