import turtle
import math

# Функція для малювання фрактала "Дерево Піфагора"
def draw_pythagoras_tree(branch_len, level, angle_deviation):
    """
    Рекурсивно малює дерево Піфагора.
    
    branch_len: Довжина поточної гілки.
    level: Поточний рівень рекурсії.
    angle_deviation: Кут нахилу від вертикалі для бічних гілок (у градусах).
                     Для вашого прикладу це 45.
    """
    if level == 0:
        return

    # Намалювати поточну гілку (стовбур або частина гілки)
    turtle.forward(branch_len)
    
    # --- Створити праву гілку ---
    # Повернути черепаху праворуч на вказаний кут
    turtle.right(angle_deviation)
    
    # Обчислити довжину нової гілки (за теоремою Піфагора для 45-45-90 трикутника)
    # branch_len * sin(45) або branch_len * cos(45)
    new_len = branch_len * math.cos(math.radians(angle_deviation))
    
    # Рекурсивний виклик для правої гілки
    draw_pythagoras_tree(new_len, level - 1, angle_deviation)
    
    # --- Створити ліву гілку ---
    # Повернути черепаху вліво, щоб компенсувати правий поворот і зробити поворот вліво
    # Загальний поворот відносно центральної осі має бути 2 * angle_deviation
    turtle.left(2 * angle_deviation)
    
    # Рекурсивний виклик для лівої гілки
    draw_pythagoras_tree(new_len, level - 1, angle_deviation)
    
    # --- Повернутися до вихідної точки та орієнтації ---
    # Повернути черепаху назад, щоб вона дивилася вздовж поточної гілки (вгору)
    turtle.right(angle_deviation)
    # Пройти назад довжину поточної гілки
    turtle.backward(branch_len)

# Основна функція для налаштування та запуску
def main():
    # Запит рівня рекурсії у користувача
    try:
        user_level = int(input("Введіть рівень рекурсії (рекомендовано від 5 до 12): "))
        if user_level < 1:
            print("Рівень рекурсії повинен бути позитивним цілим числом.")
            return
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    # Налаштування екрана
    screen = turtle.Screen()
    screen.title(f"Фрактал 'Дерево Піфагора' (Рівень {user_level})")
    screen.bgcolor("white") # Білий фон

    # Налаштування черепахи
    turtle.speed(0) # Максимальна швидкість малювання
    turtle.hideturtle() # Сховати черепаху
    turtle.color("brown") # Колір, як у прикладі
    turtle.pensize(1) # Тонка лінія

    # Встановити початкову позицію та орієнтацію
    turtle.left(90) # Черепаха дивиться вгору
    # Підняти перо, щоб перемістити черепаху вниз, не малюючи
    turtle.penup()
    turtle.goto(0, -screen.window_height() // 2 + 50) # Почати знизу по центру
    turtle.pendown() # Опустити перо для малювання

    # Налаштування для вашого прикладу
    initial_branch_len = 150 # Початкова довжина стовбура
    pythagoras_angle = 45     # Кут відхилення від вертикалі (45 + 45 = 90 між гілками)

    # Виклик функції малювання
    print(f"Починаю малювання дерева Піфагора з рівнем рекурсії {user_level}...")
    draw_pythagoras_tree(initial_branch_len, user_level, pythagoras_angle)
    print("Малювання завершено. Щоб вийти, закрийте вікно.")

    # Залишити вікно відкритим, поки користувач не закриє його
    turtle.done()

# Запуск програми
if __name__ == "__main__":
    main()