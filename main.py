from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from admin.admin_main import *
from user.student import *
from user.lecturer import *


dp = Dispatcher(bot)


@dp.callback_query_handler(lambda call: call.data and call.data.startswith('admin'))
@auth
async def process_callback_university(callback_query: types.CallbackQuery):
    if callback_query.data.startswith('admin_university'):
        await callback_university(callback_query)
    elif callback_query.data.startswith('admin_faculty'):
        await callback_faculty(callback_query)
    elif callback_query.data.startswith('admin_department'):
        await callback_department(callback_query)
    elif callback_query.data.startswith('admin_specialty'):
        await callback_specialty(callback_query)
    elif callback_query.data.startswith('admin_topics'):
        await callback_topics(callback_query)
    elif callback_query.data.startswith('admin_course'):
        await callback_admin_course(callback_query)


@dp.message_handler(text=['Підтвердити', 'Відмінити'])
@auth
async def process_admin_accept_command(message: types.Message):
    await admin_accept(message)


@dp.message_handler(text=['Додати данні'])
@auth
async def process_add_data_command(message: types.Message):
    text, buttons = await admin_university()
    await message.answer(text, reply_markup=buttons)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if message.chat.id == admin_id:
        await message.answer("Адмін Панель", reply_markup=admin_menu())
    else:
        if await is_lecturer(message.from_user.username, message.from_user.id):
            await message.answer('Вас додано до списку викладачів, очікуйте запити на підтведження тем від студентів')
        else:
            await add_user(message.from_user.username, message.from_user.id)
            await message.answer("Введіть ваше прізвище та ім'я:")


@dp.callback_query_handler(lambda call: call.data and call.data.startswith('lecturer'))
async def process_callback_university(callback_query: types.CallbackQuery):
    await callback_lecturer(callback_query)


@dp.message_handler(lambda message: message.chat.id == admin_id)
@auth
async def process_save_data_command(message: types.Message):
    await save_data(message)


@dp.callback_query_handler(lambda call: call.data and not call.data.startswith('admin'))
async def process_callback_university(callback_query: types.CallbackQuery):
    if callback_query.data.startswith('course_button'):
        await callback_course(callback_query)
    elif callback_query.data.startswith('university_button'):
        await callback_user_university(callback_query)
    elif callback_query.data.startswith('faculty_button'):
        await callback_user_faculty(callback_query)
    elif callback_query.data.startswith('department_button'):
        await callback_user_department(callback_query)
    elif callback_query.data.startswith('specialty_button'):
        await callback_user_specialty(callback_query)
    elif callback_query.data.startswith('topics_button'):
        await callback_user_send_topic(callback_query)


@dp.message_handler(lambda message: message.chat.id != admin_id)
async def process_save_data_command(message: types.Message):
    if not await is_lecturer(message.from_user.username, message.from_user.id):
        await add_first_last_name(message.from_user.username, message.text)
        await message.answer("Оберіть курс:", reply_markup=course_kb())


async def on_startup(_):
    pass


executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
