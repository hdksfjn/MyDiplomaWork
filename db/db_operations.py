from db.db import db, cursor


async def add_university(data):
    university_id = cursor.execute(
        f"INSERT INTO university (university_name) VALUES (\'{data['university_name']}\')").lastrowid
    db.commit()
    return university_id


async def add_faculty(data):
    faculty_id = cursor.execute(
        f"INSERT INTO faculty (faculty_name, university_id) VALUES (\'{data['faculty_name']}\', \'{data['university_id']}\')").lastrowid
    db.commit()
    return faculty_id


async def add_department(data):
    department_id = cursor.execute(
        f"INSERT INTO department (department_name, faculty_id) VALUES (\'{data['department_name']}\', \'{data['faculty_id']}\')").lastrowid
    db.commit()
    return department_id


async def add_specialty(data):
    specialty_id = cursor.execute(
        f"INSERT INTO specialty (specialty_name, department_id) VALUES (\'{data['specialty_name']}\', \'{data['department_id']}\')").lastrowid
    db.commit()
    return specialty_id


async def add_topics(data):
    lecturer_id = cursor.execute(f"SELECT id FROM users WHERE user_name=\'{data['lecturer_name']}\'").fetchall()
    if not lecturer_id:
        lecturer_id = cursor.execute(
            f"INSERT INTO users (user_name, user_type) VALUES (\'{data['lecturer_name']}\', 1)").lastrowid  # 1 is lecturer, 0 is student
        db.commit()
    else:
        lecturer_id = lecturer_id[0][0]

    cursor.execute(
        f"INSERT INTO topics (topics_name, specialty_id, lecturer_id, course) VALUES (\'{data['topic_name']}\', \'{data['specialty_id']}\', \'{str(lecturer_id)}\', \'{data['course']}\')")
    db.commit()


async def search_university():
    return cursor.execute(f"SELECT * FROM university").fetchall()


async def search_faculty(university_id):
    return cursor.execute(
        f"SELECT id, faculty_name FROM faculty WHERE university_id={university_id}").fetchall()


async def search_department(faculty_id):
    return cursor.execute(
        f"SELECT id, department_name FROM department WHERE faculty_id={faculty_id}").fetchall()


async def search_specialty(department_id):
    return cursor.execute(
        f"SELECT id, specialty_name FROM specialty WHERE department_id={department_id}").fetchall()


async def search_topics(specialty_id):
    data = list(cursor.execute(
        f"SELECT id, topics_name, lecturer_id, course FROM topics WHERE specialty_id={specialty_id}").fetchall())

    if not data:
        return

    for i in range(len(data)):
        user_name = cursor.execute(
            f"SELECT user_name FROM users WHERE id={str(data[i][2])}").fetchall()
        user_name = user_name[0][0]
        data[i] = list(data[i])
        data[i][2] = user_name

    return data


async def add_user(user_name, telegram_user_id, user_type=0):
    data = cursor.execute(
        f"SELECT * FROM users WHERE user_name=\'@{user_name}\'").fetchall()

    if not data:
        cursor.execute(
            f"INSERT INTO users (user_type, user_name, telegram_user_id) VALUES (\'{user_type}\', \'{'@' + user_name if user_name is not None else user_name}\', \'{telegram_user_id}\')")
        db.commit()


async def add_first_last_name(user_name, first_last_name):
    cursor.execute(
        f"UPDATE users SET first_last_name=\'{first_last_name}\' WHERE user_name=\'@{user_name}\'")
    db.commit()


async def add_course(user_name, course):
    cursor.execute(
        f"UPDATE users SET course={course} WHERE user_name=\'@{user_name}\'").fetchall()
    db.commit()


async def set_user_university(user_name, university_id):
    cursor.execute(
        f"UPDATE users SET university_id={university_id} WHERE user_name=\'@{user_name}\'").fetchall()
    db.commit()


async def set_user_faculty(user_name, faculty_id):
    cursor.execute(
        f"UPDATE users SET faculty_id={faculty_id} WHERE user_name=\'@{user_name}\'").fetchall()
    db.commit()


async def set_user_department(user_name, department_id):
    cursor.execute(
        f"UPDATE users SET department_id={department_id} WHERE user_name=\'@{user_name}\'").fetchall()
    db.commit()


async def set_user_specialty(user_name, specialty_id):
    cursor.execute(
        f"UPDATE users SET specialty_id={specialty_id} WHERE user_name=\'@{user_name}\'").fetchall()
    db.commit()


async def search_student_topics(user_name, specialty_id):
    course = cursor.execute(
        f"SELECT course FROM users WHERE user_name=\'@{user_name}\'").fetchall()[0][0]

    data = list(cursor.execute(
        f"SELECT id, topics_name, lecturer_id, course FROM topics WHERE specialty_id={specialty_id} AND course={course} AND student_id IS NULL").fetchall())

    if not data:
        return

    for i in range(len(data)):
        user_name = cursor.execute(
            f"SELECT user_name FROM users WHERE id={str(data[i][2])}").fetchall()
        user_name = user_name[0][0]
        data[i] = list(data[i])
        data[i][2] = user_name

    return data


async def is_lecturer(user_name, user_id):
    lecturer = cursor.execute(
        f"SELECT count(*) FROM users WHERE user_name=\'@{user_name}\' AND user_type=1").fetchall()  # user_type bool
    if not lecturer or int(lecturer[0][0]) == 1:
        cursor.execute(
            f"UPDATE users SET telegram_user_id={user_id} WHERE user_name=\'@{user_name}\'").fetchall()
        db.commit()
        return True
    else:
        return False


async def lecturer_telegram_user_id_and_topic_name(topic_id):
    data = cursor.execute(
        f"SELECT lecturer_id, topics_name FROM topics WHERE id={topic_id}").fetchall()[0]
    lecturer_id, topics_name = data
    telegram_user_id = cursor.execute(
        f"SELECT telegram_user_id FROM users WHERE id={lecturer_id}").fetchall()

    if telegram_user_id:
        return telegram_user_id[0][0], topics_name


async def search_user(user_name):
    telegram_user_id = cursor.execute(
        f"SELECT telegram_user_id FROM users WHERE user_name=\'@{user_name}\'").fetchall()[0][0]
    return telegram_user_id


async def select_topic(topic_id, student_id):
    cursor.execute(
        f"UPDATE topics SET student_id={student_id} WHERE id={topic_id}").fetchall()
    db.commit()
