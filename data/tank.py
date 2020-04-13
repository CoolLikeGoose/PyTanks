import pygame
import data.game_func as gff


class Tank(pygame.sprite.Sprite):
    def __init__(self, who, settings, screen, bullets):
        super().__init__()
        self.settings = settings
        self.screen = screen

        self.animation = gff.GameFunc.load_anim(who)

        self.now_img = self.animation[0]
        self.rect = self.now_img.get_rect()
        self.rect.y += 600
        self.rect.x += 400

        self.counter = 0
        self.frame = 0

        self.move = (0, None)
        self.rot = 0
        self.rotated_img = self.now_img
        self.bumped = False
        self.bullets = bullets

    def update(self):
        self.update_frame()
        self.move_pos(pygame.key.get_pressed())
        # if self.bumped:
        #     self.bump_block()
        self.screen.blit(self.rotated_img, self.rect)

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
            self.rect.y -= self.settings.speed
            self.img_rotation(0)
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.settings.speed
            self.img_rotation(180)
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.settings.speed
            self.img_rotation(270)
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.settings.speed
            self.img_rotation(90)
        elif keys[pygame.K_SPACE]:
            gff.GameFunc.fire_bullet(self)

    def img_rotation(self, deg):
        self.rotated_img = pygame.transform.rotate(self.now_img, deg)
        self.rot = deg

        if self.rect.top < self.settings.main_rect.top:
            self.rect.top = self.settings.main_rect.top
        elif self.rect.bottom > self.settings.main_rect.bottom:
            self.rect.bottom = self.settings.main_rect.bottom
        if self.rect.right > self.settings.main_rect.right:
            self.rect.right = self.settings.main_rect.right
        elif self.rect.left < self.settings.main_rect.left:
            self.rect.left = self.settings.main_rect.left

    def bump_block(self):
        if self.rot == 0:
            self.rect.y += self.settings.speed
        elif self.rot == 90:
            self.rect.x += self.settings.speed
        elif self.rot == 270:
            self.rect.x -= self.settings.speed
        elif self.rot == 180:
            self.rect.y -= self.settings.speed
