import pandas as pd
import psycopg2

db_params = {
    "host": "localhost",
    "port": "5435",
    "database": "pipeline",
    "user": "vietanlms",
    "password": "lmspipeline"
}
# Define a function to fetch and combine data from multiple tables
def fetch_and_combine_data():
    try:
        # Establish the database connection
        connection = psycopg2.connect(**db_params)

        # Query to fetch data from all tables
        query = """
        SELECT e.enrollee_id, e.full_name, e.city, e.gender,
               edu.enrolled_university, edu.education_level, edu.major_discipline,
               we.relevent_experience, we.experience, we.company_size, 
               we.company_type, we.last_new_job,
               th.training_hours, emp.employed
        FROM enrollees e
        LEFT JOIN enrollee_education edu ON e.enrollee_id = edu.enrollee_id
        LEFT JOIN work_experience we ON e.enrollee_id = we.enrollee_id
        LEFT JOIN training_hours th ON e.enrollee_id = th.enrollee_id
        LEFT JOIN employment emp ON e.enrollee_id = emp.enrollee_id
        """

        # Fetch data into a DataFrame
        df = pd.read_sql_query(query, connection)

        # Save the DataFrame to a CSV file
        df.to_csv("combined_data.csv", index=False)

        print("Data successfully saved to combined_data.csv")

    except Exception as e:
        print("Error fetching data:", e)
        return None

    finally:
        # Close the database connection
        if connection:
            connection.close()

fetch_and_combine_data()