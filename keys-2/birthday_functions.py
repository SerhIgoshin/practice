from datetime import datetime

def get_weekday(day, month, year):
    try:
        date = datetime(year, month, day)
        weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        return weekdays[date.weekday()]
    except ValueError:
        return "Некорректная дата"

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(day, month, year):
    today = datetime.today()
    birth_date = datetime(year, month, day)
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

def render_digit_as_stars(digit):
    patterns = {
        '0': ["*****", "*   *", "*   *", "*   *", "*****"],
        '1': ["    *", "    *", "    *", "    *", "    *"],
        '2': ["*****", "    *", "*****", "*    ", "*****"],
        '3': ["*****", "    *", "*****", "    *", "*****"],
        '4': ["*   *", "*   *", "*****", "    *", "    *"],
        '5': ["*****", "*    ", "*****", "    *", "*****"],
        '6': ["*****", "*    ", "*****", "*   *", "*****"],
        '7': ["*****", "    *", "    *", "    *", "    *"],
        '8': ["*****", "*   *", "*****", "*   *", "*****"],
        '9': ["*****", "*   *", "*****", "    *", "*****"],
    }
    return patterns.get(digit, ["     "]*5)

def format_date_with_stars(day, month, year):
    formatted = f"{day:02d} {month:02d} {year}"
    lines = [""] * 5  # Для хранения 5 строк звёздочного представления

    for char in formatted:
        if char.isdigit():
            digit_lines = render_digit_as_stars(char)
            for i in range(5):
                lines[i] += digit_lines[i] + "  "  # Добавляем две пробельные строки между цифрами
        elif char == ' ':
            for i in range(5):
                lines[i] += "     "  # Пробел между частями даты

    return "\n".join(lines)

def main():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))

    if year < 100:
        year += 2000

    weekday = get_weekday(day, month, year)

    print("\n" + "*" * 30)
    if weekday == "Некорректная дата":
        print("Ошибка: введена некорректная дата.")
    else:
        print(f"День недели: {weekday}")

    if is_leap_year(year):
        print(f"{year} — это високосный год!")
    else:
        print(f"{year} — это не високосный год.")

    age = calculate_age(day, month, year)
    print(f"Текущий возраст: {age} лет.")
    
    print("\nДата рождения в графическом формате:")
    print(format_date_with_stars(day, month, year))

    print("*" * 30)

if __name__ == "__main__":
    main()

