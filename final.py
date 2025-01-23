username = input("Введите ваше имя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки (ДД.ММ.ГГГГ): ")
issue = input("Введите дату истечения заметки (ДД.ММ.ГГГГ): ")
title1 = input("Введите заголовок 1: ")
title2 = input("Введите заголовок 2: ")

note = [
    username,
    content,
    status,
    created_date,
    issue,
    [title,title1,title2]
]
print(note)