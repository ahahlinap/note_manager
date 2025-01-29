

def create_note():
    username = input("Введите ваше имя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки: ")
    created_date = input("Введите дату создания заметки (ДД.ММ.ГГГГ): ")
    issue_date = input("Введите дату истечения заметки (ДД.ММ.ГГГГ): ")

    note = {
        'Имя': username,
        'Заголовок': title,
        'Описание': content,
        'Статус': status,
        'Дата создания': created_date,
        'Дедлайн': issue_date}

    return note

notes = []

while True:
    response = input("Хотите добавить новую заметку? (да или нет): ")
    if response.lower() == 'да':
        new_note = create_note()
        notes.append(new_note)
    if response.lower() == 'нет':
        print(notes)
        break

