from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db.db_operations import *
from bot import *


async def send_lecturer_accept(lecturer_tg_id, user_name, topics_name, topic_id):
    inline_kb = InlineKeyboardMarkup()
    accept_button = InlineKeyboardButton('Закріпити тему', callback_data=f'lecturer_button_accept_{topic_id}@{user_name}')
    decline_button = InlineKeyboardButton('Відмовити', callback_data=f'lecturer_button_decline_{topic_id}@{user_name}')

    inline_kb.row(accept_button, decline_button)

    await bot.send_message(lecturer_tg_id, f"@{user_name}, {topics_name}", reply_markup=inline_kb)


async def callback_lecturer(callback_query):
    button = callback_query.data.lstrip('lecturer_button_')
    if 'accept' in button:
        topic_id, user_name = button.strip('accept_').split('@')
        student_id = await search_user(user_name)
        await select_topic(topic_id, student_id)
        await bot.send_message(student_id, 'Обрана тема закріплена за вами')
    else:
        topic_id, user_name = button.strip('decline_').split('@')
        student_id = await search_user(user_name)
        await bot.send_message(student_id, 'Обрану тему не схвалено оберіть іншу')
