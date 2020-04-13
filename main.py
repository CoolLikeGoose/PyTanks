import pygame

from data.settings import Settings
from data.game_func import GameFunc


def run_game():
    pygame.init()
    settings = Settings()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(settings.screen_sizes)
    pygame.display.set_caption('PyTanks')

    gf = GameFunc(settings, screen)
    gf.map_reader_txt()

    while True:
        gf.check_events()
        gf.update_screen()

        clock.tick(settings.FPS)


if __name__ == '__main__':
    run_game()
