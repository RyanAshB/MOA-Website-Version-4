import mysql.connector

print("Hello World")


db_config = {
    'user': 'root',
    'password': 'password123',
    'host': 'localhost',
    'database': 'overseas_importers'

}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def overseas_form():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DESCRIBE overseas_importers;"
    cursor.execute(query, )

    headings=[]
    data = cursor.fetchall()
    for i in data:
        headings.append(i[0])
    print(headings)

    conn.commit()
    cursor.close()
    conn.close()
    
    return True

overseas_form()





