import pandas as pd
from sqlalchemy import create_engine


df = pd.read_parquet('module-1/yellow_tripdata_2024-01.parquet')

# PostgreSQL connection details
user = "root"
password = "root"
host = "localhost"  # Or your database server address
port = "5432"       # Default PostgreSQL port
database = "ny_taxi"

# Create an SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

# Convert DataFrame to SQL table
df.to_sql("yellow_tripdata", engine, if_exists="replace", index=False)
print('Saved to db')
# Verify by reading from the table
result = pd.read_sql("SELECT * FROM yellow_tripdata limit 5;", engine)
print(result)