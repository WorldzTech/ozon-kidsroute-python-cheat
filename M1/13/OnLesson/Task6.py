# Задание: создать 3 треугольника подряд с растоянием между дург другом, используя goto

import random
import turtle

def main():
    t = turtle.Turtle()
    t.pensize(5)

    colors = ["red", "green", "black", "blue"]
    triangle_side_lengths = [20, 70, 120]
    gap = 20

    for i in range(5):
        t.color(random.choice(colors))
        side_length = random.choice(triangle_side_lengths)

        for j in range(3):
            t.forward(side_length)
            t.left(120)

        t.up()
        t.forward(side_length + gap)
        t.down()

    input()


if __name__ == "__main__":
    main()