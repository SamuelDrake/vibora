"""Snake, classic arcade game.
Exercises
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.
"""

from turtle import *
from random import randint, randrange
from freegames import square, vector
#Variables de las cosas importantes
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colorsSnake = ['green', 'pink', 'blue', 'purple', 'cyan']
colorsFood = ['black', 'yellow', 'orange', 'red']

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
#Regresa si head está dentro del mapa
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
#Mueve la serpiente
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()#Recupera la cabeza
    head.move(aim)#La mueve hacia la dirección indicada

    if not inside(head) or head in snake:#Checa si se acaba el juego
        square(head.x, head.y, 9, 'red')#Cambia el color de la serpiente
        update()
        return#Finaliza

    snake.append(head)#Agregar una nueva pieza

    if head == food:#Si la cabeza está en la comida
        print('Snake:', len(snake))#Imprime el tamaño de la serpiente
        #Genera nueva comida
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)#Eliminar la nueva pieza agregada

    clear()#Limpiar el canvas

    for body in snake:#Imprimir todo en la serpiente
        square(body.x, body.y, 9, colorsSnake[randrange(len(colorsSnake))])
    movements=[[10,0],[-10,0],[0,10],[0,-10],[0,0]] #Posibles movimientos
    index=randint(0,4)#Seleccionar un movimiento aleatorio
    temp_food=vector(food.x+movements[index][0],food.y+movements[index][1])#Crear una nueva comida con los nuevos valores para comprobar si está en los límites
    if (inside(temp_food)):#Si está dentro del mapa
        #Efectuar cambios
        food.x=food.x+movements[index][0]
        food.y=food.y+movements[index][1]
    square(food.x, food.y, 9, colorsFood[randrange(len(colorsFood))])#Imprimir la comida
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)#Crear ventana
hideturtle()#No mostrar la tortuga en el canvas
#Recibir entradas de teclado
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()#finalizar