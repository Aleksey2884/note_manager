def show_current_status(current_status):
    """
    Показывает текущий статус заметки.
    """
    print(f"Текущий статус заметки: \"{current_status}\"")


def select_new_status():
    """
    Предлагает пользователю выбрать новый статус из списка.
    Возвращает выбранный статус.
    """
    statuses = ["выполнено", "в процессе", "отложено"]

    print("\nВыберите новый статус заметки:")
    for i, status in enumerate(statuses, start=1):
        print(f"{i}. {status}")

    choice = int(input("Ваш выбор: "))

    # Проверяем, чтобы выбор был в пределах допустимого диапазона
    if choice < 1 or choice > len(statuses):
        raise ValueError("Некорректный выбор. Попробуйте снова.")

    new_status = statuses[choice - 1]
    return new_status


def update_status(current_status):
    """
    Обновляет статус заметки.
    """
    try:
        new_status = select_new_status()
        print(f"\nСтатус заметки успешно обновлен на: \"{new_status}\"")
    except ValueError as e:
        print(e)
        update_status(current_status)  # Повторяем запрос при ошибке


def main():
    current_status = "в процессе"  # Предполагать, что текущим статусом является "в процессе"
    show_current_status(current_status)
    update_status(current_status)


if __name__ == "__main__":
    main()