import pygame
import pgzero
import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
timer_seconds = 20  # initial seconds
timer_milliseconds = 0  

fox = Actor("fox")
fox.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200
restart_button = Rect(WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 40)


def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    timer_display = "{:02}".format(timer_seconds)
    screen.draw.text("Time left :  " + timer_display + " Seconds ", color="black", topright=(WIDTH - 10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), color="black", topleft=(10, 10))
        if score >= 100: #define qualifying score here
            screen.draw.text("Winner!", color="black", midtop=(WIDTH // 2, HEIGHT // 2 + 30))
        else:
            screen.draw.text("Try Again!  Score 100 in 20 Seconds!!", color="black", midtop=(WIDTH // 2, HEIGHT // 2 + 30))
            


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))


def time_up():
    global game_over
    game_over = True


def update():
    global score, timer_seconds, timer_milliseconds, game_over

    if not game_over:
        if timer_milliseconds > 0:
            timer_milliseconds -= 1
        else:
            if timer_seconds > 0:
                timer_seconds -= 1
                timer_milliseconds = 59
            else:
                time_up()

        if keyboard.left:
            fox.x = max(fox.x - 2, 0)
        elif keyboard.right:
            fox.x = min(fox.x + 2, WIDTH - fox.width)
        elif keyboard.up:
            fox.y = max(fox.y - 2, 0)
        elif keyboard.down:
            fox.y = min(fox.y + 2, HEIGHT - fox.height)

        coin_collected = fox.colliderect(coin)
        if coin_collected:
            score += 10
            place_coin()


# Set a timer event to end the game after 1 minute
clock.schedule(time_up, 60.0)
place_coin()

pgzrun.go()
