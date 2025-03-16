from sqlalchemy import create_engine
import psycopg2 
import pandas as pd

db_params = {
    "host": "localhost",
    "port": "5435",
    "database": "courses_analysis",
    "user": "vietanlms",
    "password": "lmspipeline"
}

engine = create_engine(f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")

conn = psycopg2.connect(**db_params)

query = """
SELECT * FROM advertisement_metrics;
"""

df = pd.read_sql(query, conn) 
print(df.info())
