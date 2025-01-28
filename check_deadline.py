from datetime import datetime

# Получение даты от пользователя
user_date_str = input("Введите дату в формате дд-мм-гггг: ")

try:
    user_date = datetime.strptime(user_date_str, "%d-%m-%Y")
    current_date = datetime.now()

    if current_date > user_date:
        print("Дедлайн истёк.")
    elif current_date.date() == user_date.date():
        print("Дедлайн сегодня.")
    else:
        difference = (user_date - current_date).days
        print(f"Дедлайн ещё не истёк. Осталось {difference} дней")
except ValueError:
    print("Неверный формат даты. Пожалуйста, введите в формате ГГГГ-ММ-ДД.")




