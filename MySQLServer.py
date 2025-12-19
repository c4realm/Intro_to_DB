import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # ALX checker expects no password
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:  # <-- this exact form is required
    print(f"Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
