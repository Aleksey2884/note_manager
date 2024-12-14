def create_note():
    """Функция для создания новой заметки"""

    # Ввод данных пользователем
    name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    creation_date = input("Введите дату создания (день-месяц-год): ")
    deadline = input("Введите дедлайн (день-месяц-год): ")

    # Создание словаря-заметки
    note = {
        'name': name,
        'title': title,
        'description': description,
        'status': status,
        'creation_date': creation_date,
        'deadline': deadline
    }

    return note


def display_notes(notes_list):
    """Функция для отображения всех заметок"""

    if not notes_list:
        print("\nНет заметок для отображения.")
        return

    print("\nТекущие заметки:")
    for index, note in enumerate(notes_list, start=1):
        print(f"{index}.")
        for key, value in note.items():
            print(f"\t{key.capitalize()}: {value}")
        print()


def remove_note(notes_list, criterion):
    """Функция для удаления заметки по имени пользователя или заголовку"""

    found = False
    updated_notes = []

    for note in notes_list:
        if note['name'] == criterion or note['title'] == criterion:
            found = True
        else:
            updated_notes.append(note)

    if found:
        print(f"Удалены заметки с именем пользователя '{criterion}' или заголовком '{criterion}'.")
    else:
        print(f"Заметок с именем пользователя '{criterion}' или заголовком '{criterion}' не найдено.")

    return updated_notes


# Основной блок программы
if __name__ == "__main__":
    notes = []

# Добавляем несколько заметок для примера
    notes.append(create_note())
    notes.append(create_note())

# Отображаем текущие заметки
    display_notes(notes)

# Удаляем заметку
    criterion = input("\nВведите имя пользователя или заголовок для удаления заметки: ")
    notes = remove_note(notes, criterion)

# Отображаем оставшиеся заметки
    display_notes(notes)