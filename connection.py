import sqlite3
import supportFile
# create a connection to the database
conn = sqlite3.connect(supportFile.dataBaseName)

# create a cursor object to interact with the database
cursor = conn.cursor()
try:
    # create the Subject table
    cursor.execute('''CREATE TABLE Subject
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(255) NOT NULL)''')

    # create the StudyDate table
    cursor.execute('''CREATE TABLE StudyDate
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       date TIMESTAMP NOT NULL,
                       subject_id INTEGER NOT NULL,
                       FOREIGN KEY (subject_id) REFERENCES Subject(id))''')
except:
    print("didnt create new tables")
# commit changes and close the connection
conn.commit()
conn.close()
