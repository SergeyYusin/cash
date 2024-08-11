# Магазин 18+
cigarettes = {1: 'Winston', 2: 'LM', 3: 'Chesterfild'}
alcohol = {1: 'Vodka', 2: 'Beer', 3: 'Wine'}


def purchases(cigarette, alcoho):
    suma = 0
    student = input("Вы студент: ").lower() == 'да'
    cnum = int(input(f'В наличии есть {cigarette}, напишите цифру товара: '))
    alnum = int(input(f'В наличии есть {alcoho}, напишите цифру товара: '))
    if cnum == 1:
        print(f'{cigarette[cnum]}: 150р')
        suma += 150
    elif cnum == 2:
        print(f'{cigarette[cnum]}: 125р')
        suma += 125
    else:
        print(f'{cigarette[cnum]}: 175р')
        suma += 175
    if alnum == 1:
        print(f'{alcoho[alnum]}: 455р')
        suma += 455
    elif alnum == 2:
        print(f'{alcoho[alnum]}: 350р')
        suma += 350
    else:
        print(f'{alcoho[alnum]}: 800р')
        suma += 800
    return discounts(suma, student)


def discounts(summ: int, student: bool):
    age = int(input("Сколько вам лет: "))
    if age > 18:
        if student:
            cheq = summ - (summ * 0.1)
            print(f'Скидка 10%\n'
                  f'Сумма покупки: {cheq}р')
        elif age >= 75:
            cheq = summ - (summ * 0.2)
            print(f'Скидка 20%\n'
                  f'Сумма покупки: {cheq}р')
    else:
        print(f'Сумма покупки: {summ}р')


if __name__ == '__main__':
    purchases(cigarettes, alcohol)
