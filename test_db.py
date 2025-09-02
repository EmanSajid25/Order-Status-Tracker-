import pymysql

DB_CONFIG = {
    "host": "172.21.184.158",
    "port": 3306,
    "user": "root",
    "password": "$t@g3HcW@24",
    "database": "hcm_db_dev",
    "cursorclass": pymysql.cursors.DictCursor
}

try:
    print("🔄 Connecting to database...")
    conn = pymysql.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT DATABASE();")  # Simple test query
    result = cur.fetchone()
    print("✅ Connected! Current database:", result)
    cur.close()
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)

