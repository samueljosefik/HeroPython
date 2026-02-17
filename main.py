import pgzrun
import math
import random
from pygame import Rect
from pgzero.actor import Actor 

goal = Actor('goal')

def reset_goal():
    
    goal.x = random.randint(400, 750)
    goal.y = random.randint(50, 550)


screen: any
sounds: any
music: any
keyboard: any

WIDTH = 800
HEIGHT = 600
TITLE = "Python Hero"


MENU, PLAYING, GAME_OVER = 0, 1, 2
game_state = MENU
audio_on = True

class AnimatedEntity:
    
    def __init__(self, images, pos):
        self.images = images
        self.frame = 0
        self.actor = Actor(images[self.frame], pos)
        self.timer = 0
        self.animation_speed = 0.15 

    def update_animation(self, dt):
        
        self.timer += dt
        if self.timer >= self.animation_speed:
            self.timer = 0
            self.frame = (self.frame + 1) % len(self.images)
            self.actor.image = self.images[self.frame]

    def draw(self):
        self.actor.draw()

class Hero(AnimatedEntity):
    def __init__(self, pos):
        
        super().__init__(['hero_idle1', 'hero_idle2', 'hero_idle3'], pos)
        self.target_pos = pos
        self.speed = 4

    def update(self, dt):
        self.update_animation(dt)
        
        if self.actor.distance_to(self.target_pos) > self.speed:
            angle = self.actor.angle_to(self.target_pos)
            self.actor.x += math.cos(math.radians(angle)) * self.speed
            self.actor.y -= math.sin(math.radians(angle)) * self.speed

class Enemy(AnimatedEntity):
    def __init__(self, frames, pos, range_limit):
        super().__init__(frames, pos)
        
        self.start_x = pos[0] 
        self.range_limit = range_limit
        self.direction = 1
        self.speed = random.uniform(1.5, 3.0)

    def patrol(self, dt):
        
        self.update_animation(dt)
        self.actor.x += self.speed * self.direction
        
        
        if abs(self.actor.x - self.start_x) > self.range_limit:
            self.direction *= -1



hero = Hero((100, 500))


enemies = [
    Enemy(['enemy1_frame1', 'enemy1_frame2'], (400, 300), 120),
    Enemy(['enemy2_frame1', 'enemy2_frame2'], (200, 200), 80),
    Enemy(['enemy3_frame1', 'enemy3_frame2'], (600, 450), 100)
]


btn_start = Rect((300, 200), (200, 50))
btn_audio = Rect((300, 300), (200, 50))
btn_exit = Rect((300, 400), (200, 50))

def draw_scenery():
    
    screen.fill((10, 10, 30))
    
    random.seed(10)
    for _ in range(30):
        screen.draw.filled_circle((random.randint(0, 800), random.randint(0, 400)), 1, "white")
    
    screen.draw.filled_rect(Rect(0, 480, 800, 120), (15, 45, 15))
    for x in [100, 300, 500, 700]:
        screen.draw.filled_rect(Rect(x, 440, 15, 40), (40, 20, 10))
        screen.draw.filled_circle((x+7, 430), 25, (5, 60, 5))

def update(dt):
    global game_state
    if game_state == PLAYING:
        hero.update(dt)
        for enemy in enemies:
            enemy.patrol(dt)
            if hero.actor.inflate(-40, -40).colliderect(enemy.actor.inflate(-40, -40)):
                if audio_on:
                    sounds.impact1.play()
                game_state = GAME_OVER
        
        if hero.actor.colliderect(goal):
            game_state = 3  
WIN = 3

def draw():
    screen.clear()
    if game_state == MENU:
        draw_menu()
    elif game_state == PLAYING:
        draw_scenery()
        goal.draw() 
        hero.draw()
        for enemy in enemies: enemy.draw()
    elif game_state == GAME_OVER:
        screen.draw.text("VOCÊ FOI PEGO!", center=(400, 300), fontsize=60, color="red")
    elif game_state == WIN:
        screen.fill((0, 50, 0)) 
        screen.draw.text("VITÓRIA! VOCÊ É UM HERÓI!", center=(400, 300), fontsize=60, color="gold")
        screen.draw.text("Clique para voltar ao menu", center=(400, 380), fontsize=30)


def draw_menu():
    screen.draw.text("Python Hero", center=(400, 100), fontsize=50, color="gold")
    
    screen.draw.filled_rect(btn_start, "darkgreen")
    screen.draw.text("INICIAR", center=btn_start.center, color="white")
    
    color = "blue" if audio_on else "darkred"
    screen.draw.filled_rect(btn_audio, color)
    screen.draw.text(f"SOM: {'ON' if audio_on else 'OFF'}", center=btn_audio.center, color="white")
    
    screen.draw.filled_rect(btn_exit, "gray")
    screen.draw.text("SAIR", center=btn_exit.center, color="white")

def on_mouse_down(pos):
    global game_state, audio_on
    
    if game_state == MENU:
        if btn_start.collidepoint(pos):
            reset_goal()
            game_state = PLAYING
            if audio_on:
                music.play("chasm")
                sounds.notif1.play()
        elif btn_audio.collidepoint(pos):
            audio_on = not audio_on
            if not audio_on: 
                music.stop()
            else: 
                sounds.notif1.play()
        elif btn_exit.collidepoint(pos):
            exit()
            
    elif game_state == PLAYING:
        hero.target_pos = pos
        if audio_on:
            sounds.notif1.play()
            
    elif game_state == GAME_OVER or game_state == WIN:
       
        game_state = MENU
        hero.actor.pos = (100, 500)
        hero.target_pos = (100, 500)
pgzrun.go()
