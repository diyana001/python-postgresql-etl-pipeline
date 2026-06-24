from extract.api_extract import extract_data

from transform.clean_data import transform_data

from validate.validator import validate_data

from load.postgres_load import load_data

def run_etl():

    data = extract_data()

    df = transform_data(data)

    validate_data(df)

    load_data(df)

if __name__ == "__main__":

    run_etl()