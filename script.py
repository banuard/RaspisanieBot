import telebot
from telebot import types
import datetime

TOKEN = "8840438256:AAHSdgnprWKK9OdytRbIoA-9J5epAmqCRUU"  # <-- вставь токен от @BotFather
bot = telebot.TeleBot(TOKEN)

# Понедельник, который ТОЧНО был нечётной неделей.
# Посмотри в деканате/личном кабинете и поставь правильную дату!
REFERENCE_MONDAY = datetime.date(2026, 8, 31)  # сегодня, понедельник 1 (нечётной) недели

DAYS_RU = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

# ---------------------------------------------------------------------------
# РАСПИСАНИЕ
# Каждая пара — словарь: time, subject, type (может быть пустым), teacher (может быть пустым)
# ---------------------------------------------------------------------------
SCHEDULE = {
    # 1 неделя = нечётная (если у вас наоборот - поменяй местами ключи "нечётная"/"чётная")
    "нечётная": {
        "Понедельник": [
            {"time": "10:10 - 11:35", "subject": "Теория информационных процессов и систем", "type": "Л", "teacher": "Садовникова Н.П. (Г603)"},
            {"time": "11:50 - 13:15", "subject": "Теория информационных процессов и систем", "type": "ЛР", "teacher": "Садовникова Н.П. (Г603) Савина О.В. (Г602)"},
            {"time": "13:45 - 15:10", "subject": "Анализ требований к ИС", "type": "Л", "teacher": "Садовникова Н.П. (Г603)"},
        ],
        "Вторник": [
            {"time": "10:10 - 11:35", "subject": "Иностранный язык (английский)", "type": "ПЗ", "teacher": "Бганцева И.В. (А263) Кальнов Д.Д. (А258)"},
            {"time": "11:50 - 13:15", "subject": "Основы web технологий", "type": "Л", "teacher": "Гуртяков А.С. (Г603)"},
            {"time": "13:45 - 15:10", "subject": "Основы web технологий", "type": "ЛР", "teacher": "Гуртяков А.С. (Г603) Щербаков А.Г. (Г602)"},
        ],
        "Среда": [
            {"time": "10:10 - 11:35", "subject": "Элективные дисциплины по физической культуре и спорту", "type": "", "teacher": ""},
            {"time": "11:50 - 13:15", "subject": "Качество и надежность ИС", "type": "ЛР", "teacher": "Чикин А.Д. (Б206)"},
            {"time": "13:45 - 15:10", "subject": "Качество и надежность ИС", "type": "ЛР", "teacher": "Чикин А.Д. (Б206)"},
        ],
        "Четверг": [
            {"time": "8:30 - 9:55", "subject": "Анализ требований к ИС", "type": "ЛР", "teacher": "Садовникова Н.П. (Г603) Трудов Я.А. (Г602)"},
            {"time": "10:10 - 11:35", "subject": "Анализ требований к ИС", "type": "ЛР", "teacher": "Садовникова Н.П. (Г603) Трудов Я.А. (Г602)"},
            {"time": "11:50 - 13:15", "subject": "Основы анализа данных", "type": "Л", "teacher": "Игнатьев А.В. (Г603)"},
            {"time": "13:45 - 15:10", "subject": "Основы анализа данных", "type": "ПЗ", "teacher": "Игнатьев А.В. (Г603)"},
        ],
        "Пятница": [
            {"time": "10:10 - 11:35", "subject": "Элективные дисциплины по физической культуре и спорту", "type": "", "teacher": ""},
            {"time": "11:50 - 13:15", "subject": "Качество и надежность ИС", "type": "Л", "teacher": "Чикин А.Д. (В505)"},
            {"time": "13:45 - 15:10", "subject": "Информационные технологии (1 подгруппа)", "type": "ЛР", "teacher": "Савина О.В. (Г101)"},
            {"time": "15:25 - 16:50", "subject": "Информационные технологии (1 подгруппа)", "type": "ЛР", "teacher": "Савина О.В. (Г101)"},
        ],
        "Суббота": [],
        "Воскресенье": [],
    },
    "чётная": {
        "Понедельник": [
            {"time": "8:30 - 9:55", "subject": "Информационные технологии", "type": "Л", "teacher": "Савина О.В. (Г603)"},
            {"time": "10:10 - 11:35", "subject": "Теория информационных процессов и систем", "type": "ЛР", "teacher": "Садовникова Н.П. (Г603) Савина О.В. (Г602)"},
            {"time": "11:50 - 13:15", "subject": "Теория информационных процессов и систем", "type": "ЛР", "teacher": "Садовникова Н.П. (Г603) Савина О.В. (Г602)"},
            {"time": "13:45 - 15:10", "subject": "Анализ требований к ИС", "type": "Л", "teacher": "Садовникова Н.П. (Г603)"},
        ],
        "Вторник": [
            {"time": "10:10 - 11:35", "subject": "Иностранный язык (английский)", "type": "ПЗ", "teacher": "Бганцева И.В. (А263) Кальнов Д.Д. (А258)"},
            {"time": "11:50 - 13:15", "subject": "Основы web технологий", "type": "ЛР", "teacher": "Гуртяков А.С. (Г603) Щербаков А.Г. (Г602)"},
            {"time": "13:45 - 15:10", "subject": "Основы web технологий", "type": "ЛР", "teacher": "Гуртяков А.С. (Г603) Щербаков А.Г. (Г602)"},
        ],
        "Среда": [
            {"time": "10:10 - 11:35", "subject": "Элективные дисциплины по физической культуре и спорту", "type": "", "teacher": ""},
            {"time": "11:50 - 13:15", "subject": "Качество и надежность ИС", "type": "ЛР", "teacher": "Чикин А.Д. (Б206)"},
            {"time": "13:45 - 15:10", "subject": "Качество и надежность ИС", "type": "ЛР", "teacher": "Чикин А.Д. (Б206)"},
        ],
        "Четверг": [
            {"time": "11:50 - 13:15", "subject": "Основы анализа данных", "type": "ПЗ", "teacher": "Игнатьев А.В. (Г603)"},
            {"time": "13:45 - 15:10", "subject": "Основы анализа данных", "type": "ПЗ", "teacher": "Игнатьев А.В. (Г603)"},
        ],
        "Пятница": [
            {"time": "10:10 - 11:35", "subject": "Элективные дисциплины по физической культуре и спорту", "type": "", "teacher": ""},
            {"time": "11:50 - 13:15", "subject": "Качество и надежность ИС", "type": "Л", "teacher": "Чикин А.Д. (В505)"},
            {"time": "13:45 - 15:10", "subject": "Информационные технологии (2 подгруппа)", "type": "ЛР", "teacher": "Савина О.В. (Г101)"},
            {"time": "15:25 - 16:50", "subject": "Информационные технологии (2 подгруппа)", "type": "ЛР", "teacher": "Савина О.В. (Г101)"},
        ],
        "Суббота": [],
        "Воскресенье": [],
    },
}


