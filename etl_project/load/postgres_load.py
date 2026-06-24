# from sqlalchemy import create_engine

# from config.settings import (
#     DB_HOST,
#     DB_NAME,
#     DB_USER,
#     DB_PASSWORD,
#     DB_PORT
# )

# def load_data(df):

#     from urllib.parse import quote_plus

# encoded_password = quote_plus(DB_PASSWORD)

# engine = create_engine(
#     f"postgresql://{DB_USER}:{encoded_password}"
#     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

#     df.to_sql(
#         "products",
#         engine,
#         if_exists="append",
#         index=False
#     )

#     print("Loaded Successfully")

# import logging
# from sqlalchemy import create_engine

# def load_data(df):

#     engine = create_engine(
#         "postgresql://postgres:Senumi%4018@localhost:5432/shopdb"
#     )

#     conn = engine.connect()
#     logging.info("PostgreSQL connection established successfully")
#     print("POSTGRES LOAD FILE LOADED")


#     df.to_sql(
#         "products",
#         engine,
#         if_exists="append",
#         index=False,
#         chunksize=1000
#     )

#     conn.close()

import logging
from sqlalchemy import create_engine

print("POSTGRES LOAD FILE LOADED")

def load_data(df):

    logging.info("Starting DB load")

    engine = create_engine(
        "postgresql://postgres:Senumi%4018@localhost:5432/shopdb"
    )

    conn = engine.connect()
    print("CONNECTED SUCCESSFULLY")

    df.to_sql(
        "products",
        engine,
        if_exists="append",
        index=False,
        chunksize=1000
    )

    print(f"{len(df)} rows inserted successfully")
    logging.info(f"{len(df)} rows inserted successfully")

    logging.info("Data loaded successfully")


    conn.close()