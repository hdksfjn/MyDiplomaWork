create table university(
    id integer primary key,
    university_name varchar(255)
);

create table faculty(
    id integer primary key,
    faculty_name varchar(255),
    university_id integer,
    FOREIGN KEY(university_id) REFERENCES university(id)
);

create table department(
    id integer primary key,
    department_name varchar(255),
    faculty_id integer,
    FOREIGN KEY(faculty_id) REFERENCES faculty(id)
);

create table specialty(
    id integer primary key,
    specialty_name varchar(255),
    department_id integer,
    FOREIGN KEY(department_id) REFERENCES department(id)
);

create table topics(
    id integer primary key,
    topics_name varchar(255),
    student_id integer,
    lecturer_id integer,
    specialty_id integer,
    course integer,
    FOREIGN KEY(specialty_id) REFERENCES specialty(id),
    FOREIGN KEY(lecturer_id) REFERENCES users(id),
    FOREIGN KEY(student_id) REFERENCES users(id)
);

create table users(
    id integer primary key,
    user_name varchar(255),
    first_last_name varchar(255),
    user_type integer,
    university_id integer,
    faculty_id integer,
    department_id integer,
    specialty_id integer,
    course integer,
    telegram_user_id integer,
    FOREIGN KEY(university_id) REFERENCES university(id),
    FOREIGN KEY(faculty_id) REFERENCES faculty(id),
    FOREIGN KEY(department_id) REFERENCES department(id),
    FOREIGN KEY(specialty_id) REFERENCES specialty(id)

);
