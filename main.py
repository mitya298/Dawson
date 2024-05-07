# This is a sample Python script.
from chapter_1 import game_over


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Chapter 2

# Game Over 2.0
# показывает разыне приёмы работы со строками

def game_over_2_0():
    print("Программа 'Game Over 2.0'")
    print("То же", "самое", "сообщение")
    print("Только",
          "чуть-чуть",
          "побольше")
    print("Вот", end=" ")
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

if __name__ == '__main__':
    game_over()
    game_over_2_0()