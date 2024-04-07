import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Bouncing Game")

# Set the size of the canvas
canvas_width = 600
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 50, 50, fill=color)
        self.canvas.move(self.id, 300, 200)  # Initial position
        self.x_speed = 4
        self.y_speed = -4

    def move(self):
        self.canvas.move(self.id, self.x_speed, self.y_speed)
        pos = self.canvas.coords(self.id)  # Get current position of the ball
        if pos[1] <= 0 or pos[3] >= canvas_height:
            self.y_speed *= -1  # Reverse vertical direction if hitting top or bottom
        if pos[0] <= 0 or pos[2] >= canvas_width:
            self.x_speed *= -1  # Reverse horizontal direction if hitting left or right

def game_loop():
    ball.move()  # Move the ball
    root.after(30, game_loop)  # Repeat after 30 milliseconds

# Create ball object
ball = Ball(canvas, "red")

# Start the game loop
game_loop()

# Start the tkinter main event loop
root.mainloop()

