import pandas as pd
from sqlalchemy import create_engine
from time import time

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

#df_iter = pd.read_csv('yellow_tripdata_2021-01.csv.gz', iterator=True, chunksize=100000)
df_iter = pd.read_csv('green_tripdata_2019-09.csv.gz', iterator=True, chunksize=100000)
df = next(df_iter)

#df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
#df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

# Write table schema
#df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')
df.head(n=0).to_sql(name='green_taxi_data', con=engine, if_exists='replace')

# Write 1st set of data
df.to_sql(name='green_taxi_data', con=engine, if_exists='append')

while True: 
    t_start = time()

    df = next(df_iter)

    #df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    #df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    
    df.to_sql(name='green_taxi_data', con=engine, if_exists='append')

    t_end = time()

    print('inserted another chunk, took %.3f second' % (t_end - t_start))

# Read into DF  
df_zones = pd.read_csv('taxi+_zone_lookup.csv')

# Read DF to table directly, since it's small
df_zones.to_sql(name='zones', con=engine, if_exists='replace')