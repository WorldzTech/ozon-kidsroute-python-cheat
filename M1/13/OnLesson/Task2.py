# Задание: создать 3 треугольника подряд с растоянием между дург другом  без использования goto

import turtle

def main():
    t = turtle.Turtle()

    gap = 20
    triangle_side_length = 50
    amount = 3

    for i in range(amount):
        for j in range(3):
            t.forward(triangle_side_length)
            t.left(120)
        t.up()
        t.forward(triangle_side_length + gap)
        t.down()

    input()


if __name__ == "__main__":
    main()