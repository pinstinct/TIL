from pprint import pprint
from dateutil.parser import parse  # pip install python-dateutil
from dateutil.relativedelta import relativedelta, TU, FR
from dateutil.rrule import rrule, DAILY, WEEKLY, MONTHLY, MO, TH, SU
from datetime import datetime, date


"""datetime 모듈에 대한 강력한 확장기능을 제공하는 dateutil 주요 기능
다양한 문자열 형식의 날짜 구문 해석
상대적 날짜의 차이 계산
유연한 반복 규칙
"""
def main():
    """날짜 구문 해석하기 - parser"""
    # 날짜 문자열의 구문을 해석함
    # 반환: datetime.datetime
    print(parse('2015/06/23 12:34:56'))
    print(parse('2015-06-23'))
    print(parse('20140512'))
    print(parse('Tue 24 Jun 2015 12:34:56 KST'))
    default = datetime(2015, 8, 1)
    print(parse('12:34:45', default=default))
    print(parse('15/2/4'))  # 일/월/년으로 해석
    print(parse('15/2/4', yearfirst=True))  # 년/월/일로 해석

    """날짜의 차 계산하기 - relativedelta """
    # 날짜 계산
    now = datetime.now()
    print(now)
    today = date.today()
    print(today)
    print(now + relativedelta(months=1))  # 한달 뒤
    print(now + relativedelta(months=-1, weeks=1))  # 한 달 전의 일주일 뒤
    print(today + relativedelta(months=1, hour=10))

    # 요일 지정
    print(today + relativedelta(weekday=FR))  # 다가오는 금요일 (오늘이 금요일이면 오늘을 출력)
    print(today + relativedelta(day=31, weekday=FR(-1)))  # 이 달의 마지막주 금요일
    print(today + relativedelta(weekday=TU(+1)))  # 다가오는 화요일 (오늘이 화요일이면 오늘을 출력)

    # yearday, nlyearday 지정
    print(date(2015, 1, 1) + relativedelta(yearday=100))  # 2015년의 100일째
    print(date(2015, 12, 1) + relativedelta(yearday=100))  # 날짜와 상관없이 그 해 맨 처음부터 셈
    print(date(2012, 1, 1) + relativedelta(yearday=100))  # 2012년의 100일째
    print(date(2012, 1, 1) + relativedelta(nlyearday=100))  # 2012년의 윤일을 제외한 100일째

    # 두 개의 일시가 주어진 경우
    print(relativedelta(date(2015, 1, 1), today))

    """반복 규칙 - rrule """
    print('=====')
    start = datetime(2015, 6, 28)
    pprint(list(rrule(DAILY, count=5, dtstart=start)))  # 지정일로부터 5일간
    pprint(list(rrule(DAILY, dtstart=start, until=datetime(2015, 7, 1))))  # 지정기간 동안 매일
    pprint(list(rrule(WEEKLY, count=8, wkst=SU, byweekday=(MO, TH))))  # 매주 월, 금 / dtstart를 지정하지 않으면 datetime.now() 값이 사용
    pprint(list(rrule(MONTHLY, count=3, byweekday=MO(-1))))  # 매주 마지막 금요일
    pprint(list(rrule(WEEKLY, interval=2, count=3)))  # 격주


if __name__ == "__main__":
    main()
