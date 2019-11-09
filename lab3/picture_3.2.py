from graph import *


def main():
    windowSize(1500, 650)
    canvasSize(900, 650)
    brushColor('Light Sky Blue')
    x = 900
    y = 650
    r = 55
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
    paint_ice_cream(447, 310, 435, 80,  20)
    paint_hearth(200, 400, 20)

    run()


def paint_heads(x1, y1, r):
    brushColor('Pink')
    circle(x1, y1, r)


def paint_body_mans(x1, y1, x2, y2):
    canvas().create_oval(x1, y1, x2, y2, fill='Plum')


def paint_body_woman(x1, y1, x2, y2, x3, y3):
    brushColor('Violet Red')
    polygon([(x1, y1), (x2, y2), (x3, y3), (x1, y1)])


def paint_legs_man(x, y, x1, y1):
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
    moveTo(x, y)
    lineTo(x - 50, y + 90)
    moveTo(x + 60, y)
    lineTo(x + 110, y + 90)


def paint_arms_woman(x, y):
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


def paint_ice_cream(x, y, x1, y1, r):
    moveTo(x, y)
    lineTo(x + 10, y - 130)
    brushColor('Yellow')
    polygon([(x + 10, y - 130), (x - 40, y - 220), (x + 50, y - 225), (x + 10, y - 130)])
    brushColor('Black')
    circle(x1 - 5, y1, r)
    brushColor('Red')
    circle(x1 + 40, y1 - 7, r + 3)
    brushColor('White')
    circle(x1 + 15, y1 - 30, r + 2)


def paint_hearth(x, y, r):
    moveTo(x, y + 10)
    lineTo(x + 15, y - 210)
    brushColor('Red')
    penColor('Red')
    polygon([(x + 15, y - 200), (x - 20, y - 270), (x + 45, y - 272), (x + 15, y - 200)])
    circle(x - 1, y - 270, r - 2)
    circle(x + 27, y - 270, r - 2)


main()

