# module_3_5

number= (402030)
def get_multiplied_digits(number):
    str_number = str(number)

    # Проверка длины строки
    if len(str_number) > 1:
        first = int(str_number[0])
        # Рекурсивный вызов без первой цифры
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)


# Примеры использования
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24

result2 = get_multiplied_digits(402030)
print(result2)  # Вывод: 24


