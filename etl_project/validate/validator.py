def validate_data(df):

    if df.empty:
        raise ValueError(
            "Data is empty"
        )

    if df["id"].isnull().any():
        raise ValueError(
            "Missing IDs"
        )

    return True