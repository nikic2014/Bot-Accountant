from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import const

try:
    # создание главного меню
    main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button_history = KeyboardButton('История')
    button_consumption = KeyboardButton('Добавить расходы')
    button_income = KeyboardButton('Добавить доходы')
    button_feedback = KeyboardButton('Связь с разработчиком')
    main_kb.add(button_history)
    main_kb.add(button_consumption, button_income)
    main_kb.add(button_feedback)

    # ссоздание Reply меню для history
    history_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    history_income = KeyboardButton('История доходов')
    history_consumption = KeyboardButton('История расходов')
    button_back = KeyboardButton('Назад')
    history_kb.add(history_income)
    history_kb.add(history_consumption)
    history_kb.add(button_back)

    # создание inline меню для history
    time_kb = InlineKeyboardMarkup(row_width=1)
    day_button = InlineKeyboardButton(const.day, callback_data='День')
    week_button = InlineKeyboardButton(const.week, callback_data='Неделя')
    month_button = InlineKeyboardButton(const.month, callback_data='Месяц')
    year_button = InlineKeyboardButton(const.year, callback_data='Год')
    time_kb.add(day_button)
    time_kb.add(week_button)
    time_kb.add(month_button)
    time_kb.add(year_button)

    # создание Reply меню для income / expenses
    in_ex_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    insert_today = KeyboardButton('Добавить на сегодня')
    insert_to_date = KeyboardButton('Выбрать дату')
    button_back = KeyboardButton('Назад')
    in_ex_kb.add(insert_today)
    in_ex_kb.add(insert_to_date)
    in_ex_kb.add(button_back)

    # создание inlinee меню для выбора даты
except:
    print('Exept in GUI')
