# [SQL Expression Language Tutorial](https://docs.sqlalchemy.org/en/13/core/tutorial.html)

Python shell에서 진행한다. 

## Connecting

```python
>>> from sqlalchemy import create_engine
>>> engine = create_engine('sqlite:///core-tutorial.db', echo=True)
```
`echo` 플래그는 SQLAlchemy 로깅을 설정하는 단축어이다.

## Define and Create Tables

```python
>>> from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
>>> metadata = MetaData()
>>> users = Table('users', metadata,
...     Column('id', Integer, primary_key=True),
...     Column('name', String),
...     Column('fullname', String),
... )

>>> addresses = Table('addresses', metadata,
...   Column('id', Integer, primary_key=True),
...   Column('user_id', None, ForeignKey('users.id')),
...   Column('email_address', String, nullable=False)
...  )

>>> metadata.create_all(engine)
```
`MetaData`라는 카달로그 안에 테이블을 모두 정의한다. 

```python
>>> print(metadata.tables)
immutabledict({'users': Table('users', MetaData(bind=None), Column('id', Integer(), table=<users>, primary_key=True, nullable=False), Column('name', String(), table=<users>), Column('fullname', String(), table=<users>), schema=None), 'addresses': Table('addresses', MetaData(bind=None), Column('id', Integer(), table=<addresses>, primary_key=True, nullable=False), Column('user_id', Integer(), ForeignKey('users.id'), table=<addresses>), Column('email_address', String(), table=<addresses>, nullable=False), schema=None)})
```

## Insert Expressions

```python
>>> ins = users.insert().values(name='jack', fullname='Jack Jones')
>>> ins.compile().params  # 데이터 보기  
{'fullname': 'Jack Jones', 'name': 'jack'}
```

## Executing

```python
>>> conn = engine.connect()  # DB 연결
>>> result = conn.execute(ins)  # ResultProxy 객체 
INSERT INTO users (name, fullname) VALUES (?, ?)
('jack', 'Jack Jones')
COMMIT
```
입력한 매개 변수 대신 `?`가 로그가 출력된다. `Connection`이 SQLite dialect 사용해 명령문을 생성하는데, dialect는 이 명령어를 인식하지 못하기 때문에 입력한 매개 변수들을 기본값으로 돌린다.

```python
>>> result.inserted_primary_key
[1]
```

## Executing Multiple Statements

위의 예제는 의도적으로 다양한 동작을 보여주기 위한 방법이다. 일반적인 방법은 아래와 같다.
```python
>>> ins = users.insert()
>>> conn.execute(ins, id=2, name='wendy', fullname='Wendy Williams')
```
여러 매개 변수들을 실행할 때, 각 딕셔너리에는 같은 키들이 있어야 한다. 리스트의 첫 번째 딕셔너리를 컴파일하고, 모든 후속 딕셔너리가 호환되는 것으로 가정하기 때문이다.
```python
>>> conn.execute(addresses.insert(), [
...    {'user_id': 1, 'email_address' : 'jack@yahoo.com'},
...    {'user_id': 1, 'email_address' : 'jack@msn.com'},
...    {'user_id': 2, 'email_address' : 'www@www.org'},
...    {'user_id': 2, 'email_address' : 'wendy@aol.com'},
... ])
```
`insert()`, `update()`, `delete()` construct에서도 "executemany" 스타일의 호출이 가능하다.

## Selecting

SELECT 문을 생성하는데 사용하는 construct는 `select()` 함수이다.
```python 
>>> from sqlalchemy.sql import select
>>> s = select([users])
>>> result = conn.execute(s)
SELECT users.id, users.name, users.fullname
FROM users
()
```
리턴 값, `result`는 DBAPI 커서와 매우 유사한 ResultProxy 객체이며 `fetchone()`, `fetchall()` 같은 함수를 포함한다.

