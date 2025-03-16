import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

db_params = {
    "host": "localhost",
    "port": "5435",
    "database": "courses_analysis",
    "user": "vietanlms",
    "password": "lmspipeline"
}

engine = create_engine(f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")

def connect_to_db(db_params):
    print("Connecting to PostgreSQL...")
    conn = psycopg2.connect(**db_params)
    return conn


def load_data_from_google_sheet(google_sheet_id, sheet_name):
    try:
        url='https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=xlsx'
        data = pd.read_excel(url, sheet_name=sheet_name)
        data["gender"] = data["gender"].fillna("other").str.lower()
        
        table_name = "enrollees"
        data.to_sql(table_name, engine, if_exists="replace", index=False)
        print("Google sheet data added successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")


def load_csv_data(link):
    try:
        data = pd.read_csv(link)
        data["experience"] = data["experience"].fillna(data["experience"].mode().values[0]).str.lower()
        data["company_size"] = data["company_size"].fillna("unknown").str.lower()
        data["company_type"] = data["company_type"].fillna("unknown").str.lower()
        data["last_new_job"] = data["last_new_job"].fillna(data["last_new_job"].mode().values[0]).str.lower()
        
        table_name = "work_experience"
        data.to_sql(table_name, engine, if_exists="replace", index=False)
        
        print("CSV data added successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")


def load_data_from_web(url):
    try:
        print("Fetching data from website...")
        city_dev_index = pd.read_html(url)
        
        table_name = "city_development_index"
        city_dev_index[0].to_sql(table_name, engine, if_exists="replace", index=False)
        
        print("City Development Index data added successfully!!!")
    except Exception as e:
        print(f"Error during connection: {e}")
            
            
def load_excel_data(file_path):
    try:
        data = pd.read_excel(file_path)
        data["enrolled_university"] = data["enrolled_university"].fillna(data["enrolled_university"].mode().values[0]).str.lower()
        data["education_level"] = data["education_level"].fillna(data["education_level"].mode().values[0]).str.lower()
        data["major_discipline"] = data["major_discipline"].fillna(data["major_discipline"].mode().values[0]).str.lower()
        
        table_name = "enrollies_education"
        data.to_sql(table_name, engine, if_exists="replace", index=False)
        
        print("Excel data added successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")


def load_training_hours(table):
    try:
        training_engine = create_engine('mysql+pymysql://etl_practice:550814@112.213.86.31:3360/company_course')
        data = pd.read_sql_table(table, con=training_engine)
        
        table_name = "training_hours"
        data.to_sql(table_name, engine, if_exists="replace", index=False)
        
        print("Training hours added successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")


def load_employment(table):
    try:
        employment_engine = create_engine('mysql+pymysql://etl_practice:550814@112.213.86.31:3360/company_course')
        data = pd.read_sql_table(table, con=employment_engine)
        
        table_name = "employment"
        data.to_sql(table_name, engine, if_exists="replace", index=False)
        print("Employment added successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")


def load_advertisement_metrics():
    # Tạo bảng và lưu dữ liệu
    table_name = "advertisement_metrics"
    campaign_df_1000 = pd.read_csv("Advertisement_Metrics.csv")
    campaign_df_1000.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"CSV data added successfully!!!")
    

load_data_from_google_sheet("1QtnqUow-yriu4qQDjjgZu2BZSsEA1ORzDuh8G91zzz4", "enrollies")
load_csv_data("https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/work_experience.csv")
load_excel_data("enrollies_education.xlsx")
load_training_hours("training_hours")
load_data_from_web("https://sca-programming-school.github.io/city_development_index/index.html")
load_employment("employment")
load_advertisement_metrics()