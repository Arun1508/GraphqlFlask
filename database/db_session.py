from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

POSTGRES = {
    'user': 'postgres',
    'pw': 'qwerty1',
    'db': 'book',
    'host': 'localhost',
    'port': '5432',
}
db_url = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
engine = create_engine(db_url, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))