```python
>>> for row in result:
...     print(row)
(1, u'jack', u'Jack Jones')
(2, u'wendy', u'Wendy Williams')

>>> result = conn.execute(s)
>>> row = result.fetchone()
>>> print("name:", row['name'], "; fullname:", row['fullname'])
name: jack ; fullname: Jack Jones
>>> row = result.fetchone()
>>> print("name:", row[1], "; fullname:", row[2])
name: wendy ; fullname: Wendy Williams

>>> for row in conn.execute(s):
...     print("name:", row[users.c.name], "; fullname:", row[users.c.fullname])
name: jack ; fullname: Jack Jones
name: wendy ; fullname: Wendy Williams
```
ResultProxy 객체는 "auto close" 기능을 제공한다. 명시적으로 닫으려면 `ResultProxy.close()` 함수를 사용한다.
```python
>>> result.close()
```

### Ordering

```python
>>> stmt = select([users.c.name]).order_by(users.c.name)
>>> conn.execute(stmt).fetchall()
[(u'jack',), (u'wendy',)]
```
`ColumnElement.asc()`와 `ColumnElement.desc()`를 사용해 오름차순 또는 내림차순을 제어할 수 있다.

```python
>>> stmt = select([users.c.name]).order_by(users.c.name.desc())
>>> conn.execute(stmt).fetchall()
[(u'wendy',), (u'jack',)]
```

### Grouping

```python
>>> stmt = select([users.c.name, func.count(addresses.c.id)]).\
...             select_from(users.join(addresses)).\
...             group_by(users.c.name)
>>> conn.execute(stmt).fetchall()
[(u'jack', 2), (u'wendy', 2)]
```

## Selecting Specific Columns

```python
>>> s = select([users.c.name, users.c.fullname])
>>> result = conn.execute(s)
>>> for row in result:
...     print(row)
(u'jack', u'Jack Jones')
(u'wendy', u'Wendy Williams')

>>> for row in conn.execute(select([users, addresses])):
...     print(row)
(1, u'jack', u'Jack Jones', 1, 1, u'jack@yahoo.com')
(1, u'jack', u'Jack Jones', 2, 1, u'jack@msn.com')
(1, u'jack', u'Jack Jones', 3, 2, u'www@www.org')
(1, u'jack', u'Jack Jones', 4, 2, u'wendy@aol.com')
(2, u'wendy', u'Wendy Williams', 1, 1, u'jack@yahoo.com')
(2, u'wendy', u'Wendy Williams', 2, 1, u'jack@msn.com')
(2, u'wendy', u'Wendy Williams', 3, 2, u'www@www.org')
(2, u'wendy', u'Wendy Williams', 4, 2, u'wendy@aol.com')

>>> s = select([users, addresses]).where(users.c.id == addresses.c.user_id)
>>> for row in conn.execute(s):
...     print(row)
(1, u'jack', u'Jack Jones', 1, 1, u'jack@yahoo.com')
(1, u'jack', u'Jack Jones', 2, 1, u'jack@msn.com')
(2, u'wendy', u'Wendy Williams', 3, 2, u'www@www.org')
(2, u'wendy', u'Wendy Williams', 4, 2, u'wendy@aol.com')
```

## Conjunctions

```python
>>> from sqlalchemy.sql import and_, or_, not_
>>> print(and_(
...         users.c.name.like('j%'),
...         users.c.id == addresses.c.user_id,
...         or_(
...              addresses.c.email_address == 'wendy@aol.com',
...              addresses.c.email_address == 'jack@yahoo.com'
...         ),
...         not_(users.c.id > 5)
...       )
...  )
users.name LIKE :name_1 AND users.id = addresses.user_id AND
(addresses.email_address = :email_address_1
   OR addresses.email_address = :email_address_2)
AND users.id <= :id_1
```

```python
>>> s = select([(users.c.fullname +
...               ", " + addresses.c.email_address).
...                label('title')]).\
...        where(
...           and_(
...               users.c.id == addresses.c.user_id,
...               users.c.name.between('m', 'z'),
...               or_(
...                  addresses.c.email_address.like('%@aol.com'),
...                  addresses.c.email_address.like('%@msn.com')
...               )
...           )
...        )
>>> conn.execute(s).fetchall()
[(u'Wendy Williams, wendy@aol.com',)]

# and_() 대신 Select.where()를 사용 
>>> s = select([(users.c.fullname +
...               ", " + addresses.c.email_address).
...                label('title')]).\
...        where(users.c.id == addresses.c.user_id).\
...        where(users.c.name.between('m', 'z')).\
...        where(
...               or_(
...                  addresses.c.email_address.like('%@aol.com'),
...                  addresses.c.email_address.like('%@msn.com')
...               )
...        )
>>> conn.execute(s).fetchall()
[(u'Wendy Williams, wendy@aol.com',)]
```

