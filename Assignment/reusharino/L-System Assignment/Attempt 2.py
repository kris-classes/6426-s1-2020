import turtle as tu

foo = tu.Turtle()
foo.left(90)
foo.speed(10000)


def draw(l, n):
    if l < n:
        return
    else:
        foo.forward(l)
        foo.left(30)
        draw(l / 2, n)
        foo.right(60)
        draw(l / 2, n)
        foo.left(30)
        foo.backward(l)


d = int(input('Input number: '))
x = input('type y to draw: ')

draw(d, 100)
draw(d, 50)
draw(d, 25)
draw(d, 10)
draw(d, 5)
draw(d, 1)
draw(d, 0.1)
draw(d, 0.01)


input("press enter to stop")
