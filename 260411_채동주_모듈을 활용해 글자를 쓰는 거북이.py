import turtle
import random
from tkinter.simpledialog import askstring


def draw_random_text():
    window = turtle.Screen()
    window.title("거북이 (Module Version)")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    t.penup()

    in_str = askstring("문자를 입력", "거북이가 글을 쓰게 도와주세용:")

    if in_str:
        for char in in_str:
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)

            r = random.random()
            g = random.random()
            b = random.random()
            t.pencolor((r, g, b))

            size = random.randint(20, 80)

            t.goto(x, y)
            t.write(char, font=("NanumGothic", size, "bold"))

    t.hideturtle()
    window.exitonclick()


if __name__ == "__main__":
    draw_random_text()