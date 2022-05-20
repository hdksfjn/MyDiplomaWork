from admin.admin_buttons import *
from bot import *
from db.db_operations import *
from db.db import *


def auth(func):
    async def wrapper(message):
        if message['from']['id'] != admin_id:
            return await message.answer('Access Denied')
        return await func(message)

    return wrapper


async def back_to_admin_main(user_id):
    await bot.send_message(user_id, "Адмін Панель", reply_markup=admin_menu())


async def back_to_admin_university(user_id):
    text, buttons = await admin_university()
    await bot.send_message(user_id, university_name_text_builder(admin_temp_data, True))
    await bot.send_message(user_id, text, reply_markup=buttons)


async def back_to_admin_faculty(user_id):
    text, buttons = await admin_faculty()
    await bot.send_message(user_id, faculty_name_text_builder(admin_temp_data, True))
    await bot.send_message(user_id, text, reply_markup=buttons)


async def back_to_admin_department(user_id):
    text, buttons = await admin_department()
    await bot.send_message(user_id, department_name_text_builder(admin_temp_data, True))
    await bot.send_message(user_id, text, reply_markup=buttons)


async def back_to_admin_specialty(user_id):
    text, buttons = await admin_specialty()
    await bot.send_message(user_id, specialty_name_text_builder(admin_temp_data, True))
    await bot.send_message(user_id, text, reply_markup=buttons)


async def send_admin_faculty(user_id):
    text, buttons = await admin_faculty()
    await bot.send_message(user_id, university_name_text_builder(admin_temp_data, True))
    await bot.send_message(user_id, text, reply_markup=buttons)


async def send_admin_department(user_id):
    text, buttons = await admin_department()
    await bot.send_message(user_id, faculty_name_text_builder(admin_temp_data, True))
    await bot.send_message(user_id, text, reply_markup=buttons)


async def send_admin_specialty(user_id):
    text, buttons = await admin_specialty()
    await bot.send_message(user_id, department_name_text_builder(admin_temp_data, True))
    await bot.send_message(user_id, text, reply_markup=buttons)


async def send_admin_topics(user_id):
    text, buttons = await admin_topics()
    await bot.send_message(user_id, specialty_name_text_builder(admin_temp_data, True))
    await bot.send_message(user_id, text, reply_markup=buttons)


async def callback_university(callback_query):
    if callback_query.data == "admin_university_button_add":
        await callback_query.answer('Введіть назву університету:')
        admin_temp_data['wait_for_university_name'] = True

    elif callback_query.data == "admin_university_button_back":
        await back_to_admin_main(callback_query.from_user.id)

    else:
        university_id = callback_query.data.lstrip('admin_university_button_')
        admin_temp_data['university_name'] = admin_temp_data['university'][int(university_id)]
        admin_temp_data['university_id'] = university_id
        await send_admin_faculty(callback_query.from_user.id)


async def callback_faculty(callback_query):
    if callback_query.data == "admin_faculty_button_add":
        await callback_query.answer('Введіть назву факультету:')
        admin_temp_data['wait_for_faculty_name'] = True

    elif callback_query.data == "admin_faculty_button_back":
        await back_to_admin_university(callback_query.from_user.id)

    else:
        faculty_id = callback_query.data.lstrip('admin_faculty_button_')
        admin_temp_data['faculty_name'] = admin_temp_data['faculty'][int(faculty_id)]
        admin_temp_data['faculty_id'] = faculty_id
        await send_admin_department(callback_query.from_user.id)


async def callback_department(callback_query):
    if callback_query.data == "admin_department_button_add":
        await callback_query.answer('Введіть назву кафедри:')
        admin_temp_data['wait_for_department_name'] = True

    elif callback_query.data == "admin_department_button_back":
        await back_to_admin_faculty(callback_query.from_user.id)

    else:
        department_id = callback_query.data.lstrip('admin_department_button_')
        admin_temp_data['department_name'] = admin_temp_data['department'][int(department_id)]
        admin_temp_data['department_id'] = department_id
        await send_admin_specialty(callback_query.from_user.id)


async def callback_specialty(callback_query):
    if callback_query.data == "admin_specialty_button_add":
        await callback_query.answer('Введіть назву спеціальності:')
        admin_temp_data['wait_for_specialty_name'] = True

    elif callback_query.data == "admin_specialty_button_back":
        await back_to_admin_department(callback_query.from_user.id)

    else:
        specialty_id = callback_query.data.lstrip('admin_specialty_button_')
        admin_temp_data['specialty_name'] = admin_temp_data['specialty'][int(specialty_id)]
        admin_temp_data['specialty_id'] = specialty_id
        await send_admin_topics(callback_query.from_user.id)


async def callback_topics(callback_query):
    if callback_query.data == "admin_topics_button_add":
        await bot.send_message(admin_id, 'Введіть телеграм @username викладача:')
        admin_temp_data['wait_for_lecturer_name'] = True

    elif callback_query.data == "admin_topics_button_back":
        await back_to_admin_specialty(callback_query.from_user.id)

    elif callback_query.data == "admin_topics_button_full_back":
        await back_to_admin_main(callback_query.from_user.id)


