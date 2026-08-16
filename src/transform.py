import logging


logger = logging.getLogger(__name__)


def transform_books(df):

    initial_rows = len(df)

    # Clean names
    df["name"] = df["name"].str.strip()

    # Remove rows with required fields missing
    df = df.dropna(subset=["name", "price", "rating"])
    logger.info("Removed %d rows with missing required values",
                initial_rows - len(df))

    # Remove invalid prices
    before_price_check = len(df)
    df = df[df["price"] >= 0]
    logger.info("Removed %d rows with invalid prices",
                before_price_check - len(df))

    # Remove duplicates
    before_duplicates = len(df)
    df = df.drop_duplicates(
        subset=["name", "price", "rating"]
    )
    logger.info("Removed %d duplicate rows",
                before_duplicates - len(df))

    # Ensure correct types
    df["price"] = df["price"].astype(float)
    df["rating"] = df["rating"].astype(int)
    df["stock"] = df["stock"].astype(bool)

    # Create price category
    df["price_category"] = df["price"].apply(
        lambda x: "Expensive" if x >= 50 else "Normal"
    )

    # Create price with tax
    df["price_with_tax"] = (
        df["price"] * 1.19
    ).round(2)

    # Sort
    df = df.sort_values(
        "price",
        ascending=False
    )

    # Reset index
    df = df.reset_index(drop=True)

    logger.info("Transformation complete: %d rows remain",
                len(df))

    return df