import sqlite3
import supportFile
import datetime
import subject

class StudyDate:
    def __init__(self, id=None, date=None, subject_id=None):
        self.id = id
        self.date = date
        self.subject_id = subject_id

    @staticmethod
    def get_all():
        conn = sqlite3.connect(supportFile.dataBaseName)
        cursor = conn.cursor()
        cursor.execute("SELECT id, date, subject_id FROM StudyDate")
        rows = cursor.fetchall()
        study_dates = []
        for row in rows:
            study_dates.append(StudyDate(row[0], row[1], row[2]))
        conn.close()
        return study_dates

    @staticmethod
    def get_by_id(id):
        conn = sqlite3.connect(supportFile.dataBaseName)
        cursor = conn.cursor()
        cursor.execute("SELECT id, date, subject_id FROM StudyDate WHERE id=?", (id,))
        row = cursor.fetchone()
        study_date = None
        if row is not None:
            study_date = StudyDate(row[0], row[1], row[2])
        conn.close()
        return study_date

    def save(self):
        conn = sqlite3.connect(supportFile.dataBaseName)
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM Subject WHERE id=?", (self.subject_id,))
        row = cursor.fetchone()
        if row is None:
            raise ValueError("The subject with ID {} does not exist in the database.".format(self.subject_id))

        if self.id is None:
            cursor.execute("INSERT INTO StudyDate (date, subject_id) VALUES (?, ?)", (self.date, self.subject_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE StudyDate SET date=?, subject_id=? WHERE id=?", (self.date, self.subject_id, self.id))
        conn.commit()
        conn.close()


    def set_current_timestamp(self):
        self.date = datetime.datetime.now()

    def get_current_timestamp(self):
        return datetime.datetime.now()

    def get_timestamp_by_id(self, subject_id):
        conn = sqlite3.connect(supportFile.dataBaseName)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM StudyDate WHERE subject_id=?", (subject_id,))
        count = cursor.fetchone()[0]
        print(count)
        conn.close()
        current_timestamp = datetime.datetime.now()
        timestamp = current_timestamp + datetime.timedelta(weeks=count)
        return timestamp
    def get_subject(self):
        """Returns the Subject object associated with this StudyDate instance."""
        conn = sqlite3.connect(supportFile.dataBaseName)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Subject WHERE id=?", (self.subject_id,))
        subject_row = cursor.fetchone()
        conn.close()

        if subject_row is None:
            return None

        sub = subject.Subject(subject_row[0], subject_row[1])
        return sub
    def __str__(self):
        return f"id: {self.id}, subject_id: {self.subject_id}, dateTime: {self.date}"
