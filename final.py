from datetime import datetime

def get_user_input():
# Инициализация пустого словаря для хранения данных заметки
    note = {}

# Получение имени автора
    note['author'] = input("Введите ваше имя: ")

# Получение содержания заметки
    note['content'] = input("Введите содержание заметки: ")

# Получение статуса заметки
    status_options = ["завершена", "незавершена"]
    while True:
        status = input(f"Выберите статус заметки ({', '.join(status_options)}): ").lower()
        if status in status_options:
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
    note['status'] = status

# Получение даты создания заметки
    while True:
        try:
            creation_date = input("Введите дату создания заметки (ДД-ММ-ГГГГ): ")
            day, month, year = map(int, creation_date.split('-'))
            note['creation_date'] = datetime(year, month, day).date()
            break
        except ValueError:
            print("Некорректный формат даты. Повторите попытку.")

# Получение даты последнего обновления заметки
    while True:
        try:
            last_update_date = input("Введите дату последнего обновления заметки (ДД-ММ-ГГГГ): ")
            day, month, year = map(int, last_update_date.split('-'))
            note['last_update_date'] = datetime(year, month, day).date()
            break
        except ValueError:
            print("Некорректный формат даты. Повторите попытку.")

# Получение заголовков заметки
    note['headers'] = []
    num_headers = int(input("Сколько заголовков у вашей заметки? "))
    for i in range(num_headers):
        header = input(f"Введите заголовок #{i + 1}: ")
        note['headers'].append(header)

    return note

def display_note(note):
    print("\nИнформация о заметке:")
    print(f"Автор: {note['author']}")
    print(f"Содержание: {note['content']}")
    print(f"Статус: {note['status']}")
    print(f"Дата создания: {note['creation_date'].strftime('%d-%m-%Y')}")
    print(f"Последнее обновление: {note['last_update_date'].strftime('%d-%m-%Y')}")
    print("Заголовки:")
    for i, header in enumerate(note['headers'], start=1):
        print(f"\t{i}. {header}")

def main():
    note = get_user_input()
    display_note(note)

if __name__ == "__main__":
    main()