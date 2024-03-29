# File created by: Ivan Vikingstad
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
#
# Sources: https://cactusturtle.itch.io/bouncing-blue-blob?download
# Sources: https://stackoverflow.com/questions/50457855/transparent-image-in-pygame
# Sources: https://stackoverflow.com/questions/53442856/add-a-stopwatch-to-a-game-in-pygame
# Sources: 


# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
from os import path
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)

        self.font=pg.freetype.SysFont(None, 34)
        self.font.origin=True

        self.clock_running = True

        # to add images sounds etc copy below...
        # still working on how to get an image to replace the normal controlled square sprite
    def load_data(self):
        self.player_img = pg.image.load(path.join(img_folder, "blob.png")).convert()
        
    def new(self):
        # starts a new game
        self.score = 0
        self.load_data()
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)

        self.platforms.add(self.plat1)
        
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()

       # self.screen.fill(pg.Color('grey12'))


        hits_enemies = pg.sprite.spritecollide(self.player, self.enemies, False)
        if hits_enemies:
            print("hit enemy")
            self.clock_running = False

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                #print("hit!!!!!")
                
                if hits[0].variant == "disappearing":
                    #print("disappearing")
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    #print("bouncey")
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    #print("else")
                    #print(hits)
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # is this a method or a function?
        
        if self.clock_running == True:
            self.last_tick = pg.time.get_ticks()
            
        ticks=self.last_tick
        millis=ticks%1000
        seconds=int(ticks/1000 % 60)
        minutes=int(ticks/60000 % 24)
        out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        self.font.render_to(self.screen, (50, 50), out, pg.Color(WHITE))
        #pg.display.flip()
        # self.clock.tick(60)

        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()