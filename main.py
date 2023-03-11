from aiogram import Bot, Dispatcher, executor, types
from aiogram_calendar import simple_cal_callback, SimpleCalendar, \
    dialog_cal_callback, DialogCalendar
from aiogram.dispatcher.filters import Text
import const
import GUI

bot = Bot(token=const.TOKEN_BOT, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

try:
    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await message.answer("Добро пожаловать!\n"
                             "Данный бот создан для вашего учета расходов.\n"
                             "Вы можете добавлять свои сведения о "
                             "расходах и доходах.\n"
                             "Также вы можете запрашивать "
                             "статистику и историю операций.",
                             reply_markup=GUI.main_kb)

        # TODO: добавление пользователя в базу данных


    @dp.message_handler(text='История')
    async def History(message: types.Message):
        await message.answer("Выберите категорию", reply_markup=GUI.history_kb)


    @dp.message_handler(text='История доходов')
    async def History_Income(message: types.Message):
        await message.answer("Выберите категорию", reply_markup=GUI.time_kb)


    @dp.message_handler(text='История расходов')
    async def History_Expenses(message: types.Message):
        await message.answer('Выберите категорию', reply_markup=GUI.time_kb)


    @dp.message_handler(text='Добавить доходы')
    async def add_Income(message: types.Message):
        await message.answer("Выберете временной промежуток",
                             reply_markup=GUI.in_ex_kb)


    @dp.message_handler(text='Добавить расходы')
    async def add_Expenses(message: types.Message):
        await message.answer("Выберете верменной промежуток",
                             reply_markup=GUI.in_ex_kb)


    # Функции работы с календарем
    @dp.message_handler(text='Выбрать дату')
    async def add_Expenses(message: types.Message):
        await message.answer("Укажите нужную дату: ",
                             reply_markup=
                             await SimpleCalendar().start_calendar())


    @dp.callback_query_handler(simple_cal_callback.filter())
    async def process_simple_calendar(callback_query: types.CallbackQuery,
                                      callback_data: dict):
        selected, date = await SimpleCalendar().process_selection(
            callback_query, callback_data)
        if selected:
            await callback_query.message.answer(
                f'You selected {date.strftime("%d/%m/%Y")}',
                reply_markup=GUI.in_ex_kb)


    @dp.callback_query_handler(text=const.day)
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer("rabit day")


    @dp.callback_query_handler(text=const.week)
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer("rabit week")


    @dp.callback_query_handler(text=const.month)
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer("rabit week")


    @dp.callback_query_handler(text=const.year)
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer("rabit year")


    @dp.message_handler(text='Назад')
    async def process_start_command(message: types.Message):
        await message.answer("Вы в главном меню", reply_markup=GUI.main_kb)


    @dp.message_handler(text='Связь с разработчиком')
    async def process_start_command(message: types.Message):
        await message.answer('@Sad_prod')
except:
    print('Exept in main.py')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates='true')
