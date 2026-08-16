import logging


logger = logging.getLogger(__name__)


def load_to_csv(df, filename):

    df.to_csv(
        filename,
        index=False
    )

    logger.info(
        "Loaded %d rows into %s",
        len(df),
        filename
    )