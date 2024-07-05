if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

import pickle
import pandas as pd
import sys
import os
import s3fs
import subprocess

@data_exporter
def export_data(df_result, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    
    output_file = f"s3://module-04-output-mayur/yellow_tripdata_{kwargs['year']}-{kwargs['month']}.parquet"
    df_result.to_parquet( output_file, engine='pyarrow', compression=None, index=False )

    print("Successfully uploaded to S3")

