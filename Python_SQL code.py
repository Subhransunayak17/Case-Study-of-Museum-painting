import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:12345@localhost:1176/painting'#hostname-postgres,password-12345,username-localhost,post-1176,painting is the database name created in sql
db = create_engine(conn_string)
conn = db.connect()

files = ['artist', 'canvas_size', 'image_link', 'museum', 'museum_hours', 'product_size', 'subject', 'work']#these are the tables we want to insert

for file in files:
    df = pd.read_csv(rf'C:\Users\subhr\OneDrive\Desktop\Kaggle Data Set\{file}.csv')  # raw f-string#path is the loaction of csv files
    df.to_sql(file, con=conn, if_exists='replace', index=False)

