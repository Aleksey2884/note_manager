# Ввод данных для заметки
def get_input():
    # Получаем заголовок заметки
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")

    # Запрашиваем дату в формате 'ДД-ММ-ГГГГ'
    date_str = input("Укажите дату заметки в формате ДД-ММ-ГГГГ: ")

    try:
        # Преобразуем строку в объект datetime
        from datetime import datetime
        date = datetime.strptime(date_str, '%d-%m-%Y')

        return {
            'title': title,
            'content': content,
            'date': date
        }
    except ValueError as e:
        print(f'Ошибка при вводе даты: {e}')
        return None

note_data = get_input()
if note_data is not None:
    print(f"Заголовок: {note_data['title']}")
    print(f"Содержание: {note_data['content']}")
    print(f"Дата: {note_data['date'].strftime('%d-%m-%Y')}")