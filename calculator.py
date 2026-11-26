def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def main():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    while True:
        print(
            "\n--- Калькулятор ---\n"
            "1. Сложение\n"
            "2. Вычитание\n"
            "3. Умножение\n"
            "4. Деление\n"
            "0. Выход"
        )
        
        choice = input("Выберите операцию (1/2/3/4/0): ")
        
        if choice == '0':
            print("До свидания!")
            break
            
        if choice not in operations:
            print("Неверный ввод. Попробуйте снова.")
            continue
            
        # Обработка ошибок при вводе чисел
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: нужно вводить только числа!")
            continue

        result = operations[choice](num1, num2)
        print("Результат:", result)

if __name__ == "__main__":
    main()
