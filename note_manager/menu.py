def create_note():
    """Функция создания новой заметки"""
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    status = input("Введите статус заметки (например, 'Новая', 'В процессе' и т.п.): ")
    return {"title": title, "content": content, "status": status}


def display_notes(notes):
    """Функция отображения всех заметок"""
    if not notes:
        print("Список заметок пуст.")
        return
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note['title']}: {note['content']} ({note['status']})")


def update_note(note):
    """Функция обновления существующей заметки"""
    new_title = input("Новый заголовок (оставьте пустым, чтобы оставить прежний): ") or note["title"]
    new_content = input("Новое содержание (оставьте пустым, чтобы оставить прежнее): ") or note["content"]
    new_status = input("Новый статус (оставьте пустым, чтобы оставить прежний): ") or note["status"]
    return {"title": new_title, "content": new_content, "status": new_status}


def delete_note(notes, index):
    """Функция удаления заметки по индексу"""
    if 0 <= index < len(notes):
        del notes[index]
        print("Заметка удалена успешно.")
    else:
        print("Неверный номер заметки.")


def search_notes(notes, keyword="", status=""):
    """Функция поиска заметок по ключевым словам и статусу"""
    results = []
    for note in notes:
        if keyword.lower() in note["title"].lower() + note["content"].lower() \
                and (not status or status == note["status"]):
            results.append(note)
    return results


# Основная программа
if __name__ == "__main__":

    notes = []

    while True:

        print(
            """

            Меню действий:

            1. Создать новую заметку

            2. Показать все заметки

            3. Обновить заметку

            4. Удалить заметку

            5. Найти заметки

            6. Выйти из программы

            """
        )

        choice = input("Ваш выбор: ")

        if choice == "1":
            note = create_note()
            notes.append(note)

        elif choice == "2":
            display_notes(notes)

        elif choice == "3":
            if notes:
                display_notes(notes)
                try:
                    index = int(input("Введите номер заметки для обновления: ")) - 1
                    if 0 <= index < len(notes):
                        notes[index] = update_note(notes[index])
                    else:
                        print("Неверный номер заметки.")
                except ValueError:
                    print("Пожалуйста, введите корректный номер заметки.")
            else:
                print("Список заметок пуст.")

        elif choice == "4":
            if notes:
                display_notes(notes)
                try:
                    index = int(input("Введите номер заметки для удаления: ")) - 1
                    delete_note(notes, index)
                except ValueError:
                    print("Пожалуйста, введите корректный номер заметки.")
            else:
                print("Список заметок пуст.")

        elif choice == "5":
            keyword = input("Введите ключевое слово для поиска: ")
            status = input("Введите статус для поиска (или оставьте пустым): ")
            found_notes = search_notes(notes, keyword, status)
            display_notes(found_notes)

        elif choice == "6":
            print("Программа завершена. Спасибо за использование!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")
