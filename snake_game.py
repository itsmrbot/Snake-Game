import random
import time
import turtle

DELAY = 0.1  # seconds between moves (smaller = faster snake)
STEP = 20  # how far the snake moves each turn
LIMIT = 280  # how far the snake can go before hitting a wall

score = 0
high_score = 0
segments = []  # the body of the snake (everything behind the head)

# ---------- Screen ----------
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # we update the screen ourselves, which makes it smooth

# ---------- Snake head ----------
head = turtle.Turtle()
head.shape("circle")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ---------- Food ----------
food = turtle.Turtle()
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

# ---------- Score text ----------
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("brown")
pen.goto(0, 260)


def update_score():
    pen.clear()
    pen.write(
        f"Score: {score}   High Score: {high_score}",
        align="center",
        font=("Arial", 18, "normal"),
    )


# ---------- Controls ----------
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    x = head.xcor()
    y = head.ycor()
    if head.direction == "up":
        head.sety(y + STEP)
    elif head.direction == "down":
        head.sety(y - STEP)
    elif head.direction == "left":
        head.setx(x - STEP)
    elif head.direction == "right":
        head.setx(x + STEP)


# ---------- Game helpers ----------
def move_food():
    x = random.randint(-13, 13) * STEP
    y = random.randint(-13, 13) * STEP
    food.goto(x, y)


def add_segment():
    segment = turtle.Turtle()
    segment.shape("circle")
    segment.color("orange")
    segment.penup()
    segments.append(segment)


def move_body():
    # Move each segment to where the one in front of it was.
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # The first segment follows the head.
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())


def hit_wall():
    return abs(head.xcor()) > LIMIT or abs(head.ycor()) > LIMIT


def hit_self():
    for segment in segments:
        if segment.distance(head) < 20:
            return True
    return False


def game_over():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)  # move off screen
    segments.clear()
    score = 0
    update_score()


# ---------- Keyboard ----------
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

update_score()

# ---------- Main game loop ----------
try:
    while True:
        screen.update()

        if hit_wall():
            game_over()

        # Eating food
        if head.distance(food) < 20:
            move_food()
            add_segment()
            score += 10
            if score > high_score:
                high_score = score
            update_score()

        move_body()
        move()

        if hit_self():
            game_over()

        time.sleep(DELAY)
except (turtle.Terminator, turtle.TurtleGraphicsError):
    pass  # the window was closed, so we just stop
