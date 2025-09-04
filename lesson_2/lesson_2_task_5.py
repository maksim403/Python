month = int(input("Введите номер месяца (1-12): "))


def month_to_season(month):
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


try:
    print(month_to_season(month))
except ValueError:
    print("Введите число от 1 до 12")
