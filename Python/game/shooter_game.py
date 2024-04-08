import tkinter as tk
import random

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SHOOTER_RADIUS = 30
ENEMY_MIN_RADIUS = 10
ENEMY_MAX_RADIUS = 40
ENEMY_COLORS = ["red", "green", "blue", "yellow", "purple"]

root = tk.Tk()
root.title("Shooter Game")

canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
canvas.pack()

class Shooter:
    def __init__(self, canvas, x, y, radius, color):
        self.canvas = canvas
        self.id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def shoot(self, target_x, target_y):
        bullet = Bullet(self.canvas, self.x, self.y, target_x, target_y, self.color)

class Bullet:
    def __init__(self, canvas, start_x, start_y, target_x, target_y, color):
        self.canvas = canvas
        self.id = canvas.create_oval(start_x - 5, start_y - 5, start_x + 5, start_y + 5, fill=color)
        self.start_x = start_x
        self.start_y = start_y
        self.target_x = target_x
        self.target_y = target_y
        self.color = color
        self.speed = 5
        self.move()

    def move(self):
        dx = self.target_x - self.start_x
        dy = self.target_y - self.start_y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        steps = int(distance / self.speed)

        for _ in range(steps):
            self.canvas.move(self.id, dx / steps, dy / steps)
            self.canvas.update()
            self.canvas.after(10)


class Enemy:
    def __init__(self, canvas):
        self.canvas = canvas
        self.radius = random.randint(ENEMY_MIN_RADIUS, ENEMY_MAX_RADIUS)
        self.color = random.choice(ENEMY_COLORS)

        spawn_side = random.randint(1, 4)  # 1=top, 2=right, 3=bottom, 4=left
        if spawn_side == 1:
            self.x = random.randint(self.radius, WINDOW_WIDTH - self.radius)
            self.y = -self.radius
        elif spawn_side == 2:
            self.x = WINDOW_WIDTH + self.radius
            self.y = random.randint(self.radius, WINDOW_HEIGHT - self.radius)
        elif spawn_side == 3:
            self.x = random.randint(self.radius, WINDOW_WIDTH - self.radius)
            self.y = WINDOW_HEIGHT + self.radius
        else:
            self.x = -self.radius
            self.y = random.randint(self.radius, WINDOW_HEIGHT - self.radius)

        self.id = canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                     self.x + self.radius, self.y + self.radius, fill=self.color)

def fire_bullet(event):
    shooter.shoot(event.x, event.y)

canvas.bind("<Button-1>", fire_bullet)

def game_loop():
    # Spawn enemies
    if random.random() < 0.05:  # Adjust frequency of enemy spawn
        enemy = Enemy(canvas)

    # Move enemies towards the shooter
    for enemy in canvas.find_all():
        if canvas.gettags(enemy) == ("enemy",):
            x1, y1, x2, y2 = canvas.coords(enemy)
            dx = shooter.x - (x1 + x2) / 2
            dy = shooter.y - (y1 + y2) / 2
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance > shooter.radius + enemy.radius:
                canvas.move(enemy, dx / distance * 2, dy / distance * 2)
            else:
                game_over()
                return

    root.after(30, game_loop)

def game_over():
    canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, text="GAME OVER", fill="white", font=("Arial", 36))

# Create the shooter
shooter = Shooter(canvas, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, SHOOTER_RADIUS, "white")

# Start the game loop
game_loop()

# Start the tkinter main event loop
root.mainloop()
