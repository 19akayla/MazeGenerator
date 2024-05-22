import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Maze Generator")
screen.bgcolor("white")

# Set up maze parameters
rows = 20
cols = 20
cell_size = 20
maze = [[0 for _ in range(cols)] for _ in range(rows)]

# Function to draw a rectangle at given position
def draw_rectangle(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(cell_size)
        turtle.right(90)
    turtle.fillcolor(color)
    turtle.end_fill()

# Function to generate maze
def generate_maze():
    for row in range(rows):
        for col in range(cols):
            if random.random() > 0.6:
                maze[row][col] = 1

# Function to draw maze
def draw_maze():
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == 1:
                draw_rectangle(col * cell_size - (cols * cell_size) / 2, (rows * cell_size) / 2 - row * cell_size, "black")

# Main function
def main():
    turtle.speed(0)
    turtle.hideturtle()
    generate_maze()
    draw_maze()
    turtle.done()

if __name__ == "__main__":
    main()
