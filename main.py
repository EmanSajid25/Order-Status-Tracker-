from fastapi import FastAPI
import pymysql

app = FastAPI()

# Database connection settings
DB_CONFIG = {
    "host": "172.21.184.158",
    "user": "root",
    "password": "$t@g3HcW@24",
    "database": "hcm_db_dev",
    "cursorclass": pymysql.cursor.DictCursor  # Makes results a list of dicts
}

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}

@app.get("/faculty")
def get_faculty():
    try:
        # Connect to DB
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Fetch all faculty data
        cursor.execute("SELECT * FROM faculty_data")
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return {"faculty": results}

    except Exception as e:
        print("Error fetching faculty data:", e)
        return {"error": str(e)}
