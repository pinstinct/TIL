# SQL Expression Language Tutorial

## Connecting

```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///tutorial.db', echo=True)
```
`echo` 플래그는 SQLAlchemy 로깅을 설정하는 단축어이다.

## Define and Create Tables


