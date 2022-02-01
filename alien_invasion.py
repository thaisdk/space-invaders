import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Inicializa o jogo
    pygame.init()  # Incializa as configurações de segundo plano
    
    sai_settings = Settings()  # Instancia da classe Settings
    screen = pygame.display.set_mode((sai_settings.screen_width, sai_settings.screen_height)) # Tela
    pygame.display.set_caption("Space Alien Invaders")  # Nome
    
    ship = Ship(screen)  # Instancia da classe Ship
    
    while True:
        gf.check_events()
        gf.update_screen(screen,ship)
            
            
run_game()