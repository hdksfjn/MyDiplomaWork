from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from db.db import *
from db.db_operations import *
from admin.admin_text_builder import *
from bot import *


async def check_confirm(user_id):
    accept_button = KeyboardButton('Підтвердити')
    decline_button = KeyboardButton('Відмінити')

    kb = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    ).add(accept_button, decline_button)

    await bot.send_message(user_id, 'Ви впевнені ?', reply_markup=kb)


def admin_menu():
    data_button = KeyboardButton('Додати данні')
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    ).add(data_button)
    return kb


async def admin_university():
    univ_list = await search_university()

    inline_kb = InlineKeyboardMarkup()
    for i in range(len(univ_list)):
        admin_temp_data['university'][univ_list[i][0]] = univ_list[i][1]
        inline_btn = InlineKeyboardButton(str(i+1), callback_data=f'admin_university_button_{str(univ_list[i][0])}')
        inline_kb.insert(inline_btn)

    button_add = InlineKeyboardButton('Додати університет', callback_data=f'admin_university_button_add')
    button_back = InlineKeyboardButton('⬅️Назад', callback_data=f'admin_university_button_back')

    inline_kb.row(button_back, button_add)

    return admin_university_view(univ_list), inline_kb


async def admin_faculty():
    faculty_list = await search_faculty(admin_temp_data['university_id'])

    inline_kb = InlineKeyboardMarkup()
    for i in range(len(faculty_list)):
        admin_temp_data['faculty'][faculty_list[i][0]] = faculty_list[i][1]
        inline_btn = InlineKeyboardButton(str(i+1), callback_data=f'admin_faculty_button_{str(faculty_list[i][0])}')
        inline_kb.insert(inline_btn)

    button_add = InlineKeyboardButton('Додати факультет', callback_data=f'admin_faculty_button_add')
    button_back = InlineKeyboardButton('⬅️Назад', callback_data=f'admin_faculty_button_back')

    inline_kb.row(button_back, button_add)

    return admin_faculty_view(faculty_list), inline_kb


async def admin_department():
    department_list = await search_department(admin_temp_data['faculty_id'])

    inline_kb = InlineKeyboardMarkup()
    for i in range(len(department_list)):
        admin_temp_data['department'][department_list[i][0]] = department_list[i][1]
        inline_btn = InlineKeyboardButton(str(i+1), callback_data=f'admin_department_button_{str(department_list[i][0])}')
        inline_kb.insert(inline_btn)

    button_add = InlineKeyboardButton('Додати кафедру', callback_data=f'admin_department_button_add')
    button_back = InlineKeyboardButton('⬅️Назад', callback_data=f'admin_department_button_back')

    inline_kb.row(button_back, button_add)

    return admin_department_view(department_list), inline_kb


async def admin_specialty():
    specialty_list = await search_specialty(admin_temp_data['department_id'])

    inline_kb = InlineKeyboardMarkup()
    for i in range(len(specialty_list)):
        admin_temp_data['specialty'][specialty_list[i][0]] = specialty_list[i][1]
        inline_btn = InlineKeyboardButton(str(i+1), callback_data=f'admin_specialty_button_{str(specialty_list[i][0])}')
        inline_kb.insert(inline_btn)

    button_add = InlineKeyboardButton('Додати спеціальність', callback_data=f'admin_specialty_button_add')
    button_back = InlineKeyboardButton('⬅️Назад', callback_data=f'admin_specialty_button_back')

    inline_kb.row(button_back, button_add)

    return admin_specialty_view(specialty_list), inline_kb


async def admin_topics():
    inline_kb = InlineKeyboardMarkup()

    button_add = InlineKeyboardButton('Додати тему', callback_data=f'admin_topics_button_add')
    button_back = InlineKeyboardButton('⬅️Назад', callback_data=f'admin_topics_button_back')
    button_full_back = InlineKeyboardButton('⬅️Адмін панель', callback_data=f'admin_topics_button_full_back')

    inline_kb.row(button_back, button_add)
    inline_kb.row(button_full_back)

    topics_list = await search_topics(admin_temp_data['specialty_id'])

    return admin_topics_view(topics_list), inline_kb


def admin_course():
    inline_kb = InlineKeyboardMarkup(row_width=4)
    for i in range(3, 7):
        inline_btn = InlineKeyboardButton(str(i),
                                          callback_data=f'admin_course_button_{str(i)}')
        inline_kb.insert(inline_btn)

    return inline_kb
