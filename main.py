from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import const

bot = Bot(token = const.TOKEN_BOT, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot)



try:
    button_history = KeyboardButton('История')
    button_consumption = KeyboardButton('Добавить расходы')
    button_income = KeyboardButton('Добавить доходы')
    button_feedback = KeyboardButton('Связь с разработчиком')

    main_kb = ReplyKeyboardMarkup(resize_keyboard = True)
    main_kb.add(button_history)
    main_kb.add(button_consumption, button_income)
    main_kb.add(button_feedback)

    @dp.message_handler(commands = ['start'])
    async def start(message: types.Message):
       await message.answer("Добро пожаловать!\n"
                            "Данный бот создан для вашего учета расходов.\n"
                            "Вы можете добавлять свои сведения о "
                            "расходах и доходах.\n"
                            "Также вы можете запрашивать "
                            "статистику и историю операций.",
                            reply_markup = main_kb)

       # TODO: добавление пользователя в базу данных


    @dp.message_handler(text = 'Связь с разработчиком')
    async def process_start_command(message: types.Message):
        await message.answer('@Sad_prod')
except:
    print("Bug(((")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates =  'true')