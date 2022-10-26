from asyncio import new_event_loop
from datetime import date, time, datetime, timedelta  # datetime 모듈의 객체

def main():
    """날짜 다루기 - date 객체 """
    new_years_day = date(2122, 1, 1)  # date 객체 생성 
    print(new_years_day)
    print(new_years_day.year, new_years_day.month, new_years_day.day)
    print(new_years_day.weekday())  # 월요일일 1, 일요일을 7로 하여 요일 반환
    print(new_years_day.isoformat())  # ISO 8601 형식(YYYY-MM-DD)의 문자열 반환
    print(str(new_years_day))  # isoformat()과 같은 결과
    print(new_years_day.strftime('%Y/%m/%d'))

    """"시각 다루기 - time 객체 """
    print(time())
    print(time(16, 12, 25))
    print(time(second=10))
    print(time(microsecond=10))
    now = time(16, 12, 26)
    print(now.hour, now.minute, now.second, now.microsecond, now.tzinfo)
    print(now.isoformat())  # ISO 8601 형식(HH:MM:SS.mmmmmm) 또는 마이크로초가 0일 때는 HH:MM:SS의 문자열 반환
    print(str(now))  # isoformat()과 같은 결과
    print(now.tzname())
    print(now.strftime('%H:%M'))

    """일시 다루기 - datetime 객체 """
    print('=====')
    today = datetime.today()
    print(today.date())
    print(today.time())
    print(today)
    print(datetime.utcnow())  # UTC 현재 일시를 반환
    print(today.isoformat())
    print(str(today))
    print(today.strftime('%Y/%m/%d'))

    """일시의 차 - timedelta 객체 """
    print('=====')
    today2 = date.today()
    print(today2)
    print(new_years_day - today2)
    week = timedelta(days=7)
    print(today + week)  # 일주일 뒤
    print(today + week * 2)  # 2주 뒤
    print(today - week)  # 일주일 전


if __name__ == "__main__":
    main()
