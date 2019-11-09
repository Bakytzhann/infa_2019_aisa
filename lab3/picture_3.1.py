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

    paint_body_man(x - 550, y - 450, x - 700, y - 150)
    paint_body_woman(x - 350, y - 450, x - 450, y - 150, x - 250, y - 150)

    paint_head_man(x - 625, y - 490, r)
    paint_head_woman(x - 350, y - 500, r)

    paint_line_man(x - 700, y - 30)
    paint_line_woman(x - 400, y - 30)

    paint_arm_man(x - 625 - 43, y - 490 + 50 + 15)
    paint_arm_woman(x - 360, y - 420)
    run()


def paint_head_man(x1, y1, r):
    brushColor('Pink')
    circle(x1, y1, r)


def paint_head_woman(x1, y1, r):
    brushColor('Pink')
    circle(x1, y1, r)


def paint_body_man(x1, y1, x2, y2):
    canvas().create_oval(x1, y1, x2, y2, fill='Plum')


def paint_body_woman(x1, y1, x2, y2, x3, y3):
    brushColor('Violet Red')
    polygon([(x1, y1), (x2, y2), (x3, y3)])


def paint_line_man(x1, y1):
    line(x1, y1, x1 - 40, y1 + 5)
    line(x1, y1, x1 + 50, y1 - 150)
    moveTo(x1 + 140, y1)
    lineTo(x1 + 180, y1 + 5)
    line(x1 + 140, y1, x1 + 90, y1 - 150)


def paint_line_woman(x1, y1):
    line(x1, y1, x1, y1 - 120)
    line(x1, y1, x1 - 40, y1)
    moveTo(x1 + 80, y1)
    line(x1 + 80, y1, x1 + 80, y1 - 120)
    line(x1 + 80, y1, x1 + 120, y1 + 2)


def paint_arm_man(x1, y1):
    line(x1, y1, x1 - 100, y1 + 150)
    line(x1 + 85, y1, x1 + 185, y1 + 150)
    moveTo(x1 - 100, y1 + 150)
    brushColor('Yellow')
    polygon([(x1 - 100, y1 + 150), (x1 - 100 - 75, y1 + 150 - 65),
             (x1 - 100 + 20, y1 + 150 - 70 - 20), (x1 - 100, y1 + 150)])
    brushColor('Dark Red')
    circle(x1 - 150, y1 + 150 - 80, 20)
    brushColor('Red')
    circle(x1 - 110, y1 + 150 - 100, 25)
    brushColor('White')
    circle(x1 - 145, y1 + 35, 25)


def paint_arm_woman(x1, y1):
    line(x1, y1, x1 - 140, y1 + 140)
    line(x1 + 20, y1, x1 + 80, y1 + 40)
    line(x1 + 80, y1 + 40, x1 + 160, y1)
    line(x1 + 150, y1 + 30, x1 + 190, y1 - 100)
    brushColor('Red')
    polyline([(x1 + 190, y1 - 100), (x1 + 175, y1 - 150), (x1 + 230, y1 - 145), (x1 + 190, y1 - 100)])
    brushColor('red')
    circle(x1 + 189, y1 - 153, 15)
    circle(x1 + 189 + 30, y1 - 148, 15)


main()
