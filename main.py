import time
from datetime import datetime

print(datetime.now())

current_hour = datetime.now().hour
if current_hour >= 20 or current_hour < 10:
    print("Мы сейчас закрыты! Приходите завтра с 10:00 до 20:00😊")

money = 0
Adult = False
pay = False
dishes = []

rolls = ["1) Калифорния | 500р", "2) Лава с лососем | 500р", "3) Филадельфия | 650р", "4) Темпура ролл | 550р",
         "5) Гейша ролл | 450р"]
drinks = ["1) Сок добрый (500 мл) | 90р", "2) Кола добрый (500 мл) | 100р", "3) Чай липтон (500 мл) | 80р",
          "4) Вода негазированная (500 мл) | 50р", "5) Энергетик Alpha Energy (300 мл) | 100р"]
all_sushi = ["1) Суши сяке (30гр): Лосось, Рис | 150р", "2) Суши унаги (35гр): Угорь, Рис, Соус унаги, Кунжут | 160р"]
soups = ["1) Том Ям | 750р"]
woks = ["1) Вок с курицей | 300р", "2) Вок с говядиной | 350р", "3) Вок с креветками | 500р"]
custom_rolls = ["Творожный сыр | + 80р", "Огурец | + 30р", "Авакадо | + 50р", "Креветки | 140р", "Лосось | 180р"]

print("=" * 50)
print('Доставка еды из морепродуктов "Мать Габена"')
print("=" * 50)
print()

print("🧑‍💻Вход в приложение")
name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")

try:
    year_of_birth = int(input("Введите год рождения: "))
    Adult = year_of_birth <= 2007
except:
    print("Некорректный ввод!")
    exit()

if Adult:
    print(
        "Так как вы совершеннолетний, порции будут в 1,2 раза больше обычных! А так же вам будут доступно больше позиций в меню")
    time.sleep(2)

print("\n" * 3)
print("=" * 50)
print('Доставка еды из морепродуктов "Мать Габена"')
print("=" * 50)
print()

print(f"Благодарим за регистрацию, {last_name} {name}!")
time.sleep(2)


def show_header():
    print("\n" * 3)
    print("=" * 50)
    print('Доставка еды из морепродуктов "Мать Габена"')
    print("=" * 50)


def menu():
    global pay

    while not pay:
        show_header()
        print("🏠Меню")
        print("Выберите раздел:")
        print("Роллы == Суши == Супы == Вок == Напитки == Кастом роллы")
        print('Для оплаты напишите "Оплата"')
        print('Для выхода напишите "Выход"')
        choice = input()

        if choice == "Кастом роллы":
            custom_roll()
        elif choice == "Роллы":
            roll()
        elif choice == "Суши":
            sushi()
        elif choice == "Супы":
            soup()
        elif choice == "Вок":
            wok()
        elif choice == "Напитки":
            drink()
        elif choice == "Оплата":
            paying()
        elif choice == "Выход":
            print("До свидания!")
            break
        else:
            print("Такой команды нет!")
            input("Нажмите Enter чтобы продолжить")


def roll():
    global money, dishes

    while True:
        show_header()
        print("Вот весь выбор роллов:")
        for i, roll_item in enumerate(rolls, 1):
            print(roll_item)
        print("6) Выход в меню")

        try:
            roll_type = int(input("Введите номер желаемого ролла: "))
        except:
            print("Пожалуйста, введите число!")
            input("Нажмите Enter чтобы продолжить")
            continue

        if roll_type == 6:
            break
        elif 1 <= roll_type <= 5:
            prices = [500, 500, 650, 550, 450]
            money += prices[roll_type - 1]
            dishes.append(rolls[roll_type - 1])
            print(f"Добавлено: {rolls[roll_type - 1]}")
        else:
            print("Неверный номер!")

        input("Нажмите Enter чтобы продолжить")


def sushi():
    global money, dishes

    while True:
        show_header()
        print("Вот весь выбор суши:")
        for sushi_item in all_sushi:
            print(sushi_item)
        print("3) Выход в меню")

        try:
            sushi_type = int(input("Введите номер желаемых суши: "))
        except:
            print("Пожалуйста, введите число!")
            input("Нажмите Enter чтобы продолжить")
            continue

        if sushi_type == 3:
            break
        elif sushi_type == 1:
            money += 150
            dishes.append(all_sushi[0])
            print(f"Добавлено: {all_sushi[0]}")
        elif sushi_type == 2:
            money += 160
            dishes.append(all_sushi[1])
            print(f"Добавлено: {all_sushi[1]}")
        else:
            print("Неверный номер!")

        input("Нажмите Enter чтобы продолжить")


