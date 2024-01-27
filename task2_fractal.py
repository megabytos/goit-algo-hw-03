import turtle


def koch_curve(t, level, size):
    if level == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, level - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(level, size=500):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2 / 3**0.5)
    t.pendown()

    for _ in range(3):
        koch_curve(t, level, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":     
    try:
        level = int(input('Enter recursion level: '))
        draw_koch_snowflake(level)
    except ValueError:
        print("You should enter a number")
    