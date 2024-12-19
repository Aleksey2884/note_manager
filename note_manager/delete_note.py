def find_note_by_username_or_title(notes, query):
    """
    Находит заметку по имени пользователя или заголовку.
    Возвращает список найденных заметок.
    """
    found_notes = []

    for note in notes:
        if query.lower() in note["username"].lower() or query.lower() in note["title"].lower():
            found_notes.append(note)

    return found_notes


def delete_note(notes, query):
    """
    Удаляет заметку из списка.
    Сообщает, если заметка была успешно удалена.
    """
    found_notes = find_note_by_username_or_title(notes, query)

    if found_notes:
        for note in found_notes:
            notes.remove(note)
        print(f"Успешно удалено. Остались следующие заметки:\n")
        display_notes(notes)
    else:
        print("Заметка не найдена.")


def display_notes(notes):
    """
    Отображает список текущих заметок.
    """
    if notes:
        print("\nТекущие заметки:")
        for index, note in enumerate(notes, start=1):
            print(f"{index}. Имя: {note['username']}")
            print(f"   Заголовок: {note['title']}")
            print(f"   Описание: {note['description']}")
            print(f"   Статус: {note['status']}")
            print(f"   Дата создания: {note['creation_date']}")
            print(f"   Дедлайн: {note['deadline']}")
    else:
        print("Нет заметок для отображения.")


def main():
    # Пример данных
    notes = [
        {
            "username": "Иван Иванов",
            "title": "Первая заметка",
            "description": "Описание первой заметки",
            "status": "Новый",
            "creation_date": "10-12-2024",
            "deadline": "20-12-2024"
        },
        {
            "username": "Петр Петров",
            "title": "Вторая заметка",
            "description": "Описание второй заметки",
            "status": "Выполнен",
            "creation_date": "02-11-2024",
            "deadline": "28-11-2024"
        }
    ]

    display_notes(notes)

    query = input("Введите имя пользователя или заголовок для удаления заметки: ").strip()
    delete_note(notes, query)


if __name__ == "__main__":
    main()
