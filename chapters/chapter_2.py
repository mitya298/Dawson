# Chapter 2

# Game Over 2.0
# показывает разыне приёмы работы со строками

def game_over_2_0():
    print("\n\n\nПрограмма 'Game Over 2.0'")
    print("То же", "самое", "сообщение")
    print("Только",
          "чуть-чуть",
          "побольше")
    print("Вот", end="**")
    print("оно...")
    print(
        """
         _____
        /
        |
        |
        |
        \\______
        """)
    input("\n\n Нажмите Enter, чтобы выйти...")

def fancy_credits():
    print("\t\t\t\'Воображаемые\' \"благодарности\"..\n\n\t\t\t \\ \\ \\ \a")

#забавные строки (конкатенация и повторение)
def silly_strings():
    print("\tЭта " + "строка\n"+"врядли " + "удивит Вас"\
          + "\nЭто конкатенация..")
    print("\nА это повторение строк:\n" + "Пирожные "*10)
    input("\n\nНажмите ENTER, чтобы выйти....")

# математические операции
# типы данных - целые (int) дробные (float),
# decimal - модуль для поддержки точной десятичной арифметики для дробных чисел
def word_problems():
    print("Сложение  и вычитание: 800 - 40 + 20 = ", 800 - 40 + 20)
    print("Умножение: 6 * 3 = ", 6 * 3)
    print("Деление: 107 / 4 = ", 107 / 4)
    print("Остаток от деления - \'нахождение остатка по модулю\': 107 % 4 = ", 107 % 4)
    print("Деление нацело - \'дробная часть отбрасывается!\': 107 // 4 = ", 107 // 4)

# переменные
# имя переменной может состоять только из цифр, букв и знаков подчеркивания;
# имя переменной не может начинаться с цифры (SyntaxError: invalid decimal literal).
def greeter():
    name = "Вася"
    print("Привет, ", name)
    input("Нажмите ENTER, чтобы выйти...\n")

# программа персональный привет
def personal_greeter():
    name = input('\nВведите своё имя:')
    print('Вы ввели - ', name)
    print ('Привет, ', name)
    input('\n\nНажмите Enter для завершения...')

# программа манипуляции с цитатой
# пример строковых методов upper, lower, title, replace

def quotation_manipulation():
    quote = "Думаю, на мировом рынке будет продано штук 5 компьютеров"
    print("\nИсходная цитата")
    print(quote)
    print("\nОна же в верхнем регистре: ")
    print(quote.upper())
    print("\nОна же в нижнем регистре: ")
    print(quote.lower())



# list 61