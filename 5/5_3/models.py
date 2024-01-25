from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase

# Подключение к БД
#postgres_db = "postgresql://Alex:Alex_password@localhost/myDataBase"

# Создание движка SqlAlchemy
#engine = create_engine(postgres_db)

# Базовый класс
class Base(DeclarativeBase): pass

# Класс(таблица) Продукции
class Product(Base):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    count = Column(Integer)
    description = Column(String)

# Создание таблиц
#Base.metadata.create_all(bind=engine)