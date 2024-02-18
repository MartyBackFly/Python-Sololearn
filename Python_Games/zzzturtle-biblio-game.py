import turtle
import random

# Configuración de la pantalla
wn = turtle.Screen()
wn.title("Juego Simple en Python")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Jugador
jugador = turtle.Turtle()
jugador.shape("square")
jugador.color("blue")
jugador.speed(100)
jugador.penup()
jugador.goto(0, -250)

# Enemigo
enemigo = turtle.Turtle()
enemigo.shape("circle")
enemigo.color("red")
enemigo.speed(200)
enemigo.penup()
enemigo.goto(random.randint(-290, 290), 250)

# Funciones
def mover_derecha():
    x = jugador.xcor()
    x += 20
    jugador.setx(x)

def mover_izquierda():
    x = jugador.xcor()
    x -= 20
    jugador.setx(x)

# Teclado
wn.listen()
wn.onkeypress(mover_derecha, "Right")
wn.onkeypress(mover_izquierda, "Left")

# Bucle principal del juego
while True:
    # Movimiento del enemigo
    y = enemigo.ycor()
    y -= 1
    enemigo.sety(y)

    # Verificar colisión
    if jugador.distance(enemigo) < 20:
        print("¡Has perdido!")
        break

    # Verificar límites de la pantalla para el enemigo
    if enemigo.ycor() < -290:
        enemigo.goto(random.randint(-290, 290), 250)

# Cierre de la ventana al hacer clic en ella
wn.mainloop()
