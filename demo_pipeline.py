import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import pymysql

db_params = {
    "host": "localhost",
    "port": "5435",
    "database": "pipeline",
    "user": "vietanlms",
    "password": "lmspipeline"
}

def connect_to_db(db_params):
    print("Connecting to PostgreSQL...")
    conn = psycopg2.connect(**db_params)
    return conn


def load_data_from_google_sheet(google_sheet_id, sheet_name):
    try:
        url='https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=xlsx'
        data = pd.read_excel(url, sheet_name=sheet_name)
        data["gender"] = data["gender"].fillna("other").str.lower()
        conn = connect_to_db(db_params)
        
        cursor = conn.cursor()
        insert_query = "INSERT INTO enrollees (enrollee_id, full_name, city, gender) VALUES (%s, %s, %s, %s);"
        
        for _, row in data.iterrows():
            cursor.execute(insert_query, (row["enrollee_id"], row["full_name"], row["city"], row["gender"]))
        
        conn.commit()
        print("Google sheet data added successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def load_csv_data(link):
    try:
        data = pd.read_csv(link)
        data["experience"] = data["experience"].fillna(data["experience"].mode().values[0]).str.lower()
        data["company_size"] = data["company_size"].fillna("unknown").str.lower()
        data["company_type"] = data["company_type"].fillna("unknown").str.lower()
        data["last_new_job"] = data["last_new_job"].fillna(data["last_new_job"].mode().values[0]).str.lower()
        conn = connect_to_db(db_params)
        
        cursor = conn.cursor()
        insert_query = "INSERT INTO work_experience (enrollee_id, relevent_experience, experience, company_size, company_type, last_new_job) VALUES (%s, %s, %s, %s, %s, %s);"
        
        for _, row in data.iterrows():
            cursor.execute(insert_query, (row["enrollee_id"], row["relevent_experience"], row["experience"], row["company_size"], row["company_type"], row["last_new_job"]))
        
        conn.commit()
        print("CSV data added successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def load_excel_data(file_path):
    try:
        data = pd.read_excel(file_path)
        data["enrolled_university"] = data["enrolled_university"].fillna(data["enrolled_university"].mode().values[0]).str.lower()
        data["education_level"] = data["education_level"].fillna(data["education_level"].mode().values[0]).str.lower()
        data["major_discipline"] = data["major_discipline"].fillna(data["major_discipline"].mode().values[0]).str.lower()
        conn = connect_to_db(db_params)
        
        cursor = conn.cursor()
        insert_query = "INSERT INTO enrollee_education (enrollee_id, enrolled_university, education_level, major_discipline) VALUES (%s, %s, %s, %s);"
        
        for _, row in data.iterrows():
            cursor.execute(insert_query, (row["enrollee_id"], row["enrolled_university"], row["education_level"], row["major_discipline"]))
        
        conn.commit()
        print("Excel data added successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def load_training_hours(table):
    try:
        engine = create_engine('mysql+pymysql://etl_practice:550814@112.213.86.31:3360/company_course')
        data = pd.read_sql_table(table, con=engine)
        
        conn = connect_to_db(db_params)
        
        cursor = conn.cursor()
        insert_query = "INSERT INTO training_hours (enrollee_id, training_hours) VALUES (%s, %s);"
        
        for _, row in data.iterrows():
            cursor.execute(insert_query, (int(row["enrollee_id"]), int(row["training_hours"])))
        
        conn.commit()
        print("Training hours added successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def load_employment(table):
    try:
        engine = create_engine('mysql+pymysql://etl_practice:550814@112.213.86.31:3360/company_course')
        data = pd.read_sql_table(table, con=engine)
        
        conn = connect_to_db(db_params)
        
        cursor = conn.cursor()
        insert_query = "INSERT INTO employment (enrollee_id, employed) VALUES (%s, %s);"
        
        for _, row in data.iterrows():
            cursor.execute(insert_query, (int(row["enrollee_id"]), int(row["employed"])))
        
        conn.commit()
        print("Employment added successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


load_data_from_google_sheet("1VCkHwBjJGRJ21asd9pxW4_0z2PWuKhbLR3gUHm-p4GI", "enrollies")
load_csv_data("https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/work_experience.csv")
load_excel_data("enrollies_education.xlsx")
load_training_hours("training_hours")
load_employment("employment")