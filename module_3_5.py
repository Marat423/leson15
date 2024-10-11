def get_multiplied_digits(number): # Создаем функцию
    str_number = str(number)  # Создаем переменую которая переводить в строкой тип
    first = int(str_number[0]) # Находим первое число
    if len(str_number) <= 1: # если число больше 1 возвращем его
        return int(str_number)

    return first * get_multiplied_digits(int(str_number[1:])) # первое число умножаем на последующие


result = get_multiplied_digits(40203)
print(result)

