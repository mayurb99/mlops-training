#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import sys
import os
categorical = ['PULocationID', 'DOLocationID']


def load_model():
    with open('../../model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
    return dv,model


def read_data(filename):

    df = pd.read_parquet(filename)
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')    
    return df

def create_ride_ids(df, year, month):

    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    return df

def make_predictions(dv,model,df):
    
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    return y_pred



def run():

    year = int(sys.argv[1]) # 2023
    month = int(sys.argv[2]) # 4
    input_file = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'    
    #output_file = f'output/yellow_tripdata_{year:04d}-{month:02d}.parquet' //use this for storing output locally
    output_file = f's3://module-04-output-mayur/yellow_tripdata_{year:04d}-{month:02d}.parquet'

    df = read_data(input_file)
    dv,model = load_model()
    y_pred = make_predictions(dv,model,df)
    
    print('predicted mean duration:', y_pred.mean())
    print(y_pred)
    
    df = create_ride_ids(df, year, month)
    df_result = pd.DataFrame()
    df_result['ride_id']=df['ride_id']
    df_result['predicted_duration'] = y_pred
    
    #os.makedirs('output', exist_ok=True)    
    df_result.to_parquet( output_file, engine='pyarrow', compression=None, index=False )

if __name__== '__main__':
    run()







    
