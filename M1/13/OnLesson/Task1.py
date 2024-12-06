# Задание 1: Создать рисунок их треугольников

import turtle

def main():
    t = turtle.Turtle()

    path = 100

    for i in range(10):
        for j in range(3):
            t.forward(path)
            t.left(120)
        t.right(20)
        path -= 10

    input()

if __name__ == "__main__":
    main()