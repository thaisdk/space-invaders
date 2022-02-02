import sys, pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Inicializa o jogo
    pygame.init()  # Incializa as configurações de segundo plano
    game_settings = Settings()  # Instancia da classe Settings
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)) # Tela
    pygame.display.set_caption("Space Alien Invaders")  # Nome
    
    ship = Ship(game_settings, screen)  # Instancia da classe Ship
    bullets = Group()
    
    while True:        
        gf.check_events(game_settings, screen, ship, bullets)
        # Espaçonave e projeteis
        ship.update()
        bullets.update()
        
        gf.update_screen(game_settings, screen, ship, bullets)
            
            
run_game() 