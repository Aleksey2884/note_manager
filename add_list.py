# Функция для получения данных от пользователя
def get_user_input():
    # Получаем заголовки заметки
    title_1 = input("Введите первый заголовок заметки: ")
    title_2 = input("Введите второй заголовок заметки: ")
    title_3 = input("Введите третий заголовок заметки: ")

# Получаем содержание заметки
    content = input("Введите содержание заметки: ")

# Получаем дату создания заметки
    date_created = input("Введите дату создания заметки (в формате ДД-ММ-ГГГГ): ")

# Проверяем формат введенной даты
    try:
        day, month, year = map(int, date_created.split('-'))
        if not (1 <= day <= 31):
            raise ValueError("День должен быть числом от 1 до 31")
        if not (1 <= month <= 12):
            raise ValueError("Месяц должен быть числом от 1 до 12")
        if len(str(year)) != 4 or year < 1000:
            raise ValueError("Год должен быть четырехзначным числом больше 999")
# Если дата корректная, преобразуем её в объект datetime
        from datetime import datetime
        date_created = datetime(year, month, day)
    except ValueError as e:
        print(f"Ошибка при вводе даты: {e}")
        return None

# Создаем список заголовков
    titles = [title_1, title_2, title_3]

# Возвращаем все полученные данные
    return {
        'titles': titles,
        'content': content,
        'date_created': date_created
    }


# Основная функция программы
def main():
    user_data = get_user_input()

    if user_data is not None:
        print("\nВаша заметка:")
        for i, title in enumerate(user_data['titles'], start=1):
            print(f"{i}. Заголовок: {title}")
        print(f"Содержание: {user_data['content']}")
        print(f"Дата создания: {user_data['date_created'].strftime('%d-%m-%Y')}")
    else:
        print("Произошла ошибка при вводе данных.")


if __name__ == "__main__":
    main()