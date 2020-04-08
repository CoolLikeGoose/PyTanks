import pygame


class Settings:
    def __init__(self):
        self.screen_sizes = (1280, 960)
        self.main_rect = pygame.Rect(32, 32, 1024, 896)
        self.multiply_size = 4
        self.FPS = 60
        self.anim_frame = 6

        self.scoreboard_bg = (100, 100, 100)
        self.battlefield_bg = (0, 0, 0)

        self.speed = 4

        self.is_dev_mode = False
        if self.dev_mode: self.dev_mode()

    def dev_mode(self):
        pass