## Using Textual SQL

```python
>>> from sqlalchemy.sql import text
>>> s = text(
...     "SELECT users.fullname || ', ' || addresses.email_address AS title "
...         "FROM users, addresses "
...         "WHERE users.id = addresses.user_id "
...         "AND users.name BETWEEN :x AND :y "
...         "AND (addresses.email_address LIKE :e1 "
...             "OR addresses.email_address LIKE :e2)")
>>> conn.execute(s, x='m', y='z', e1='%@aol.com', e2='%@msn.com').fetchall()
[(u'Wendy Williams, wendy@aol.com',)]
```

## Using Aliases and Subqueries

```python
>>> a1 = addresses.alias()
>>> a2 = addresses.alias()
>>> s = select([users]).\
...        where(and_(
...            users.c.id == a1.c.user_id,
...            users.c.id == a2.c.user_id,
...            a1.c.email_address == 'jack@msn.com',
...            a2.c.email_address == 'jack@yahoo.com'
...        ))
>>> conn.execute(s).fetchall()
SELECT users.id, users.name, users.fullname
FROM users, addresses AS addresses_1, addresses AS addresses_2
WHERE users.id = addresses_1.user_id
    AND users.id = addresses_2.user_id
    AND addresses_1.email_address = ?
    AND addresses_2.email_address = ?
('jack@msn.com', 'jack@yahoo.com')
[(1, u'jack', u'Jack Jones')]
```
SQL 결과에 `addresses_1`과 `addresses_2`가 생겼다. 이 이름은 명령문 내 위치에 따라 결정된다. 

```python
>>> a1 = addresses.alias('a1')
>>> s = select([users]).\
...        where(and_(
...            users.c.id == a1.c.user_id,
...            users.c.id == a2.c.user_id,
...            a1.c.email_address == 'jack@msn.com',
...            a2.c.email_address == 'jack@yahoo.com'
...        ))
>>> conn.execute(s).fetchall()
SELECT users.id, users.name, users.fullname
FROM users, addresses AS a1, addresses AS addresses_1
WHERE users.id = a1.user_id 
	AND users.id = addresses_1.user_id 
	AND a1.email_address = ? 
	AND addresses_1.email_address = ?
('jack@msn.com', 'jack@yahoo.com')
[(1, u'jack', u'Jack Jones')]
```

```python
>>> address_subq = s.alias()
>>> s = select([users.c.name]).where(users.c.id == address_subq.c.id)
>>> conn.execute(s).fetchall()
[(u'jack',)]
```

## Using Joins

```python
>>> print(users.join(addresses))
users JOIN addresses ON users.id = addresses.user_id
```

두 테이블이 JOIN 할 때, ForeignKey 기반으로 ON 조건을 자동 생성한다. 

```python
>>> print(users.join(addresses,
...                 addresses.c.email_address.like(users.c.name + '%')
...             )
...  )
users JOIN addresses ON addresses.email_address LIKE users.name || :name_1
```

JOIN을 사용해 `select()`문을 만들 때, `Select.select_from()` 메소드를 사용한다.

```python
>>> s = select([users.c.fullname]).select_from(
...    users.join(addresses,
...             addresses.c.email_address.like(users.c.name + '%'))
...    )
>>> conn.execute(s).fetchall()
[(u'Jack Jones',), (u'Jack Jones',), (u'Wendy Williams',)]
```

```python
>>> s = select([users.c.fullname]).select_from(users.outerjoin(addresses))
>>> print(s)
SELECT users.fullname
    FROM users
    LEFT OUTER JOIN addresses ON users.id = addresses.user_id
```
