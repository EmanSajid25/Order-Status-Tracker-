import pymysql

# Connect to MySQL
try:
    connection = pymysql.connect(
        host='172.21.184.158',
        user='root',
        password='$t@g3HcW@24',
        database='hcm_db_dev'
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM faculty_data")
        results = cursor.fetchall()  # Fetch all rows

        print("Connected to the remote MySQL database. Faculty Data:")
        for row in results:
            print(row)

    connection.close()

except Exception as e:
    print("Error while connecting to MySQL:", e)






