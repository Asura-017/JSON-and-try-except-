import sqlite3

try:
    # Connect to the database
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()

    # Process results
    for row in results:
        print(row)

except sqlite3.OperationalError as e:
    print(f"Database error: {e}")
except sqlite3.DatabaseError as e:
    print(f"General database error: {e}")
finally:
    conn.close()  # Ensures the database connection is closed
