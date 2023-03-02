import sqlite3
import connection
import supportFile
import studyDate

class Subject:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    def __str__(self):
        return f"name :{self.name}, id: {self.id}"
    @staticmethod
    def get_all():
        conn = sqlite3.connect(supportFile.dataBaseName)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM Subject")
        rows = cursor.fetchall()
        subjects = []
        for row in rows:
            subjects.append(Subject(row[0], row[1]))
        conn.close()
        return subjects

    @staticmethod
    def get_by_id(id):
        conn = sqlite3.connect(supportFile.dataBaseName)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM Subject WHERE id=?", (id,))
        row = cursor.fetchone()
        subject = None
        if row is not None:
            subject = Subject(row[0], row[1])
        conn.close()
        return subject

    def save(self):
            conn = sqlite3.connect(supportFile.dataBaseName)
            cursor = conn.cursor()

            # Check if a subject with the same name already exists in the database
            cursor.execute("SELECT id FROM Subject WHERE name=?", (self.name,))
            row = cursor.fetchone()
            if row is not None and (self.id is None or row[0] != self.id):
                raise ValueError("A subject with the same name already exists in the database.")

            if self.id is None:
                cursor.execute("INSERT INTO Subject (name) VALUES (?)", (self.name,))
                self.id = cursor.lastrowid
            else:
                cursor.execute("UPDATE Subject SET name=? WHERE id=?", (self.name, self.id))
            conn.commit()

def printAll(subjects):
    for sub in subjects:
        print(sub)
#if __name__ == "__main__":
#    t = Subject(None,"This subject")
#
#    t.save()
#    printAll(Subject.get_all())
#

if __name__ == "__main__":
    supportFile.dataBaseName = "mydatabase.db"
    # Open a connection to the database
    conn = sqlite3.connect(supportFile.dataBaseName)
    c = conn.cursor()

    # Drop the tables if they exist
    c.execute("DROP TABLE IF EXISTS StudyDate")
    c.execute("DROP TABLE IF EXISTS Subject")

    # Create the tables
    with open("dataBaseScheme.sql") as f:
        schema = f.read()
    c.executescript(schema)

    # Commit the changes
    conn.commit()
    # Test the Subject class
    subject1 = Subject(name="Math")
    subject1.save()
    subject2 = Subject(name="History")
    subject2.save()
    subject3 = Subject(name="English")
    subject3.save()
    subject4 = Subject(name="Math") # Should raise an exception
    try:
        subject4.save()
    except Exception as e:
        print("Caught exception:", e)

    subjects = Subject.get_all()
    for subject in subjects:
        print(subject)

    # Test the StudyDate class
    study1 = studyDate.StudyDate(subject_id=1)
    study1.set_current_timestamp()
    study1.save()
    study2 = studyDate.StudyDate(subject_id=2)
    study2.set_current_timestamp()
    study2.save()
    study3 = studyDate.StudyDate(subject_id=3)
    study3.set_current_timestamp()
    study3.save()

    studies = studyDate.StudyDate.get_all()
    for study in studies:
        print(study)
        print(study.get_subject())

    study8 = studyDate.StudyDate(subject_id=2)
    study8.set_current_timestamp()
    study8.save()
    timestamp = study2.get_timestamp_by_id(2)
    print(study2)
    studyDatesThings = studyDate.StudyDate.get_all()
    print('')
    for d in studyDatesThings:
        print(d)
    print("Timestamp:", timestamp)
