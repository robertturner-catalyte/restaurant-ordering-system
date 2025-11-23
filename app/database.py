
from contextlib import contextmanager
from pydantic_settings import BaseSettings
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError, InternalError, DBAPIError, SQLAlchemyError
from .exceptions import DBQueryError, DatabaseError

class DBSettings(BaseSettings):
    name: str
    user: str
    password: str
    server: str
    port: str
    driver: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Config:
        env_prefix = "DB_"

class DatabaseConnector:
    def __init__(self):
        db_settings = DBSettings()
        self.db_name = db_settings.name

        connection_str = f"postgresql+{db_settings.driver}://{db_settings.user}:{db_settings.password}@{db_settings.server}:{db_settings.port}/{db_settings.name}"
        try:
            engine = create_engine(connection_str, future = True, echo=False)
            with engine.connect() as conn:
                pass
        except Exception:
            with create_engine(
                url=f"postgresql+{db_settings.driver}://{db_settings.user}:{db_settings.password}@{db_settings.server}:{db_settings.port}/postgres",
                isolation_level="AUTOCOMMIT"
            ).connect() as conn:
                try:
                    conn.execute(text(f"CREATE DATABASE {db_settings.name}"))
                except Exception as e:
                    raise e
        self.session_maker =sessionmaker(bind=engine)

    @contextmanager
    def get_session(self):
        try:
            with self.session_maker() as session:
                yield session
        except (OperationalError, InternalError) as e:
            raise DatabaseError(str(e))
        except DBAPIError as e:
            raise DBQueryError(str(e))
        except SQLAlchemyError as e:
            raise DatabaseError(str(e))
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            session.close()

database_connector = DatabaseConnector()



