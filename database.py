import os
from supabase import create_client, Client


url: str = "https://dbsoziczronwqwgjfbac.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRic296aWN6cm9ud3F3Z2pmYmFjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTUzNTA5NDAsImV4cCI6MjAzMDkyNjk0MH0.7OhB7JYkccBv1-bbwILx_5LIkxEkQZa3DVIli-xcJdg"

# Create a Supabase client
supabase: Client = create_client(url, key)

def insert_data(table_name, json):
    for element in json:
        try:
            supabase.table(table_name).insert(element).execute()
        except Exception as e:
            print(f'Error inserting the entry {element}:- ', e)

    return 'success'

 
import psycopg2

pg_host = "aws-0-ap-south-1.pooler.supabase.com"     
pg_port = "5432"                   
pg_user = "postgres.dbsoziczronwqwgjfbac"  
pg_password = "parthnangroo"
pg_database = "postgres"


conn = psycopg2.connect(
    host=pg_host,
    port=pg_port,
    user=pg_user,
    password=pg_password,
    dbname=pg_database
)

def delete_database(table_name: str):
    try:
        cur = conn.cursor()
        delete_query = f"DELETE FROM {table_name};"
        cur.execute(delete_query)
        conn.commit()
        print(f"All rows deleted from table '{table_name}'.")
    except Exception as e:
        print(f"Error deleting rows: {e}")
    finally:
        cur.close()