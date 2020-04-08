import os
import sys
import pygame


class GameFunc:
    def __init__(self, settings, screen, tank1):
        self.screen = screen
        self.settings = settings
        self.main_rect = pygame.Rect(settings.main_rect)

        self.tank1 = tank1

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        self.screen.fill(self.settings.scoreboard_bg)
        self.screen.fill(self.settings.battlefield_bg, self.main_rect)

        self.map_update()

        self.tank1.update()

        pygame.display.flip()

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
        self.txt_map = []

        with open(path, 'r') as f:
            for line in f:
                self.txt_map.append(list(line))
        # [line.remove(x) for line in self.txt_map for x in range(len(line)) if x == '\n']

        self.bricks = pygame.image.load('data/Models/Blocks/bricks.png').convert_alpha()
        self.bricks = pygame.transform.scale(self.bricks, (self.bricks.get_width() * 4, self.bricks.get_height() * 4))

    def map_update(self):
        y = 0
        for line in self.txt_map:
            x = 0
            for tile in line:
                if tile == '1':
                    self.screen.blit(self.bricks, (x * 64 + 32, y * 64 + 32))
                x += 1
            y += 1
