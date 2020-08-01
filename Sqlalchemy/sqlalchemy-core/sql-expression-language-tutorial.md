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
print(metadata.tables)
immutabledict({'users': Table('users', MetaData(bind=None), Column('id', Integer(), table=<users>, primary_key=True, nullable=False), Column('name', String(), table=<users>), Column('fullname', String(), table=<users>), schema=None), 'addresses': Table('addresses', MetaData(bind=None), Column('id', Integer(), table=<addresses>, primary_key=True, nullable=False), Column('user_id', Integer(), ForeignKey('users.id'), table=<addresses>), Column('email_address', String(), table=<addresses>, nullable=False), schema=None)})
```
