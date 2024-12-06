# Задание: нарисовать линию, состояющую из 4 случайных цветов

import random
import turtle

def main():
    t = turtle.Turtle()
    t.pensize(5)

    colors = ["red", "green", "black", "blue"]

    for i in range(4):
        t.color(random.choice(colors))
        t.forward(50)

    input()


if __name__ == "__main__":
    main()