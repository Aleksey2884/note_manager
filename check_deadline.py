def get_current_status():
    return input("Текущий статус заметки: ").lower()

def update_status(current_status):
    valid_statuses = ["выполнено", "в процессе", "отложено"]
    while True:
        print(f"Текущий статус: {current_status.title()}")
        new_status = input(f"Введите новый статус ({', '.join(valid_statuses)}): ").lower()
        if new_status in valid_statuses:
            current_status = new_status
            break
        else:
            print("Некорректный статус! Попробуйте ещё раз.")
    return current_status

def main():
    current_status = get_current_status()
    updated_status = update_status(current_status)
    print(f"Новый статус заметки: {updated_status.title()}")

if __name__ == "__main__":
    main()