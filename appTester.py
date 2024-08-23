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
    print(df.columns)
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS overseas_importers;")
    cursor.execute("CREATE TABLE overseas_importers (Commodity varchar(255), Country varchar(255), Name_of_Company varchar(255), Address varchar(255), Address_Continued varchar(255), Contact_Information varchar(255));")
    for index, row in df.iterrows():

        values = [
            row['Commodity'] if pd.notna(row['Commodity']) else None,
            row['Country'] if pd.notna(row['Country']) else None,
            row['Name of Company'] if pd.notna(row['Name of Company']) else None,
            row['Address'] if pd.notna(row['Address']) else None,
            row.get("Address Cont'd") if pd.notna(row.get("Address Cont'd")) else None,
            row.get("Contact Information") if pd.notna(row.get("Contact Information")) else None
        ]

        cursor.execute(
            "INSERT INTO overseas_importers (Commodity, Country, Name_of_Company, Address, Address_Continued, Contact_Information) VALUES (%s, %s, %s, %s, %s, %s)",
            values
        )

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

