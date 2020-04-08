import pygame
from data.game_func import GameFunc as GF


class Tank:
    def __init__(self, who, settings, screen):
        self.settings = settings
        self.screen = screen

        self.animation = GF.load_anim(who)

        self.now_img = self.animation[0]
        self.img_rect = self.now_img.get_rect()
        self.img_rect.y += 600
        self.img_rect.x += 400

        self.counter = 0
        self.frame = 0

        self.move = (0, None)
        self.rot = None
        self.rotated_img = self.now_img

    def update(self):
        self.update_frame()
        self.move_pos(pygame.key.get_pressed())
        self.screen.blit(self.rotated_img, self.img_rect)

    def update_frame(self):
        if self.counter == self.settings.anim_frame:
            self.counter = 0
            self.frame += 1
        if self.frame == len(self.animation):
            self.frame = 0
        self.now_img = self.animation[self.frame]
        self.counter += 1

    def move_pos(self, keys):
        if keys[pygame.K_UP]:
            self.img_rect.y -= self.settings.speed
            self.img_rotation(0)
        elif keys[pygame.K_DOWN]:
            self.img_rect.y += self.settings.speed
            self.img_rotation(180)
        elif keys[pygame.K_RIGHT]:
            self.img_rect.x += self.settings.speed
            self.img_rotation(270)
        elif keys[pygame.K_LEFT]:
            self.img_rect.x -= self.settings.speed
            self.img_rotation(90)

    def img_rotation(self, deg):
        self.rotated_img = pygame.transform.rotate(self.now_img, deg)

        if self.img_rect.top < self.settings.main_rect.top:
            self.img_rect.top = self.settings.main_rect.top
        elif self.img_rect.bottom > self.settings.main_rect.bottom:
            self.img_rect.bottom = self.settings.main_rect.bottom
        if self.img_rect.right > self.settings.main_rect.right:
            self.img_rect.right = self.settings.main_rect.right
        elif self.img_rect.left < self.settings.main_rect.left:
            self.img_rect.left = self.settings.main_rect.left
