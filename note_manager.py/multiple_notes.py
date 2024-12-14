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

    print("\nСписок заметок:")
    for index, note in enumerate(notes_list, start=1):
        print(f"{index}.")
        for key, value in note.items():
            print(f"\t{key.capitalize()}: {value}")
        print()


# Основной блок программы
if __name__ == "__main__":
    notes = []
    while True:
        print("\nДобро пожаловать в \"Менеджер заметок\"! Вы можете добавить новую заметку.")

        new_note = create_note()
        notes.append(new_note)

        choice = input("\nХотите добавить ещё одну заметку? (да/нет): ").lower().strip()
        if choice != 'да':
            break

# Отображение всех заметок
    display_notes(notes)