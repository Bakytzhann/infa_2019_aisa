from graph import *


def main():
    windowSize(1500, 650)
    canvasSize(900, 650)
    brushColor('Light Sky Blue')
    x = 900
    y = 650
    rectangle(0, 0, x, y - 350)
    brushColor('Lawn Green')
    rectangle(0, y - 350, x, y)
    paint_body_mans(160, 280, 80, 450)
    paint_body_mans(810, 280, 730, 450)
    paint_body_woman(350, 280, 280, 470, 420, 470)
    paint_body_woman(550, 280, 480, 470, 620, 470)
    paint_heads(120, 258, 35)
    paint_heads(770, 258, 35)
    paint_heads(350, 258, 35)
    paint_heads(550, 258, 35)
    paint_legs_man(92, 420, 150, 415)
    paint_legs_man(742, 420, 800, 415)
    paint_legs_woman(330, 470)
    paint_legs_woman(530, 470)
    paint_arms_man(90, 310)
    paint_arms_man(740, 310)
    paint_arms_woman(357, 300)
    paint_arms_woman(438, 305)
    paint_ice_cream(450, 310, 460, 170, 410, 100, 510, 100, 23)
    paint_ice_cream(690, 400, 700, 300, 680, 270, 720, 270, 10)
    paint_hearth(200, 400, 20)
    run()


def paint_heads(x1, y1, r):
    """
                функция paint_heads рисует головы всех персонажей
    :param x1: начальная точка по оси х
    :param y1: начальная точка по оси y
    :param r:  радиус голавы персонажей
    :return:
    """
    brushColor('Pink')
    circle(x1, y1, r)


def paint_body_mans(x1, y1, x2, y2):
    """
                функция paint_body_mans рисует тело парня в форме овала
    :param x1: начальная точка по оси х
    :param y1: начальная точка по оси y
    :param x2: начальная точка по оси х
    :param y2: начальная точка по оси y
    :return:
    """
    canvas().create_oval(x1, y1, x2, y2, fill='Plum')


def paint_body_woman(x1, y1, x2, y2, x3, y3):
    """
                функция paint_body_woman рисует тело девушек
    :param x1: первая верхная точка треугольника по оси х
    :param y1: первая верхная точка треугольника по оси y
    :param x2: нижная левая точка треугольника по оси х
    :param y2: нижная левая точка треугольника по оси y
    :param x3: правая нижная точка треугольника по оси х
    :param y3: правая нижная точка треугольника по оси y
    :return:
    """
    brushColor('Violet Red')
    polygon([(x1, y1), (x2, y2), (x3, y3), (x1, y1)])


def paint_legs_man(x, y, x1, y1):
    """
                    функция paint_legs_man рисует ногу парня
        :param x: начальная точка ног парней по оси х
        :param y: начальная точка ног парней по оси y
        :return:
    """
    for k in range(2):
        moveTo(x, y)
        if k == 0:
            lineTo(x - 50, y + 120)
            lineTo((x - 50) - 20, 540)
        else:
            lineTo(x + 20, y + 120)
            lineTo((x + 50) - 10, 535)
        x = x1
        y = y1


def paint_legs_woman(x, y):
    """
                функция paint_legs_woman рисует ногу девушек
    :param x: начальная точка ног девушек по оси х
    :param y: начальная точка ног девушек по оси y
    :return:
    """
    for k in range(2):
        if k == 0:
            moveTo(x, y)
            lineTo(x, y + 90)
            lineTo(x - 20, y + 90)
        else:
            moveTo(x + 40, y)
            lineTo(x + 40, y + 90)
            lineTo(x + 60, y + 90)


def paint_arms_man(x, y):
    """
                функция paint_arms_man рисует руку парня
    :param x: начальная точка по оси х (x = 90)
    :param y: начальная точка по оси y (y = 310)
    :return:
    """
    moveTo(x, y)
    lineTo(x - 50, y + 90)
    moveTo(x + 60, y)
    lineTo(x + 110, y + 90)


def paint_arms_woman(x, y):
    """
                функция paint_arms_woman рисует руку девушки
    :param x: начальная точка по оси х (x = 357
    :param y: начальная точка по оси y (y = 300)
    :return:
    """
    moveTo(x, y)
    lineTo(x + 50, y + 30)
    moveTo(x + 50, y + 30)
    lineTo(x + 100, y + 5)
    moveTo(x, y)
    if x == 357:
        moveTo(x - 15, y)
        lineTo(x - 115, y + 100)
    else:
        moveTo(x + 122, y)
        lineTo(x + 222, y + 100)


def paint_ice_cream(x, y, x1, y1, x2, y2, x3, y3, r):
    """
                Функция 'paint_ice_cream' рисует мороженное
    :param x: нижная часть лентика по оси х (х = 450)
    :param y: точка для нижной части лентика (y = 310)
    :param x1: нижная точка треугольника по оси х
    :param y1: нижная точка треугольника по оси y
    :param x2: вторая левая точка треугольника по оси х
    :param y2: вторая левая точка треугольника по оси y
    :param x3: третья точка треугольника по оси х
    :param y3: третья точка треугольника по оси y
    :param r:  радиус шара который находиться над треугольником
    :return: None
    """
    moveTo(x, y)
    lineTo(x1, y1)
    brushColor('Yellow')
    polygon([(x1, y1), (x2, y2), (x3, y3), (x1, y1)])
    brushColor('Black')
    circle(x2 + (x1 - x2) / 2, y2 - 10, r)
    brushColor('Red')
    circle(x2 + (x3 - x1) + (x1 - x2) / 2, y2 - 10, r + 2)
    brushColor('White')
    circle(x1, y2 - 2 * r, r + 2)


def paint_hearth(x, y, r):
    """
        Функция 'paint_hearth' рисует сердца.
        х и y начальная точка нижной части лентика
        Здесь х - начальная точка по оси х (х = 200).
        Здесь y - начальная точка по оси y (y = 400).
        Здесь r - радиус шара
    """
    moveTo(x, y + 10)
    lineTo(x + 15, y - 210)
    brushColor('Red')
    penColor('Red')
    polygon([(x + 15, y - 200), (x - 20, y - 270), (x + 45, y - 272), (x + 15, y - 200)])
    circle(x - 1, y - 270, r - 2)
    circle(x + 27, y - 270, r - 2)


main()