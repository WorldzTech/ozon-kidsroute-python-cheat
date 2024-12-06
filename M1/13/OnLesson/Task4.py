# Задание: нарисовать линию, состояющую из 4 разных цветов, используя списки

import turtle

def main():
    t = turtle.Turtle()
    t.pensize(5)

    colors = ["red", "green", "black", "blue"]

    for color in colors:
        t.color(color)
        t.forward(50)

    input()


if __name__ == "__main__":
    main()