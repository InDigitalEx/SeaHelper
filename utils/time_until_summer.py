from datetime import datetime

import pytz


def literal_format(value, form1, form2, form3) -> str:
    return f"{value} {form1 if value == 1 else form2 if value < 5 else form3}"


def format_time(delta):
    months = delta.days // 30
    days = delta.days % 30

    parts_full = []
    if months > 0:
        parts_full.append(literal_format(months, 'месяц', 'месяца', 'месяцев'))
    if days > 0:
        parts_full.append(literal_format(days, 'день', 'дня', 'дней'))

    parts_days = []
    if delta.days > 0:
        parts_days.append(literal_format(delta.days, 'дней', 'день', 'дня'))

    return f"<b>До начала лета осталось:</b> \n\n{' '.join(parts_full)} или {' '.join(parts_days)}"


def time_until_summer(timezone):
    # Получаем текущее время по заданной временной зоне
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)

    # Определяем дату начала следующего лета (1 июня следующего года)
    summer_start = datetime(now.year + (1 if now.month > 6 else 0), 6, 1, tzinfo=tz)

    # Если текущее время уже после 1 июня, сообщаем "Уже лето"
    if now.month >= 6 and now.month < 9:
        return "Уже лето"

    # Вычисляем оставшееся время до начала лета
    time_remaining = summer_start - now
    return format_time(time_remaining)
