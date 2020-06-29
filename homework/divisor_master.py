import math

# Простым назвается целое положительное число, которое
# может делиться без остатка только на единицу или само на себя

# функция для проверки допустимых значений чисел
# передающихся в качестве параметра в функции модуля
#
# вместо жесткой привязки к диапазону от 1 до 1000 решил
# сделать функцию принимающую число для анализа,
# граничные значения области допустимых значений
#
# если граничные значения или значение числа для анализа
# не являются допустимыми, функция предлагаем их заменить
# до тех пор, пока все значения не будут корректными
def set_num_range(int_num, start_num, end_num):

    while type(start_num) != int or start_num < 1:
        print("Некорретный ввод: задайте целое число больше ноля")
        start_num = int(input("start_num = "))

    while type(end_num) != int or end_num < 1:
        print("Некорретный ввод: задайте целое число больше ноля")
        end_num = int(input("end_num = "))

    difference = int(math.fabs(start_num - end_num))

    while start_num == end_num or difference < 2:
        print("Разность между крайнми значениями диапазона должна быть больше единицы")
        start_num = int(input("start_num = "))
        end_num = int(input("end_num =  "))
        difference = math.fabs(start_num - end_num)

    a = start_num if start_num < end_num else end_num
    b = end_num if end_num > start_num else start_num


    while int_num < 1 or type(int_num) != int:
        print(f"Задайте целое положительное число в заданном диапазоне {a} до {b}")
        int_num = int(input("int_num = "))

    while int_num < a or int_num > b:
        print(f"Задайте целое положительное число в заданном диапазоне {a} до {b}")
        int_num = int(input("int_num = "))

    return int_num


# функция определяющая является ли число простым
def is_prime(int_num):
    return len(get_num_int_divisors(int_num)) <= 2


# получить все целые делители числа
# при делении на которые возвращается
# целый результат
def get_num_int_divisors(int_num):
    divisors_list = []
    for i in range(1, int_num + 1):
        res = int_num % i
        if res == 0:
            divisors_list.append(i)

    return divisors_list


# возвращает наибольший целый делитель числа
def get_max_divisor(int_num):
    if is_prime(int_num):
        return int_num
    divisors_list = get_num_int_divisors(int_num)
    return max(divisors_list[:-1])


# возвращает наибольший простой делитель числа
def get_max_prime_divisor(int_num):
    if is_prime(int_num):
        return int_num

    divisors_list = get_num_int_divisors(int_num)
    prime_nums_in_list = [num for num in divisors_list if is_prime(num)]

    return max(prime_nums_in_list)


# возвращает наименьший простой делитель числа
# отличный от единицы, если их больше одного
# и если число не является простым
def get_min_prime_divisor(int_num):

    if is_prime(int_num):
        return 1

    divisors_list = get_num_int_divisors(int_num)
    prime_nums_in_list = [num for num in divisors_list if is_prime(num)]

    return min(prime_nums_in_list[1:])


# функция осуществляет разложения числа на простые
# множители
def decompose_on_prime(int_num):

    if is_prime(int_num):
        return [1, int_num]

    decompose_list = []
    divisor = 2

    # while count > 1:
    #     divisor = get_min_prime_divisor(int_num)
    #     count = divisor
    #     if divisor > 1:
    #         decompose_list.append(divisor)
    #     int_num = int(int_num / divisor)

    while divisor > 1:
        divisor = get_min_prime_divisor(int_num)
        int_num = int(int_num / divisor)
        if divisor > 1:
            decompose_list.append(divisor)
        else:
            decompose_list.append(int_num)

    return decompose_list
