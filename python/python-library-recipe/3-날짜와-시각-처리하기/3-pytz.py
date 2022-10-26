import pytz  # pip install pytz           
from datetime import datetime


"""pytz는 Olson 표준시간대라는 정보를 파이썬용으로 정리한 것
pytz를 사용하면 서머타임 등을 포함한 정확한 표준시간대 처리 가능
"""
def main():
    # 표준시간대 정보 다루기
    # timezone()
    # 인수: 표준시간대를 표시할 문자열
    # 반환: pytz.tzinfo (datetime.tzinfo를 상속한 것)
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    seoul = pytz.timezone('Asia/Seoul')
    eastern = pytz.timezone('US/Eastern') 

    # 표준시간대가 지정된 datetime 생성
    seoul_dt = seoul.localize(datetime(2014, 1, 1, 1, 17, 22))
    print(seoul_dt.strftime(fmt))
    eastern_dt = seoul_dt.astimezone(eastern)  # 동부 시각으로 변경
    print(eastern_dt.strftime(fmt))
    
    jan = datetime(2015, 1, 1)
    jun = datetime(2015, 6, 1)
    print(eastern.utcoffset(jan))  # UTC로부터 지정된 일시의 차를 반환
    print(eastern.utcoffset(jun))
    print(eastern.dst(jan))  # 서머타임의 차를 반환
    print(eastern.dst(jun))
    print(eastern.tzname(jan))  # 표준시간대 이름을 반환  
    print(eastern.tzname(jun))


if __name__ == "__main__":
    main()
