import datetime
class Note:
    def __init__(self, title, content, created_date=None, issue_date=None):
        self.title = title
        self.content = content
        self.created_date = created_date or datetime.datetime.now().date()
        self.issue_date = issue_date
    def __repr__(self):
        return f'Note({self.title}, {self.created_date}, {self.issue_date})'
notes = []
def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    issue_date_str = input("Укажите дату исполнения (в формате ДД-ММ-ГГГГ): ")
    try:
        issue_date = datetime.datetime.strptime(issue_date_str, "%d-%m-%Y").date()
    except ValueError:
        print("Ошибка: неверный формат даты. Используйте формат ДД-ММ-ГГГГ.")
        return
    note = Note(title, content, issue_date=issue_date)
    notes.append(note)
    print(f"Заметка '{note.title}' успешно создана! Дата создания: {note.created_date:%d-%m-%Y}, "
          f"Срок исполнения: {note.issue_date:%d-%m-%Y}")
def display_notes():
    if not notes:
        print("Нет заметок для отображения.")
        return
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note.title}")
        print(f"Дата создания: {note.created_date:%d-%m-%Y}")
        print(f"Срок исполнения: {note.issue_date:%d-%m-%Y}")
        print(f"Содержание:\n{note.content}\n")
def update_note():
    index = int(input("Введите номер заметки для обновления: "))
    if index < 1 or index > len(notes):
        print("Неправильный номер заметки.")
        return
    note = notes[index - 1]
    new_title = input(f"Введите новый заголовок ({note.title}): ") or note.title
    new_content = input(f"Введите новое содержание ({note.content}): ") or note.content
    new_created_date = input(f"Введите новую дату создания (формат DD-MM-YYYY): ")
    new_issue_date = input(f"Введите новую дату исполнения (формат DD-MM-YYYY): ")
    note.title = new_title
    note.content = new_content
    if new_created_date:
        try:
            note.created_date = datetime.datetime.strptime(new_created_date, "%d-%m-%Y").date()
        except ValueError:
            print("Ошибка! Неверная дата создания. Дата оставлена без изменений.")
    if new_issue_date:
        try:
            note.issue_date = datetime.datetime.strptime(new_issue_date, "%d-%m-%Y").date()
        except ValueError:
            print("Ошибка! Неверная дата исполнения. Дата оставлена без изменений.")
    print(f"Заметка '{new_title}' успешно обновлена.")
def delete_note():
    index = int(input("Введите номер заметки для удаления: "))
    if index < 1 or index > len(notes):
        print("Ничего не найдено.")
        return
    deleted_note = notes.pop(index - 1)
    print(f"Заметка '{deleted_note.title}' удалена.")
def search_notes():
    query = input("Введите строку для поиска: ").lower()
    results = [note for note in notes if query in note.title.lower() or query in note.content.lower()]
    if not results:
        print("Ничего не найдено.")
        return
    for result in results:
        print(result.title)
        print(f"Дата создания: {result.created_date:%d-%m-%Y}")
        print(f"Срок исполнения: {result.issue_date:%d-%m-%Y}")
        print(f"Содержание:\n{result.content}\n")
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")
        choice = input("Выберите пункт меню: ")
        if choice == '1':
            create_note()
        elif choice == '2':
            display_notes()
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            search_notes()
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")
    print("Завершение программы!")

if __name__ == "__main__":
    main_menu()        
