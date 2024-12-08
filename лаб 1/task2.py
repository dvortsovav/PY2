from task_1 import Book, BankAccount, SocialNetwork

if __name__ == "__main__":
    try:
         book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)
         account = BankAccount("98765", 500.0)
         social_network = SocialNetwork("TwitterClone", 100000)
    except ValueError as e:
         print(f"Ошибка при создании объекта: {e}")

    try:
        book.read_chapter(-1) # Вызвать метод с некорректными аргументами (отрицательный номер главы)
    except ValueError as e:
        print(f"Ошибка: неправильные данные")

    try:
        account.deposit(-100) # Вызвать метод с некорректными аргументами (отрицательная сумма депозита)
    except ValueError as e:
        print(f"Ошибка: неправильные данные")

    try:
        social_network.add_users(-50) # Вызвать метод с некорректными аргументами (отрицательное количество новых пользователей)
    except ValueError as e:
        print(f"Ошибка: неправильные данные")
