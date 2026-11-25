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
    while True:
        print("\n--- Калькулятор ---")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("0. Выход")
        
        choice = input("Выберите операцию (1/2/3/4/0): ")
        
        if choice == '0':
            print("До свидания!")
            break
            
        if choice not in ('1', '2', '3', '4'):
            print("Неверный ввод. Попробуйте снова.")
            continue
            
        # Обработка ошибок при вводе чисел
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: нужно вводить только числа!")
            continue

        if choice == '1':
            print("Результат:", add(num1, num2))
        elif choice == '2':
            print("Результат:", subtract(num1, num2))
        elif choice == '3':
            print("Результат:", multiply(num1, num2))
        elif choice == '4':
            print("Результат:", divide(num1, num2))

if __name__ == "__main__":
    main()
