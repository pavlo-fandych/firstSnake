import turtle

# Налаштування вікна
screen = turtle.Screen()
screen.bgcolor("white")

# Створення черепашки
pen = turtle.Turtle()
pen.speed(5)  # Швидкість малювання

# Функція для малювання кола
def draw_circle(color, radius, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.color(color)
    pen.circle(radius)
    pen.end_fill()

# Малювання тіла єдинорога
draw_circle("lightblue", 100, 0, -100)

# Малювання голови єдинорога
draw_circle("lightpink", 50, 0, 50)

# Малювання ока єдинорога
draw_circle("black", 10, 15, 100)

# Малювання рогу
pen.penup()
pen.goto(-20, 120)
pen.pendown()
pen.color("gold")
pen.begin_fill()
pen.left(30)
pen.forward(50)
pen.left(120)
pen.forward(50)
pen.left(120)
pen.forward(50)
pen.end_fill()

# Малювання ноги
pen.penup()
pen.goto(-40, -100)
pen.pendown()
pen.begin_fill()
pen.color("lightblue")
pen.left(90)
pen.forward(50)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(50)
pen.end_fill()

pen.penup()
pen.goto(40, -100)
pen.pendown()
pen.begin_fill()
pen.color("lightblue")
pen.left(90)
pen.forward(50)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(50)
pen.end_fill()

# Малювання хвоста
pen.penup()
pen.goto(-90, -50)
pen.pendown()
pen.color("purple")
pen.begin_fill()
pen.circle(40, 180)
pen.end_fill()

# Завершення малювання
pen.hideturtle()
turtle.done()
