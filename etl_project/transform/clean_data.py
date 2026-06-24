import pandas as pd

def transform_data(data):

    df = pd.DataFrame(data)

    df = df[
        [
            "id",
            "title",
            "price",
            "category"
        ]
    ]

    df["title"] = df["title"].str.strip().str.title()
    df["category"] = df["category"].str.strip().str.lower()

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    df = df.drop_duplicates()
    df = df.dropna()

    df = df[df["price"] > 0]

    return df