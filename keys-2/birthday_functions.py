"""
Кейс-задача №2: Стилистическое преобразование чисел
Задание:
Реализовать программу, которая включает следующие функции:

Запрос дня, месяца и года рождения пользователя.
Определение дня недели для этой даты.
Проверка, является ли год високосным.
Подсчет текущего возраста пользователя.
Вывод даты рождения в формате дд мм гггг, где цифры прорисованы звездочками.
Решение:

Код программы (Python):
"""

from datetime import datetime

def get_weekday(day, month, year):
    try:
        # Создаём объект даты с введёнными значениями
        date = datetime(year, month, day)
        
        # Список дней недели на русском языке
        weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        
        # Возвращаем день недели на русском языке
        return weekdays[date.weekday()]
    except ValueError:
        return "Некорректная дата"  # Если дата некорректная

def is_leap_year(year):
    # Проверка на високосный год
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def calculate_age(day, month, year):
    today = datetime.today()
    birth_date = datetime(year, month, day)
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

def format_date_with_stars(day, month, year):
    # Форматируем дату в нужный вид, заменяя цифры на звёздочки
    formatted_day = f"{day:02d}"
    formatted_month = f"{month:02d}"
    formatted_year = f"{year}"
    
    # Преобразуем каждый символ в строку с заменой цифр на звёздочки
    formatted_day = ''.join('*' if char.isdigit() else char for char in formatted_day)
    formatted_month = ''.join('*' if char.isdigit() else char for char in formatted_month)
    formatted_year = ''.join('*' if char.isdigit() else char for char in formatted_year)

    return f"{formatted_day} {formatted_month} {formatted_year}"

def main():
    # Ввод данных
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))

    # Проверка года на 2 цифры и преобразование в 4 цифры
    if year < 100:
        year += 2000  # Добавляем 2000, чтобы получить правильный четырёхзначный год

    # Получаем день недели
    weekday = get_weekday(day, month, year)
    
    # Выводим результаты с оформлениями (звездочками)
    print("\n" + "*" * 30)  # Оформление с 30 звёздочками
    
    if weekday == "Некорректная дата":
        print("Ошибка: введена некорректная дата.")
    else:
        print(f"День недели: {weekday}")
    
    # Проверка на високосный год
    if is_leap_year(year):
        print(f"{year} — это високосный год!")
    else:
        print(f"{year} — это не високосный год.")

    # Подсчёт возраста
    age = calculate_age(day, month, year)
    print(f"Текущий возраст: {age} лет.")
    
    # Вывод даты рождения в формате с звёздочками
    formatted_date = format_date_with_stars(day, month, year)
    print(f"Дата рождения в формате с звёздочками: {formatted_date}")
    
    print("*" * 30)  # Оформление с 30 звёздочками

if __name__ == "__main__":
    main()
