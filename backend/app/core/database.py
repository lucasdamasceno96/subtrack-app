from sqlmodel import create_engine, Session
from app.core.config import settings
from typing import Generator

# O Engine é a fábrica de conexões.
# echo=True faz o log das queries SQL (ótimo para debug, desligar em prod)
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)

def get_session() -> Generator[Session, None, None]:
    """
    Dependency function to yield database sessions.
    Ensures the session is closed even if an error occurs.
    """
    with Session(engine) as session:
        yield session