def soup():
    global money, dishes

    while True:
        show_header()
        print("Вот весь выбор супов:")
        for soup_item in soups:
            print(soup_item)
        print("2) Выход в меню")

        try:
            soup_type = int(input("Введите номер желаемого супа: "))
        except:
            print("Пожалуйста, введите число!")
            input("Нажмите Enter чтобы продолжить")
            continue

        if soup_type == 2:
            break
        elif soup_type == 1:
            money += 750
            dishes.append(soups[0])
            print(f"Добавлено: {soups[0]}")
        else:
            print("Неверный номер!")

        input("Нажмите Enter чтобы продолжить")


def wok():
    global money, dishes

    while True:
        show_header()
        print("Вот весь выбор вок:")
        for wok_item in woks:
            print(wok_item)
        print("4) Выход в меню")

        try:
            wok_type = int(input("Введите номер желаемого вока: "))
        except:
            print("Пожалуйста, введите число!")
            input("Нажмите Enter чтобы продолжить")
            continue

        if wok_type == 4:
            break
        elif wok_type == 1:
            money += 300
            dishes.append(woks[0])
            print(f"Добавлено: {woks[0]}")
        elif wok_type == 2:
            money += 350
            dishes.append(woks[1])
            print(f"Добавлено: {woks[1]}")
        elif wok_type == 3:
            money += 500
            dishes.append(woks[2])
            print(f"Добавлено: {woks[2]}")
        else:
            print("Неверный номер!")

        input("Нажмите Enter чтобы продолжить")


def drink():
    global money, dishes

    while True:
        show_header()
        print("Вот весь выбор напитков:")

        if Adult:
            for drink_item in drinks:
                print(drink_item)
            print("6) Выход в меню")
        else:
            for i in range(4):
                print(drinks[i])
            print("5) Выход в меню")

        try:
            drink_type = int(input("Введите номер желаемого напитка: "))
        except:
            print("Пожалуйста, введите число!")
            input("Нажмите Enter чтобы продолжить")
            continue

        if Adult:
            if drink_type == 6:
                break
            elif 1 <= drink_type <= 5:
                prices = [90, 100, 80, 50, 100]
                money += prices[drink_type - 1]
                dishes.append(drinks[drink_type - 1])
                print(f"Добавлено: {drinks[drink_type - 1]}")
            else:
                print("Неверный номер!")
        else:
            if drink_type == 5:
                break
            elif 1 <= drink_type <= 4:
                prices = [90, 100, 80, 50]
                money += prices[drink_type - 1]
                dishes.append(drinks[drink_type - 1])
                print(f"Добавлено: {drinks[drink_type - 1]}")
            else:
                print("Неверный номер!")

        input("Нажмите Enter чтобы продолжить")


def custom_roll():
    global money, dishes

    while True:
        show_header()
        print("Создайте свои роллы!")
        print("Ингредиенты:")
        for i, j in enumerate(custom_rolls, 1):
            print(f"{i}) {j}")
        print("6) Выход в меню")

        try:
            ing_choice = int(input("Выберите ингредиент для добавления: "))
        except:
            print("Пожалуйста, введите число!")
            input("Нажмите Enter чтобы продолжить")
            continue

        if ing_choice == 6:
            break
        elif 1 <= ing_choice <= 5:
            prices = [80, 30, 50, 140, 180]
            money += prices[ing_choice - 1]
            dishes.append(f"Кастомный ролл: {custom_rolls[ing_choice - 1]}")
            print(f"Добавлен ингредиент: {custom_rolls[ing_choice - 1]}")
        else:
            print("Неверный номер!")

        money += 100

        input("Нажмите Enter чтобы продолжить")
    dishes.append("Стандартное наполнение ролла (нори, рис)")

def paying():
    global pay, money, dishes

    if not dishes:
        print("Ваша корзина пуста!")
        input("Нажмите Enter чтобы продолжить")
        return

    pay = True
    show_header()

    print("Как вы хотите получить заказ? (Самовывоз/Доставка)")
    print("За самовывоз скидка 10%!")
    delivery_type = input().strip()

    original_money = money
    if delivery_type == "Самовывоз":
        discount = money // 10
        money -= discount
        print(f"Применена скидка 10%: -{discount}р")
    elif delivery_type == "Доставка":
        address = input("Введите адрес доставки: ")
        print(f"Доставка по адресу: {address}")
    else:
        print("Неверный тип доставки!")
        pay = False
        input("Нажмите Enter чтобы продолжить")
        return

    print("\nВаш заказ:")
    for dish in dishes:
        print(f"  - {dish}")

    print(f"\nИтого к оплате: {money} рублей")
    if delivery_type == "Самовывоз":
        print(f"(Без скидки: {original_money} рублей)")

    print("\nРеквизиты для оплаты:")
    print("Перевод на СБЕР +79617135002")
    print("После проверки оплаты ваш заказ будет принят на кухню")

    if delivery_type == "Самовывоз":
        print("\nПриходите на адрес: Кемерово, Весенняя улица 28, 5 этаж")

    input("\nНажмите Enter для завершения")

menu()