import os
import sys
import pygame

from data.block import Block
from data.tank import Tank
from data.bullet import Bullet


class GameFunc:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.main_rect = pygame.Rect(settings.main_rect)

        self.blocks = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.tank1 = Tank('p1', settings, screen, self.bullets)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        self.screen.fill(self.settings.scoreboard_bg)
        self.screen.fill(self.settings.battlefield_bg, self.main_rect)

        self.blocks.update()
        self.check_collide_tb()
        self.tank1.update()

        pygame.display.flip()

    def load_tank(self):
        pass

    @staticmethod
    def load_anim(who):
        animation = []
        animation_scaled = []
        up = 4

        if who == 'p1':
            path = 'data/Models/Players/Player_1'

        for file in os.listdir(path):
            animation.append(pygame.image.load(path + '/' + file).convert_alpha())

        for anim in animation:
            animation_scaled.append(pygame.transform.scale(anim, (anim.get_width() * up, anim.get_height() * up)))
        return animation_scaled

    def map_reader_txt(self):
        path = 'data/Maps/level_1.goose'
        txt_map = []

        with open(path, 'r') as f:
            for line in f:
                txt_map.append(list(line))

        y = 0
        for line in txt_map:
            x = 0
            for tile in line:
                if tile is '1':
                    block = Block((x * 64 + 32, y * 64 + 32), tile, self.screen)
                    self.blocks.add(block)
                x += 1
            y += 1

    def check_collide_tb(self):
        collide = pygame.sprite.spritecollideany(self.tank1, self.blocks)
        if collide:
            if type(collide) == Block:
                # self.tank1.bumped = True
                self.tank1.bump_block()  # TODO: fix this shit
        # else:
        # self.tank1.bumped = False

    @staticmethod
    def fire_bullet(self):
        bullet = Bullet(self.screen, self.settings, self, self.rot)
        self.bullets.add(bullet)
