# --- Функція для форматування ціни ---
def format_price(price):
    """Приймає число та повертає рядок у форматі 'ціна: xxx.xx грн'."""
    return f"ціна: {price:.2f} грн"


# --- Функція для перевірки наявності товарів ---
def check_availability(*products):
    """
    Приймає довільну кількість товарів.
    Повертає словник з назвами товарів як ключами і True/False — чи є вони в наявності.
    """
    available = {
        "хліб": True,
        "молоко": True,
        "яблука": False,
        "цукор": True,
        "сіль": False
    }

    result = {}
    for product in products:
        result[product] = available.get(product, False)
    return result


# --- Функція для оформлення замовлення ---
def make_order(order):
    """
    Приймає замовлення (словник товарів із цінами).
    Якщо всі товари є — рахує суму.
    """
    availability = check_availability(*order.keys())
    if all(availability.values()):
        total = sum(order.values())
        return f"Замовлення підтверджено! Загальна {format_price(total)}"
    else:
        not_available = [p for p, a in availability.items() if not a]
        return f"Ці товари відсутні: {', '.join(not_available)}"


# --- Точка входу ---
def main():
    """
    Основна частина програми.
    Користувач може вибрати: переглянути ціну або купити.
    """
    print("Вітаємо в магазині!")
    print("Доступні товари: хліб, молоко, яблука, цукор, сіль")
    print("1 — Переглянути ціну\n2 — Купити")

    choice = input("Ваш вибір: ")

    order = {"хліб": 20, "молоко": 35, "цукор": 28}

    if choice == "1":
        print("Ціни на обрані товари:")
        for product, price in order.items():
            print(f"{product.capitalize()}: {format_price(price)}")

    elif choice == "2":
        print(make_order(order))

    else:
        print("Невірна команда!")


# --- Запуск програми ---
if __name__ == "__main__":
    main()
