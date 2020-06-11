import turtle as tu

foo = tu.Turtle()
foo.left(90)
foo.speed(1000000)


def draw(l, n):
    if l < n:
        return
    else:
        foo.forward(l)
        foo.left(30)
        draw(l / 1.5, n)
        foo.right(60)
        draw(l / 1.5, n)
        foo.left(30)
        # foo.dot()
        foo.backward(l)
        # foo.clear()


# d = int(input('Input number: '))

# x = input('type y to draw: ')

d = 100

foo.setposition(-1000, 0)
draw(d, 100)

foo.setposition(-650, 0)
draw(d, 50)

foo.setposition(-300, 0)
draw(d, 25)

foo.setposition(50, 0)
draw(d, 10)

foo.setposition(400, 0)
draw(d, 5)

foo.setposition(750, 0)
draw(d, 1)

input("press enter to stop")