async def callback_admin_course(callback_query):
    admin_temp_data['course'] = int(callback_query.data.lstrip('admin_course_button_'))
    await check_confirm(callback_query.from_user.id)


async def accept_university(message):
    try:
        admin_temp_data['university_id'] = await add_university(admin_temp_data)  # save name to db
        await message.answer(university_name_text_builder(admin_temp_data))  # send confirm to user
        admin_temp_data['wait_for_university_name'] = False  # disable name
        text, buttons = await admin_faculty()
        await message.answer(text, reply_markup=buttons)
    except:
        pass


async def accept_faculty(message):
    admin_temp_data['faculty_id'] = await add_faculty(admin_temp_data)  # save name to db
    try:
        await message.answer(faculty_name_text_builder(admin_temp_data))  # send confirm to user
        admin_temp_data['wait_for_faculty_name'] = False  # disable name
        text, buttons = await admin_department()
        await message.answer(text, reply_markup=buttons)
    except:
        pass


async def accept_department(message):
    admin_temp_data['department_id'] = await add_department(admin_temp_data)  # save name to db
    try:
        await message.answer(department_name_text_builder(admin_temp_data))  # send confirm to user
        admin_temp_data['wait_for_department_name'] = False  # disable name
        text, buttons = await admin_specialty()
        await message.answer(text, reply_markup=buttons)
    except:
        pass


async def accept_specialty(message):
    admin_temp_data['specialty_id'] = await add_specialty(admin_temp_data)  # save name to db
    try:
        await message.answer(specialty_name_text_builder(admin_temp_data))  # send confirm to user
        admin_temp_data['wait_for_specialty_name'] = False  # disable name
        text, buttons = await admin_topics()
        await message.answer(text, reply_markup=buttons)
    except:
        pass


async def accept_topic(message):
    try:
        await add_topics(admin_temp_data)  # save name to db
        admin_temp_data['wait_for_course'] = False
        text, buttons = await admin_topics()
        await message.answer(text, reply_markup=buttons)
    except:
        pass


def clear_name(name):
    admin_temp_data[f'wait_for_{name}_name'] = False  # disable name
    admin_temp_data[f'{name}_name'] = ''  # clear name


async def decline_university(message):
    clear_name('university')
    text, buttons = await admin_university()
    await message.answer(text, reply_markup=buttons)


async def decline_faculty(message):
    clear_name('faculty')
    text, buttons = await admin_faculty()
    await message.answer(text, reply_markup=buttons)


async def decline_department(message):
    clear_name('department')
    text, buttons = await admin_department()
    await message.answer(text, reply_markup=buttons)


async def decline_specialty(message):
    clear_name('specialty')
    text, buttons = await admin_specialty()
    await message.answer(text, reply_markup=buttons)


async def decline_topic(message):
    clear_name('topic')
    text, buttons = await admin_topics()
    await message.answer(text, reply_markup=buttons)


async def accept(message):
    if admin_temp_data['wait_for_university_name']:
        await accept_university(message)

    elif admin_temp_data['wait_for_faculty_name']:
        await accept_faculty(message)

    elif admin_temp_data['wait_for_department_name']:
        await accept_department(message)

    elif admin_temp_data['wait_for_specialty_name']:
        await accept_specialty(message)

    elif admin_temp_data['wait_for_course']:
        await accept_topic(message)


async def decline(message):
    if admin_temp_data['wait_for_university_name']:
        await decline_university(message)

    elif admin_temp_data['wait_for_faculty_name']:
        await decline_faculty(message)

    elif admin_temp_data['wait_for_department_name']:
        await decline_department(message)

    elif admin_temp_data['wait_for_specialty_name']:
        await decline_specialty(message)

    elif admin_temp_data['wait_for_course']:
        await decline_topic(message)


async def admin_accept(message):
    if message.text == 'Підтвердити':
        await accept(message)

    elif message.text == 'Відмінити':
        await decline(message)


async def save_data(message):
    if admin_temp_data['wait_for_university_name']:
        admin_temp_data['university_name'] = message.text
        await check_confirm(message.from_user.id)

    elif admin_temp_data['wait_for_faculty_name']:
        admin_temp_data['faculty_name'] = message.text
        await check_confirm(message.from_user.id)

    elif admin_temp_data['wait_for_department_name']:
        admin_temp_data['department_name'] = message.text
        await check_confirm(message.from_user.id)

    elif admin_temp_data['wait_for_specialty_name']:
        admin_temp_data['specialty_name'] = message.text
        await check_confirm(message.from_user.id)

    elif admin_temp_data['wait_for_lecturer_name']:  # send  lecturer username -> topic -> course buttons
        admin_temp_data['lecturer_name'] = message.text
        admin_temp_data['wait_for_lecturer_name'] = False
        admin_temp_data['wait_for_topic_name'] = True
        await message.answer('Введіть назву теми:')

    elif admin_temp_data['wait_for_topic_name']:
        admin_temp_data['topic_name'] = message.text
        admin_temp_data['wait_for_topic_name'] = False
        admin_temp_data['wait_for_course'] = True
        await message.reply('Оберіть курс:', reply_markup=admin_course())
