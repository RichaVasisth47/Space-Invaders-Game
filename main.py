import math
import random
import turtle

# Step 1: Set up the game screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders Game")
wn.tracer(0)

# Step 2: Set up the Scoreboard
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Step 3: Create the Player (Colorful Spaceship)
player = turtle.Turtle()
player.color("cyan")
player.shape("triangle")
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)

player_speed = 15

# Step 4: Create the Enemy Invaders
number_of_enemies = 5
enemies = []

for _ in range(number_of_enemies):
  enemy = turtle.Turtle()
  enemy.color("red")
  enemy.shape("square")
  enemy.penup()
  enemy.speed(0)
  x = random.randint(-200, 200)
  y = random.randint(100, 250)
  enemy.goto(x, y)
  enemies.append(enemy)

enemy_speed = 2

# Step 5: Create the Player's Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 25
bullet_state = "ready"


# Step 6: Define Player Movement Functions
def move_left():
  x = player.xcor()
  x -= player_speed
  if x < -280:
    x = -280
  player.setx(x)


def move_right():
  x = player.xcor()
  x += player_speed
  if x > 280:
    x = 280
  player.setx(x)


def fire_bullet():
  global bullet_state
  if bullet_state == "ready":
    bullet_state = "fire"
    x = player.xcor()
    y = player.ycor() + 10
    bullet.goto(x, y)
    bullet.showturtle()


def is_collision(t1, t2):
  distance = math.sqrt(
      (t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2
  )
  if distance < 20:
    return True
  return False


# Step 7: Keyboard Bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# Flag to track game state
game_running = True

# Step 8: Main Game Loop
while game_running:
  wn.update()

  # Move the enemy
  for enemy in enemies:
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    if enemy.xcor() > 280:
      for e in enemies:
        e.sety(e.ycor() - 30)
      enemy_speed *= -1

    if enemy.xcor() < -280:
      for e in enemies:
        e.sety(e.ycor() - 30)
      enemy_speed *= -1

    # Check for collision between bullet and enemy
    if bullet_state == "fire" and is_collision(bullet, enemy):
      bullet.hideturtle()
      bullet_state = "ready"
      bullet.goto(0, -400)

      x = random.randint(-200, 200)
      y = random.randint(100, 250)
      enemy.goto(x, y)

      score += 10
      score_pen.clear()
      score_pen.write(
          f"Score: {score}", align="center", font=("Courier", 24, "normal")
      )

    # Check for collision between player and enemy (Game Over)
    if is_collision(player, enemy):
      player.hideturtle()
      enemy.hideturtle()
      score_pen.goto(0, 0)
      score_pen.write(
          "GAME OVER", align="center", font=("Courier", 36, "bold")
      )
      game_running = False
      break

  # Move the bullet
  if bullet_state == "fire":
    y = bullet.ycor()
    y += bullet_speed
    bullet.sety(y)

  if bullet.ycor() > 275:
    bullet.hideturtle()
    bullet_state = "ready"

# Keep the window open after game over
turtle.done()

