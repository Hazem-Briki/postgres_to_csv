import logging

from extract import extract_books
from transform import transform_books
from load import get_last_successful_run, upsert_books


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def run_etl():

    logger.info("ETL started")

    last_successful_run = get_last_successful_run()

    logger.info(
        "Last successful run: %s",
        last_successful_run
    )

    df = extract_books(last_successful_run)

    logger.info(
        "Extracted %d rows",
        len(df)
    )

    if df.empty:
        logger.info("No new or changed records found")
        logger.info("ETL completed successfully")
        return

    df = transform_books(df)

    logger.info(
        "Transformed dataset: %d rows",
        len(df)
    )

    upsert_books(df)

    logger.info("ETL completed successfully")


if __name__ == "__main__":
    run_etl()