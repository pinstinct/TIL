import csv


def main():
    """CSV 파일의 읽기와 쓰기 """
    sample = './python/python-library-recipe/8-특정-데이터-포맷-다루기/sample.csv'
    # csv.reader() 함수
    # CSV 파일 각 행의 데이터를 반복 가능한(iterable) reader 객체로 반환
    # 인수: csvfile, dialect(자주 사용하는 서식화 매개변수의 집합 지정), **fmtparams
    # 서식화 매개변수: 구분 문자나 종단 기호를 가리킴
    # dialect는 excel(Excel로 출력되는 CSV 파일), excel-tab(Excel로 출력되는 TSV 파일), unix(종단 기호를 '\n'으로 하는 파일) 중에서 선택
    # delimiter: 구분 문자 지정, 기본 값은 쉼포(,)
    # quotechar: 인용 부호 지정, 기본 값은 큰따옴표("")
    with open(sample, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

    # csv.writer() 함수
    # CSV 파일의 데이터를 구분 문자로 구분된 문자열로 변환하여 출력하기 위한 writer 객체 반환
    with open(sample, mode='r', encoding='utf-8') as read_file:
        reader = csv.reader(read_file)
        next(reader)  # 헤더 행을 날림
        with open('resut.tsv', mode='w', encoding='utf-8') as write_file:
            writer = csv.writer(write_file, delimiter='\t')
            writer.writerow(['도시', '인구 밀도(명/km2)'])  # 헤더 행 쓰기
            for row in reader:
                population_density = float(row[2]) / float(row[3])
                writer.writerow([row[1], int(population_density)])  # 데이터를 서식화하여 writer 파일 객체에 쓰기 

    """CSV 파일 헤더를 이용한 편리한 읽어오기 """
    # DictReader()는 헤더 행을 사전의 키로 각 행의 값을 사전의 값으로 취급할 수 있는 편리한 클래스
    with open(sample, mode='r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            print(row)

    with open(sample, mode='r', encoding='utf-8') as read_file:
        reader = csv.DictReader(read_file)
        with open('result1.tsv', mode='w', encoding='utf-8') as write_file:
            writer = csv.writer(write_file, delimiter='\t')
            writer.writerow(['도시', '인구 밀도(명/km2)'])
            for row in reader:
                population_density = float(row['인구(명)']) / float(row['면적(km2)'])  # 행 문자열을 이용할 수 있어 처리 내용이 명확하게 보임
                writer.writerow([row['도시'], int(population_density)])


if __name__ == "__main__":
    main()
