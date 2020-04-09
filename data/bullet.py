import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, settings, tank, facing):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.tank = tank
        self.facing = facing

        self.image = pygame.image.load('data/Models/Effects/bullet.png').convert_alpha()
        pygame.transform.scale(self.image, (self.image.get_width() * settings.multiply_size,
                                            self.image.get_height() * settings.multiply_size))
        self.image = pygame.transform.rotate(self.image, self.tank.rot)

        self.rect = self.image.get_rect()
        self.rect.centerx = self.tank.rect.centerx
        self.rect.bottom = self.tank.rect.top

        self.main_coord = (0, -self.settings.speed)
        self.check_main_coord()

    def check_main_coord(self):
        if self.tank.rot == 0:
            self.main_coord = (0, -self.settings.speed)
        elif self.tank.rot == 90:
            self.main_coord = (-self.settings.speed, 0)
        elif self.tank.rot == 180:
            self.main_coord = (0, self.settings.speed)
        elif self.tank.rot == 270:
            self.main_coord = (self.settings.speed, 0)

    def update(self):
        self.screen.blit(self.image, self.rect)
        self.rect = self.rect.move(self.main_coord[0], self.main_coord[1])
        print(self.main_coord)
        print(self.rect.x, self.rect.y)
