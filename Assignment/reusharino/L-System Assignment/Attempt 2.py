import turtle as tu

foo = tu.Turtle()
foo.left(90)
foo.speed(10)


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
j = int(input('input stop number: '))
x = input('type y to draw: ')

draw(d, j)
input("")
