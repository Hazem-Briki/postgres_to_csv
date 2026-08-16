import pandas as pd
from sqlalchemy import create_engine

from config import DATABASE_URL


def extract_books():

    engine = create_engine(DATABASE_URL)

    query = """
        SELECT id, name, price, rating, stock
        FROM books;
    """

    df = pd.read_sql(query, engine)

    engine.dispose()

    return df