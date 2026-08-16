import logging

from extract import extract_books
from transform import transform_books
from load import load_to_csv


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def main():

    logger.info("ETL started")

    try:
        df = extract_books()
        logger.info("Extracted %d rows", len(df))

        df = transform_books(df)
        logger.info("Transformed dataset: %d rows", len(df))

        output_file = "output/books_clean.csv"

        load_to_csv(df, output_file)
        logger.info("CSV created: %s", output_file)

        logger.info("ETL completed successfully")

    except Exception as e:
        logger.error("ETL failed: %s", e)
        raise


if __name__ == "__main__":
    main()