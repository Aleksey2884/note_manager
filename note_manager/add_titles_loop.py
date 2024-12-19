## Описание: программа запрашивает у пользователя заголовки, позволяет завершить
#ввод пустой строкой и выводит итоговый список добавленных заголовков.

def get_user_input():
    """Получаем ввод от пользователя."""
    user_input = input("Введите заголовок (или оставьте пустым для завершения): ")
    return user_input.strip()


def main():
    # Инициализируем пустой список для хранения заголовков
    titles = []

    while True:
        title = get_user_input()  # Получаем заголовок от пользователя

        if not title:  # Если введён пустой заголовок, завершаем цикл
            break

        titles.append(title)

    print("\nЗаголовки заметки:")
    for title in titles:
        print(f"- {title}")


if __name__ == "__main__":
    main()