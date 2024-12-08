# Запрашиваем информацию у пользователя
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

from datetime import datetime

# Исходные даты в формате строки
created_date = '19-03-2024'
issue_date = '05-10-2024'

# Преобразуем строки в объекты datetime
dt_created_date = datetime.strptime(created_date, '%d-%m-%Y')
dt_issue_date = datetime.strptime(issue_date, '%d-%m-%Y')

# Формируем новый формат вывода без года
temp_created_date = dt_created_date.strftime('%d-%m')
temp_issue_date = dt_issue_date.strftime('%d-%m')

# Выводим новые значения
from datetime import datetime

# Исходные даты в формате строки
created_date = '07-12-2024'
issue_date = '07-01-2025'

# Преобразуем строки в объекты datetime
dt_created_date = datetime.strptime(created_date, '%d-%m-%Y')
dt_issue_date = datetime.strptime(issue_date, '%d-%m-%Y')

# Формируем новый формат вывода без года
temp_created_date = dt_created_date.strftime('%d-%m')
temp_issue_date = dt_issue_date.strftime('%d-%m')

# Выводим введенные данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print(f'Created Date: {temp_created_date}')
print(f'Issue Date: {temp_issue_date}')