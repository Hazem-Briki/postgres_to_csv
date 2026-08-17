import pandas as pd

from src.transform import transform_books


def test_negative_price_is_removed():

    df = pd.DataFrame({
        "id": [1, 2],
        "name": ["Book A", "Book B"],
        "price": [50.0, -10.0],
        "rating": [4, 3],
        "stock": [True, True]
    })

    result = transform_books(df)

    assert len(result) == 2
    assert result.iloc[0]["name"] == "Book A"
    assert result.iloc[0]["price"] == 50.0

def test_duplicates_are_removed():

    df = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Book A", "Book A", "Book B"],
        "price": [50.0, 50.0, 30.0],
        "rating": [4, 4, 3],
        "stock": [True, True, True]
    })

    result = transform_books(df)

    assert len(result) == 2

def test_name_is_stripped():

    df = pd.DataFrame({
        "id": [1],
        "name": ["  Book A  "],
        "price": [50.0],
        "rating": [4],
        "stock": [True]
    })

    result = transform_books(df)

    assert result.iloc[0]["name"] == "Book A"