titles = []

while True:
        title = input("Введите заголовок заметки (или 'стоп'/enter для завершения): ")

        if title.lower() == 'стоп' or title == '':
            break
        titles.append(title)

print(titles)