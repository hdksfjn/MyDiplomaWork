from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db.db_operations import *
from user.text_builder import *
from bot import *
from user.lecturer import send_lecturer_accept


def course_kb():
    inline_kb = InlineKeyboardMarkup(row_width=4)
    for i in range(3, 7):
        inline_btn = InlineKeyboardButton(str(i),
                                          callback_data=f'course_button_{str(i)}')
        inline_kb.insert(inline_btn)

    return inline_kb


async def user_university():
    univ_list = await search_university()

    inline_kb = InlineKeyboardMarkup()
    for i in range(len(univ_list)):
        inline_btn = InlineKeyboardButton(str(i+1), callback_data=f'university_button_{str(univ_list[i][0])}')
        inline_kb.insert(inline_btn)

    return user_university_view(univ_list), inline_kb


async def user_faculty(university_id):
    faculty_list = await search_faculty(university_id)

    inline_kb = InlineKeyboardMarkup()
    for i in range(len(faculty_list)):
        inline_btn = InlineKeyboardButton(str(i+1), callback_data=f'faculty_button_{str(faculty_list[i][0])}')
        inline_kb.insert(inline_btn)

    return user_faculty_view(faculty_list), inline_kb


async def user_department(faculty_id):
    department_list = await search_department(faculty_id)

    inline_kb = InlineKeyboardMarkup()
    for i in range(len(department_list)):
        inline_btn = InlineKeyboardButton(str(i+1), callback_data=f'department_button_{str(department_list[i][0])}')
        inline_kb.insert(inline_btn)

    return user_department_view(department_list), inline_kb


async def user_specialty(department_id):
    specialty_list = await search_specialty(department_id)

    inline_kb = InlineKeyboardMarkup()
    for i in range(len(specialty_list)):
        inline_btn = InlineKeyboardButton(str(i+1), callback_data=f'specialty_button_{str(specialty_list[i][0])}')
        inline_kb.insert(inline_btn)

    return user_specialty_view(specialty_list), inline_kb


async def user_topics(user_name, speciality_id):
    topics_list = await search_student_topics(user_name, speciality_id)

    inline_kb = InlineKeyboardMarkup()
    if topics_list:
        for i in range(len(topics_list)):
            inline_btn = InlineKeyboardButton(str(i+1), callback_data=f'topics_button_{str(topics_list[i][0])}')
            inline_kb.insert(inline_btn)

    return user_topics_view(topics_list), inline_kb


async def callback_course(callback_query):
    await add_course(callback_query.from_user.username, callback_query.data.lstrip('course_button_'))
    text, kb = await user_university()
    await bot.send_message(callback_query.from_user.id, text, reply_markup=kb)


async def callback_user_university(callback_query):
    university_id = callback_query.data.lstrip('university_button_')
    await set_user_university(callback_query.from_user.username, university_id)
    text, kb = await user_faculty(university_id)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=kb)


async def callback_user_faculty(callback_query):
    faculty_id = callback_query.data.lstrip('faculty_button_')
    await set_user_faculty(callback_query.from_user.username, faculty_id)
    text, kb = await user_department(faculty_id)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=kb)


async def callback_user_department(callback_query):
    department_id = callback_query.data.lstrip('department_button_')
    await set_user_department(callback_query.from_user.username, department_id)
    text, kb = await user_specialty(department_id)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=kb)


async def callback_user_specialty(callback_query):
    specialty_id = callback_query.data.lstrip('specialty_button_')
    await set_user_specialty(callback_query.from_user.username, specialty_id)
    text, kb = await user_topics(callback_query.from_user.username, specialty_id)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=kb)


async def callback_user_send_topic(callback_query):
    topic_id = callback_query.data.lstrip('topics_button_')
    lecturer_tg_id, topics_name = await lecturer_telegram_user_id_and_topic_name(topic_id)
    if lecturer_tg_id:
        await bot.send_message(callback_query.from_user.id, 'Обрану тему надіслано на узгодження викладачеві')
        await send_lecturer_accept(int(lecturer_tg_id), callback_query.from_user.username, topics_name, topic_id)
