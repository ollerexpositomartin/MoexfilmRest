import logging
import psycopg2
from Moexfilm import application_context
from Moexfilm.core.media.domain.repositories import MoexfilmConnector

config = application_context.config


class MoexfilmDbConnector(MoexfilmConnector):

    def __enter__(self) -> 'MoexfilmDbConnector':
        self._conn = psycopg2.connect(f"""
            host='{config.DB_HOST}' 
            dbname='{config.DB_NAME}' 
            user='{config.DB_USER}' 
            password='{config.DB_PASSWORD}'
            """)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()

    def end(self):
        try:
            self._conn.commit()
        except Exception as e:
            logging.error(f"Error to end connection 🤢 : {e}")
        finally:
            self._conn.close()

    def execute(self, query: str, params=None):
        with self._conn.cursor() as cursor:
            try:
                cursor.execute(query, params)
            except Exception as e:
                logging.error(f"Error to execute query 🤢 : {e}")
                self._conn.rollback()

            if cursor.description:
                return cursor.fetchall()
            else:
                return None
