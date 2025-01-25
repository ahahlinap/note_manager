status = input("Введите текущий статус заметки: ")
print(f"Текущий статус заметки: '{status}'")

print("Выберите новый статус заметки(1-Выполнено,2-В процессе,3-Отложено): ")



status_changed = False

while not status_changed:
    choice = input("Введите номер статуса (1, 2 или 3): ")
    if choice == '1':
        status = "выполнено"
        print(f"Обновленный статус заметки: '{status}'")
        status_changed = True
    elif choice == '2':
        status = "в процессе"
        print(f"Обновленный статус заметки: '{status}'")
        status_changed = True
    elif choice == '3':
        status = "отложено"
        print(f"Обновленный статус заметки: '{status}'")
        status_changed = True
    else:
        print("Неверный статус. Попробуйте ещё раз: возможные варианты ввода 1,2 или 3")
