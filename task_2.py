import turtle

def draw_pifagor_tree(branch_len, level):
    if level == 0:
        return

    turtle.forward(branch_len)
    
    # Права гілка
    turtle.right(45)
    draw_pifagor_tree(branch_len * 0.7, level - 1)
    
    # Ліва гілка
    turtle.left(90)
    draw_pifagor_tree(branch_len * 0.7, level - 1)
    
    # Повернення в початкове положення
    turtle.right(45)
    turtle.backward(branch_len)

def main():
    try:
        level = int(input("Введіть рівень рекурсії (рекомендовано 6-10): "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    turtle.speed('fastest')
    turtle.left(90) # Повертаємо черепашку вгору
    turtle.up()
    turtle.goto(0, -200) # Позиція початку
    turtle.down()
    
    draw_pifagor_tree(100, level)
    turtle.done()

if __name__ == "__main__":
    main()
