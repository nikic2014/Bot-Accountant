from aiogram import Bot, Dispatcher, executor, types
from aiogram_calendar import simple_cal_callback, SimpleCalendar, \
    dialog_cal_callback, DialogCalendar
from aiogram.dispatcher.filters import Text
import psycopg2
import const
import GUI
from config import host, user, password, db_name

bot = Bot(token=const.TOKEN_BOT, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

conaction = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
try:
    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        user_id = message.from_user.id
        chat_id = message.chat.id

        try:
            with conaction.cursor() as cursor:
                cursor.execute(
                    f"INSERT INTO Users (user_id, chat_id) VALUES {user_id, chat_id};"
                )
                conaction.commit()
                cursor.execute(
                    "select * from users"
                )
                print("Пользователь добавлен в базу данных: ",
                      cursor.fetchall())

        except psycopg2.errors.UniqueViolation:
            await message.answer("<em>Добро пожаловать!\n"
                                 "Мы рады, что вы к нам вернулись!!!\n"
                                 "Вы можете добавлять свои сведения о "
                                 "расходах и доходах.\n"
                                 "Также вы можете запрашивать "
                                 "статистику и историю операций.</em>",
                                 reply_markup=GUI.main_kb,
                                 parse_mode="HTML")
        else:
            await message.answer("<em>Добро пожаловать!\n"
                                 "Данный бот создан для вашего учета расходов.\n"
                                 "Вы можете добавлять свои сведения о "
                                 "расходах и доходах.\n"
                                 "Также вы можете запрашивать "
                                 "статистику и историю операций.</em>",
                                 reply_markup=GUI.main_kb,
                                 parse_mode="HTML")


    @dp.message_handler(commands=['stop-conaction'])
    async def start(message: types.Message):
        conaction.close()
        print("Соединение закрыто")


    @dp.message_handler(text='История')
    async def History(message: types.Message):
        await message.answer("Выберите категорию",
                             reply_markup=GUI.history_kb)


    @dp.message_handler(text='История доходов')
    async def History_Income(message: types.Message):
        await message.answer("Выберите категорию",
                             reply_markup=GUI.time_kb)


    @dp.message_handler(text='История расходов')
    async def History_Expenses(message: types.Message):
        await message.answer('Выберите категорию',
                             reply_markup=GUI.time_kb)


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
    async def history_day(call: types.CallbackQuery):
        await call.message.answer("rabit day")


    @dp.callback_query_handler(text=const.week)
    async def history_week(call: types.CallbackQuery):
        await call.message.answer("rabit week")


    @dp.callback_query_handler(text=const.month)
    async def history_month(call: types.CallbackQuery):
        await call.message.answer("rabit month")


    @dp.callback_query_handler(text=const.year)
    async def history_year(call: types.CallbackQuery):
        await call.message.answer("rabit year")


    @dp.message_handler(text='Назад')
    async def back_in_main(message: types.Message):
        await message.answer("Вы в главном меню", reply_markup=GUI.main_kb)


    @dp.message_handler(text='Связь с разработчиком')
    async def contact_developer(message: types.Message):
        await message.answer('@Sad_prod')


except Exception as ex_:
    print("Error while working with PostgreSQL:", ex_)
except:
    print('Exept in main.py')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates='true')
