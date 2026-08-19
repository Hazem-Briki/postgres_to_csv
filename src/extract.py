import pandas as pd
from sqlalchemy import create_engine

from config import SOURCE_DB_URL


def extract_books(last_successful_run):

    engine = create_engine(SOURCE_DB_URL)

    query = """
        SELECT id, name, price, rating, stock, updated_at
        FROM books
        WHERE updated_at > %(last_run)s
        ORDER BY updated_at, id;
    """

    df = pd.read_sql(
        query,
        engine,
        params={"last_run": last_successful_run}
    )

    engine.dispose()

    return df