import mysql.connector
import pandas as pd
from tkinter import *
from tkinter import filedialog

print("Hello World")


db_config = {
    'user': 'root',
    'password': 'password123',
    'host': 'localhost',
    'database': 'overseas_importers'

}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def submit_form(file):
    df = pd.read_excel(file)
    print(df.columns)
    df.columns = df.columns.str.strip()
    print(len(df.columns))
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace("'", "")
    print(df.columns)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS overseas_importers;")
    cursor.execute(f"CREATE TABLE overseas_importers ({df.columns[0]} varchar(255));")

    i=1
    while i < len(df.columns):
        cursor.execute(f"ALTER TABLE overseas_importers ADD {df.columns[i]} varchar(255);")
        print(df.columns[i])
        i=i+1

    my_s = ", ".join(["%s"] * len(df.columns))
    query = f"INSERT INTO overseas_importers ({', '.join([f'`{col}`' for col in df.columns])}) VALUES ({my_s});"

    for index, row in df.iterrows():
        values = [row[col] if pd.notna(row[col]) else None for col in df.columns]
        cursor.execute(query, tuple(values))


    conn.commit()
    cursor.close()
    conn.close()
    
    return True


def openFile():
    filepath = filedialog.askopenfilename()
    print(filepath)
    submit_form(filepath)

window = Tk()
button = Button(text="Open", command=openFile)
button.pack()
window.mainloop()

