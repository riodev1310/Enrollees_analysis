import pandas as pd
from sqlalchemy import create_engine

def load_training_hours(table, writer):
    try:
        training_engine = create_engine('mysql+pymysql://etl_practice:550814@112.213.86.31:3360/company_course')
        data = pd.read_sql_table(table, con=training_engine)
        
        data.to_excel(writer, sheet_name="training_hours", index=False)  # Fixed typo in sheet_name
        print("Training hours saved successfully!!!")
    except Exception as e: 
        print(f"Error during connection: {e}")

def load_employment(table, writer):
    try:
        employment_engine = create_engine('mysql+pymysql://etl_practice:550814@112.213.86.31:3360/company_course')
        data = pd.read_sql_table(table, con=employment_engine)
        
        data.to_excel(writer, sheet_name="employment", index=False)
        print("Employment data saved successfully!!!")  # Updated message for clarity
    except Exception as e: 
        print(f"Error during connection: {e}")

# Use ExcelWriter to write to the same file
excel_file_name = "enrollees_status.xlsx"
with pd.ExcelWriter(excel_file_name, engine="openpyxl") as writer:
    load_training_hours("training_hours", writer)
    load_employment("employment", writer)