import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, pos, block, screen):
        super().__init__()
        self.pos = pos
        self.block = block
        self.screen = screen

        if block == '1':
            self.image = pygame.image.load('data/Models/Blocks/bricks.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (16 * 4, 16 * 4))

        self.rect = pygame.Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())

    def update(self):
        self.screen.blit(self.image, self.rect)
