# Инициализация коллекций данных
portfolio = []  # Список для хранения названий купленных акций
shares = {}  # Словарь для хранения количества акций по названию компании
traded_companies = set()  # Множество для хранения уникальных компаний, с которыми проводились сделки


# Функция для покупки акций
def buy_shares():
    company = input("Введите название компании для покупки акций: ")
    quantity = int(input("Введите количество акций для покупки: "))

    # Проверка, есть ли уже акции этой компании в портфолио
    if company in shares:
        shares[company] += quantity  # Увеличиваем количество акций
    else:
        portfolio.append(company)  # Добавляем компанию в портфолио
        shares[company] = quantity  # Инициализируем количество акций

    traded_companies.add(company)  # Добавляем компанию в множество
    print(f"Куплено {quantity} акций {company}.")


# Функция для продажи акций
def sell_shares():
    company = input("Введите название компании для продажи акций: ")
    if company in shares:
        quantity = int(input("Введите количество акций для продажи: "))
        if shares[company] >= quantity:
            shares[company] -= quantity  # Уменьшаем количество акций
            if shares[company] == 0:
                portfolio.remove(company)  # Удаляем компанию, если акций не осталось
            print(f"Продано {quantity} акций {company}.")
        else:
            print("Недостаточно акций для продажи.")
    else:
        print("У вас нет акций этой компании.")


# Функция для просмотра портфолио
def view_portfolio():
    print("\nВаше портфолио:")
    if not portfolio:
        print("Ваше портфолио пусто.")
    else:
        for company in portfolio:
            print(f"{company}: {shares[company]} акций")


# Функция для просмотра уникальных компаний, с которыми проводились сделки
def view_traded_companies():
    print("\nКомпании, с которыми проводились сделки:")
    if not traded_companies:
        print("Нет компаний с которыми проведены сделки.")
    else:
        for company in traded_companies:
            print(company)


# Главный цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Купить акции")
    print("2. Продать акции")
    print("3. Просмотреть портфолио")
    print("4. Просмотреть компании, с которыми проводились сделки")
    print("5. Выход")

    choice = input("Ваш выбор: ")

    if choice == "1":
        buy_shares()
    elif choice == "2":
        sell_shares()
    elif choice == "3":
        view_portfolio()
    elif choice == "4":
        view_traded_companies()
    elif choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор, попробуйте снова.")
