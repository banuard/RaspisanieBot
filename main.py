import flet as ft
import datetime


# ========== АВТОМАТИЧЕСКОЕ ОПРЕДЕЛЕНИЕ УЧЕБНОГО ГОДА ==========
def get_reference_monday():
    """Возвращает первый понедельник сентября текущего года"""
    today = datetime.date.today()
    year = today.year

    # Если сейчас 2026 год - используем 31 августа
    if year == 2026:
        return datetime.date(2026, 8, 31)

    # Для остальных годов - первый понедельник сентября
    # Ищем 1 сентября
    sept_1 = datetime.date(year, 9, 1)
    # Находим ближайший понедельник (включая 1 сентября)
    days_until_monday = (7 - sept_1.weekday()) % 7
    return sept_1 + datetime.timedelta(days=days_until_monday)


REFERENCE_MONDAY = get_reference_monday()
DAYS_RU = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

# ========== РАСПИСАНИЕ ==========
SCHEDULE = {
    "нечётная": {
        "Понедельник": [
            {"time": "10:10 - 11:35", "subject": "Теория информационных процессов и систем", "type": "Л",
             "teacher": "Садовникова Н.П. (Г603)"},
            {"time": "11:50 - 13:15", "subject": "Теория информационных процессов и систем", "type": "ЛР",
             "teacher": "Садовникова Н.П. (Г603) Савина О.В. (Г602)"},
            {"time": "13:45 - 15:10", "subject": "Анализ требований к ИС", "type": "Л",
             "teacher": "Садовникова Н.П. (Г603)"},
        ],
        "Вторник": [
            {"time": "10:10 - 11:35", "subject": "Иностранный язык (английский)", "type": "ПЗ",
             "teacher": "Бганцева И.В. (А263) Кальнов Д.Д. (А258)"},
            {"time": "11:50 - 13:15", "subject": "Основы web технологий", "type": "Л",
             "teacher": "Гуртяков А.С. (Г603)"},
            {"time": "13:45 - 15:10", "subject": "Основы web технологий", "type": "ЛР",
             "teacher": "Гуртяков А.С. (Г603) Щербаков А.Г. (Г602)"},
        ],
        "Среда": [
            {"time": "10:10 - 11:35", "subject": "Элективные дисциплины по физической культуре и спорту", "type": "",
             "teacher": ""},
            {"time": "11:50 - 13:15", "subject": "Качество и надежность ИС", "type": "ЛР",
             "teacher": "Чикин А.Д. (Б206)"},
            {"time": "13:45 - 15:10", "subject": "Качество и надежность ИС", "type": "ЛР",
             "teacher": "Чикин А.Д. (Б206)"},
        ],
        "Четверг": [
            {"time": "8:30 - 9:55", "subject": "Анализ требований к ИС", "type": "ЛР",
             "teacher": "Садовникова Н.П. (Г603) Трудов Я.А. (Г602)"},
            {"time": "10:10 - 11:35", "subject": "Анализ требований к ИС", "type": "ЛР",
             "teacher": "Садовникова Н.П. (Г603) Трудов Я.А. (Г602)"},
            {"time": "11:50 - 13:15", "subject": "Основы анализа данных", "type": "Л",
             "teacher": "Игнатьев А.В. (Г603)"},
            {"time": "13:45 - 15:10", "subject": "Основы анализа данных", "type": "ПЗ",
             "teacher": "Игнатьев А.В. (Г603)"},
        ],
        "Пятница": [
            {"time": "10:10 - 11:35", "subject": "Элективные дисциплины по физической культуре и спорту", "type": "",
             "teacher": ""},
            {"time": "11:50 - 13:15", "subject": "Качество и надежность ИС", "type": "Л",
             "teacher": "Чикин А.Д. (В505)"},
            {"time": "13:45 - 15:10", "subject": "Информационные технологии (1 подгруппа)", "type": "ЛР",
             "teacher": "Савина О.В. (Г101)"},
            {"time": "15:25 - 16:50", "subject": "Информационные технологии (1 подгруппа)", "type": "ЛР",
             "teacher": "Савина О.В. (Г101)"},
        ],
        "Суббота": [],
        "Воскресенье": [],
    },
    "чётная": {
        "Понедельник": [
            {"time": "8:30 - 9:55", "subject": "Информационные технологии", "type": "Л",
             "teacher": "Савина О.В. (Г603)"},
            {"time": "10:10 - 11:35", "subject": "Теория информационных процессов и систем", "type": "ЛР",
             "teacher": "Садовникова Н.П. (Г603) Савина О.В. (Г602)"},
            {"time": "11:50 - 13:15", "subject": "Теория информационных процессов и систем", "type": "ЛР",
             "teacher": "Садовникова Н.П. (Г603) Савина О.В. (Г602)"},
            {"time": "13:45 - 15:10", "subject": "Анализ требований к ИС", "type": "Л",
             "teacher": "Садовникова Н.П. (Г603)"},
        ],
        "Вторник": [
            {"time": "10:10 - 11:35", "subject": "Иностранный язык (английский)", "type": "ПЗ",
             "teacher": "Бганцева И.В. (А263) Кальнов Д.Д. (А258)"},
            {"time": "11:50 - 13:15", "subject": "Основы web технологий", "type": "ЛР",
             "teacher": "Гуртяков А.С. (Г603) Щербаков А.Г. (Г602)"},
            {"time": "13:45 - 15:10", "subject": "Основы web технологий", "type": "ЛР",
             "teacher": "Гуртяков А.С. (Г603) Щербаков А.Г. (Г602)"},
        ],
        "Среда": [
            {"time": "10:10 - 11:35", "subject": "Элективные дисциплины по физической культуре и спорту", "type": "",
             "teacher": ""},
            {"time": "11:50 - 13:15", "subject": "Качество и надежность ИС", "type": "ЛР",
             "teacher": "Чикин А.Д. (Б206)"},
            {"time": "13:45 - 15:10", "subject": "Качество и надежность ИС", "type": "ЛР",
             "teacher": "Чикин А.Д. (Б206)"},
        ],
        "Четверг": [
            {"time": "11:50 - 13:15", "subject": "Основы анализа данных", "type": "ПЗ",
             "teacher": "Игнатьев А.В. (Г603)"},
            {"time": "13:45 - 15:10", "subject": "Основы анализа данных", "type": "ПЗ",
             "teacher": "Игнатьев А.В. (Г603)"},
        ],
        "Пятница": [
            {"time": "10:10 - 11:35", "subject": "Элективные дисциплины по физической культуре и спорту", "type": "",
             "teacher": ""},
            {"time": "11:50 - 13:15", "subject": "Качество и надежность ИС", "type": "Л",
             "teacher": "Чикин А.Д. (В505)"},
            {"time": "13:45 - 15:10", "subject": "Информационные технологии (2 подгруппа)", "type": "ЛР",
             "teacher": "Савина О.В. (Г101)"},
            {"time": "15:25 - 16:50", "subject": "Информационные технологии (2 подгруппа)", "type": "ЛР",
             "teacher": "Савина О.В. (Г101)"},
        ],
        "Суббота": [],
        "Воскресенье": [],
    },
}


