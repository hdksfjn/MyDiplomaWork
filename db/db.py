import os
import sqlite3

path = 'db/'  # db path
db = sqlite3.connect(os.path.join(path, "MyDiplomaWork.db"))
cursor = db.cursor()


admin_temp_data = dict(wait_for_university_name=False, wait_for_faculty_name=False, wait_for_department_name=False,
                       wait_for_specialty_name=False, wait_for_lecturer_name=False, wait_for_topic_name=False,
                       wait_for_course=False, university_id=None, faculty_id=None, department_id=None, specialty_id=None,
                       university={}, faculty={}, department={}, specialty={})


def _init_db():
    with open(os.path.join(path, "create_db.sql"), "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    db.commit()


def check_db_exists():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='university'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()
