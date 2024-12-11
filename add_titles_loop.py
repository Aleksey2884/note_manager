# Создаем пустой список для хранения заголовков
titles = []

while True:
    # Запрашиваем у пользователя новый заголовок
    title = input("Введите заголовок заметки (или 'стоп' для завершения): ")

    if title.lower() == "стоп":
        break

    if title.strip():  # Проверяем, что строка не пустая после удаления пробелов
        titles.append(title)

if len(titles) > 0:
    print("\nСписок введенных заголовков:")
    for i, title in enumerate(titles):
        print(f"{i + 1}. {title}")
else:
    print("\nВы не ввели ни одного заголовка.")