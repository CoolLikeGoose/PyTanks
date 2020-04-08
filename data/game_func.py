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
                # elif event.type == pygame.KEYDOWN:
            #     self.check_keydown(event)
            # elif event.type == pygame.KEYUP:
            #     self.check_keyup(event)

    # def check_keydown(self, event):
    #     if event.key == pygame.K_LEFT:
    #         self.tank1.move = (-1, 'X')
    #     elif event.key == pygame.K_RIGHT:
    #         self.tank1.move = (1, 'X')
    #     elif event.key == pygame.K_DOWN:
    #         self.tank1.move = (1, 'Y')
    #     elif event.key == pygame.K_UP:
    #         self.tank1.move = (-1, 'Y')
    #
    # def check_keyup(self, event):
    #     if event.key == pygame.K_LEFT:
    #         self.tank1.move = (0, None)
    #     elif event.key == pygame.K_RIGHT:
    #         self.tank1.move = (0, None)
    #     elif event.key == pygame.K_DOWN:
    #         self.tank1.move = (0, None)
    #     elif event.key == pygame.K_UP:
    #         self.tank1.move = (0, None)

    def update_screen(self):
        self.screen.fill(self.settings.scoreboard_bg)
        self.screen.fill(self.settings.battlefield_bg, self.main_rect)

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
        pass
