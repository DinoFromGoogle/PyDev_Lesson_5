import homework.divisor_master as dm

do_this = True
while do_this:
    a = int(input("Введите нижнюю границу диапазона "))
    b = int(input("Введите верхнюю границу диапазона "))
    c = int(input(f"Введите число для обработки в заданном диапазоне от {a} до {b} "))

    num = dm.set_num_range(c, a, b)

    if dm.is_prime(num):
        print(f"Число {num} является простым")
    else:
        print(f'Число {num} не является простым')

    print("Список целых делителей:")
    print(dm.get_num_int_divisors(num))

    print("Наибольший делитель:")
    print(dm.get_max_divisor(num))

    print("Наибольший простой делитель:")
    print(dm.get_max_prime_divisor(num))

    print("Наименьший простой делитель:")
    print(dm.get_min_prime_divisor(num))

    print("Результат разложения числа на множители")
    print(dm.decompose_on_prime(num))

    print()
    print("Продолжить? (1 - Да)")
    d = int(input())

    if d != 1:
        do_this = False
        print("Всего доброго, ждём Вас снова!")