# ========== ФУНКЦИИ ==========
def get_week_parity(date):
    days_since_ref = (date - REFERENCE_MONDAY).days
    weeks_since_ref = days_since_ref // 7
    return "нечётная" if weeks_since_ref % 2 == 0 else "чётная"


def get_monday(date):
    return date - datetime.timedelta(days=date.weekday())


def format_day(date):
    parity = get_week_parity(date)
    day_name = DAYS_RU[date.weekday()]
    lessons = SCHEDULE.get(parity, {}).get(day_name, [])

    result = f"❗️{parity.capitalize()} неделя\n📅{day_name}\n\n"
    if not lessons:
        result += "Занятий нет 🎉"
        return result

    for i, lesson in enumerate(lessons):
        result += f"⏱️{lesson['time']}\n"
        result += f"{lesson['subject']}\n"
        if lesson.get('type'):
            result += f"{lesson['type']}\n"
        if lesson.get('teacher'):
            result += f"{lesson['teacher']}\n"
        if i < len(lessons) - 1:
            result += "- - - - -\n"
    return result


def format_week(monday_date):
    parity = get_week_parity(monday_date)
    result = f"❗️{parity.capitalize()} неделя\n\n"

    for i in range(5):
        day_date = monday_date + datetime.timedelta(days=i)
        day_name = DAYS_RU[day_date.weekday()]
        lessons = SCHEDULE.get(parity, {}).get(day_name, [])

        result += f"📅{day_name}\n"
        if not lessons:
            result += "Занятий нет 🎉\n"
        else:
            for j, lesson in enumerate(lessons):
                result += f"  ⏱️{lesson['time']}\n"
                result += f"  {lesson['subject']}\n"
                if lesson.get('type'):
                    result += f"  {lesson['type']}\n"
                if lesson.get('teacher'):
                    result += f"  {lesson['teacher']}\n"
                if j < len(lessons) - 1:
                    result += "  - - - - -\n"
        result += "\n"
    return result


