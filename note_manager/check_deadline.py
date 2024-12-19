#Описание: Программа запрашивает дату дедлайна, сравнивает её с текущей датой и сообщает, истек ли срок или сколько дней осталось д

from datetime import datetime


def parse_date(date_str):
    """
    Парсит строку даты в объект datetime.
    :param date_str: строка даты в формате "день-месяц-год"
    :return: объект datetime
    :raise ValueError: если формат даты неверен
    """
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")
        return date
    except ValueError:
        raise ValueError("Неверный формат даты. Введите дату в формате день-месяц-год.")


def calculate_days_difference(current_date, deadline_date):
    """
    Рассчитывает разницу между двумя датами в днях.
    :param current_date: текущая дата
    :param deadline_date: дата дедлайна
    :return: количество дней до или после дедлайна
    """
    difference = deadline_date - current_date
    days_left = difference.days
    return days_left


def check_and_print_deadline(days_left):
    """
    Проверяет и выводит информацию о дедлайне.
    :param days_left: количество дней до или после дедлайна
    """
    if days_left < 0:
        print(f"Внимание! Дедлайн истёк {abs(days_left)} дня(-ей) назад.")
    elif days_left == 0:
        print("Сегодня последний день дедлайна!")
    else:
        print(f"Дедлайн через {days_left} дня(-ей).")


def main():
    # Текущая дата
    today = datetime.now().date()
    print(f"Текущая дата: {today.strftime('%d-%m-%Y')}")

    # Запрашиваем дату дедлайна
    while True:
        try:
            deadline_str = input("Введите дату дедлайна (в формате день-месяц-год): ")
            deadline = parse_date(deadline_str)
            break
        except ValueError as e:
            print(e)

    # Рассчитываем разницу в днях
    days_left = calculate_days_difference(today, deadline.date())

    # Выводим результат
    check_and_print_deadline(days_left)


if __name__ == "__main__":
    main()