def get_week_parity(date: datetime.date) -> str:
    """Определяет нечётная или чётная неделя для данной даты."""
    days_since_ref = (date - REFERENCE_MONDAY).days
    weeks_since_ref = days_since_ref // 7
    return "нечётная" if weeks_since_ref % 2 == 0 else "чётная"


def get_monday(date: datetime.date) -> datetime.date:
    """Возвращает понедельник той недели, в которую входит date."""
    return date - datetime.timedelta(days=date.weekday())


def _format_lessons_block(lessons: list) -> list:
    """Формирует список строк для пар одного дня (без заголовка дня)."""
    lines = []
    if not lessons:
        lines.append("")
        lines.append("Занятий нет 🎉")
        return lines

    lines.append("")
    for i, lesson in enumerate(lessons):
        lines.append(f"⏱️{lesson['time']}")
        lines.append(lesson["subject"])
        if lesson.get("type"):
            lines.append(lesson["type"])
        if lesson.get("teacher"):
            lines.append(lesson["teacher"])
        if i < len(lessons) - 1:
            lines.append("- - - - -")
    return lines


def format_day(date: datetime.date) -> str:
    """Форматирует расписание одного дня по шаблону."""
    parity = get_week_parity(date)
    day_name = DAYS_RU[date.weekday()]
    lessons = SCHEDULE.get(parity, {}).get(day_name, [])

    lines = [f"❗️{parity.capitalize()} неделя", f"📅{day_name}"]
    lines.extend(_format_lessons_block(lessons))
    return "\n".join(lines)


def format_week(monday_date: datetime.date) -> str:
    """Форматирует расписание на всю неделю (Пн-Пт)."""
    parity = get_week_parity(monday_date)
    blocks = [f"❗️{parity.capitalize()} неделя"]

    for i in range(5):  # Пн-Пт
        day_date = monday_date + datetime.timedelta(days=i)
        day_name = DAYS_RU[day_date.weekday()]
        lessons = SCHEDULE.get(parity, {}).get(day_name, [])

        day_block = [f"📅{day_name}"]
        day_block.extend(_format_lessons_block(lessons))
        blocks.append("\n".join(day_block))

    return "\n\n".join(blocks)


def main_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        types.KeyboardButton("Сегодня"),
        types.KeyboardButton("Завтра"),
        types.KeyboardButton("Текущая неделя"),
        types.KeyboardButton("Следующая неделя"),
    )
    return kb


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот расписания 👋\nВыбери, что показать:",
        reply_markup=main_keyboard(),
    )


@bot.message_handler(func=lambda m: m.text == "Сегодня")
def today(message):
    text = format_day(datetime.date.today())
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())


@bot.message_handler(func=lambda m: m.text == "Завтра")
def tomorrow(message):
    tmr = datetime.date.today() + datetime.timedelta(days=1)
    text = format_day(tmr)
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())


@bot.message_handler(func=lambda m: m.text == "Текущая неделя")
def current_week(message):
    monday = get_monday(datetime.date.today())
    text = format_week(monday)
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())


@bot.message_handler(func=lambda m: m.text == "Следующая неделя")
def next_week(message):
    monday = get_monday(datetime.date.today()) + datetime.timedelta(days=7)
    text = format_week(monday)
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())


if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()