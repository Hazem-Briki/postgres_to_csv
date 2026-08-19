import logging

from sqlalchemy import create_engine, text

from config import DESTINATION_DB_URL


logger = logging.getLogger(__name__)


def upsert_books(df):

    engine = create_engine(DESTINATION_DB_URL)

    query = text("""
        INSERT INTO books_clean (
            id,
            name,
            price,
            rating,
            stock,
            price_category,
            price_with_tax
        )
        VALUES (
            :id,
            :name,
            :price,
            :rating,
            :stock,
            :price_category,
            :price_with_tax
        )
        ON CONFLICT (id)
        DO UPDATE SET
            name = EXCLUDED.name,
            price = EXCLUDED.price,
            rating = EXCLUDED.rating,
            stock = EXCLUDED.stock,
            price_category = EXCLUDED.price_category,
            price_with_tax = EXCLUDED.price_with_tax;
    """)

    records = df.to_dict(orient="records")

    with engine.begin() as connection:
        connection.execute(query, records)

    engine.dispose()

    logger.info(
        "Upserted %d rows into books_clean",
        len(df)
    )


def get_last_successful_run():

    engine = create_engine(DESTINATION_DB_URL)

    query = text("""
        SELECT last_successful_run
        FROM etl_control
        WHERE pipeline_name = 'books_etl';
    """)

    with engine.connect() as connection:
        result = connection.execute(query)
        last_run = result.scalar()

    engine.dispose()

    return last_run