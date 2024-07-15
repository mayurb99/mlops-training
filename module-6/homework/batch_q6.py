import os
import sys
from datetime import datetime
import pandas as pd

def get_input_path(year, month):
    default_input_pattern = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
    input_pattern = os.getenv('INPUT_FILE_PATTERN', default_input_pattern)
    return input_pattern.format(year=year, month=month)


def get_output_path(year, month):
    default_output_pattern = 's3://nyc-duration-prediction-alexey/taxi_type=fhv/year={year:04d}/month={month:02d}/predictions.parquet'
    output_pattern = os.getenv('OUTPUT_FILE_PATTERN', default_output_pattern)
    return output_pattern.format(year=year, month=month)



def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)


options = {
    'client_kwargs': {
        'endpoint_url': "http://localhost:4566"
    }
}

def prediction():
    
    input_file = get_input_path(2023, 1)
    output_file = get_output_path(2023, 1)
    os.system('python batch.py 2023 1')
    prediction = pd.read_parquet(output_file, storage_options=options)
    print(f"Sum of prediction is  {prediction['predicted_duration'].sum()}")

    

	


if __name__ == "__main__":
    prediction()