# ========== ИНТЕРФЕЙС ПРИЛОЖЕНИЯ (Flet) ==========
def main(page: ft.Page):
    page.title = "📚 Расписание"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.padding = 20
    page.bgcolor = ft.Colors.GREY_50

    # Заголовок
    title = ft.Text("📚 Расписание", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800)

    # Поле для вывода результата
    result_text = ft.Text(
        "Выберите день или неделю 👆",
        size=16,
        color=ft.Colors.BLACK87,
        selectable=True,
    )

    result_container = ft.Container(
        content=result_text,
        padding=15,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.GREY_300),
    )

    # Обработчики кнопок
    def show_today(e):
        result_text.value = format_day(datetime.date.today())
        page.update()

    def show_tomorrow(e):
        tmr = datetime.date.today() + datetime.timedelta(days=1)
        result_text.value = format_day(tmr)
        page.update()

    def show_week(e):
        monday = get_monday(datetime.date.today())
        result_text.value = format_week(monday)
        page.update()

    def show_next_week(e):
        monday = get_monday(datetime.date.today()) + datetime.timedelta(days=7)
        result_text.value = format_week(monday)
        page.update()

    # Кнопки
    btn_today = ft.ElevatedButton(
        "📅 Сегодня",
        on_click=show_today,
        bgcolor=ft.Colors.BLUE_50,
        color=ft.Colors.BLUE_800,
        width=200,
    )

    btn_tomorrow = ft.ElevatedButton(
        "📅 Завтра",
        on_click=show_tomorrow,
        bgcolor=ft.Colors.BLUE_50,
        color=ft.Colors.BLUE_800,
        width=200,
    )

    btn_week = ft.ElevatedButton(
        "📅 Текущая неделя",
        on_click=show_week,
        bgcolor=ft.Colors.GREEN_50,
        color=ft.Colors.GREEN_800,
        width=200,
    )

    btn_next_week = ft.ElevatedButton(
        "📅 Следующая неделя",
        on_click=show_next_week,
        bgcolor=ft.Colors.GREEN_50,
        color=ft.Colors.GREEN_800,
        width=200,
    )

    # Группируем кнопки в ряд
    buttons_row1 = ft.Row(
        [btn_today, btn_tomorrow],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    buttons_row2 = ft.Row(
        [btn_week, btn_next_week],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Добавляем всё на страницу
    page.add(
        title,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        buttons_row1,
        buttons_row2,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        result_container,
    )


ft.app(target=main)