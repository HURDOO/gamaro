import random

c = ""  # corner
p = ""  # point


def turtle_setup(canv_width, canv_height):
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    screen.setworldcoordinates(0, 0, canv_width, canv_height)

    t.hideturtle()
    t.speed(0)
    t.color("black")
    return t


def midpoint(a, b):
    ax, ay = a
    bx, by = b
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    return mx, my


def rando_point():
    x = random.randint(0, canv_width)
    y = random.randint(0, canv_height)
    randopoint = (x, y)
    p = randopoint  # Let p be a random point in the window
    return p


def rando_corner():
    randocorner = random.choice(corners)
    c = randocorner
    return c


if __name__ == "__main__":
    import turtle

    canv_width = 500
    canv_height = 500

    t = turtle_setup(400, 400)

    turtle_setup(canv_width, canv_height)

    middlex = (canv_width / 2)
    corner1 = (middlex, canv_height)
    corner2 = (0, 0)
    corner3 = (canv_width, 0)
    corners = [corner1, corner2, corner3]

    p = rando_point()
    c = rando_corner()
    m = midpoint(p, c)

    t.up()
    for i in range(100000):
        c = rando_corner()
        m = midpoint(p, c)
        t.goto(m)

        if i > 5:
            t.pendown()
            t.dot(2)  # dot size
            t.penup()
            p = m

        # turtle.update()
