import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASES = dict()
DATABASES['prod'] = {
    'HOST': 'postgres',
    'PORT': '5432',
    'DBNAME': 'test',
    'USER': 'username',
    'PASSWORD': 'password'
}
conn_string = f"host='{DATABASES['prod']['HOST']}' dbname='{DATABASES['prod']['DBNAME']}' user='{DATABASES['prod']['USER']}' password='{DATABASES['prod']['PASSWORD']}' port='{DATABASES['prod']['PORT']}'"
conn = psycopg2.connect(conn_string)

engine = create_engine(f"postgresql+psycopg2://{DATABASES['prod']['USER']}:{DATABASES['prod']['PASSWORD']}@{DATABASES['prod']['HOST']}:{DATABASES['prod']['PORT']}/{DATABASES['prod']['DBNAME']}")

Session = sessionmaker(engine)
