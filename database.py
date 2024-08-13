from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = 'sqlite:///db.sqlite'

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine) # Procura a todos os modulos que tem as tabelas e cria-as.


def get_session(): 
    with Session(engine) as session:
        yield session
