from pydoc import plain
import sys, pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Inicializa o jogo
    pygame.init()  # Incializa as configurações de segundo plano
    game_settings = Settings()  # Instancia da classe Settings
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)) # Tela
    pygame.display.set_caption("Space Alien Invaders")  # Nome

    play_button = Button(game_settings, screen, "Play")
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, screen, stats)
    
    ship = Ship(game_settings, screen)  # Instancia da classe Ship
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(game_settings, screen, ship, aliens)
    
    while True:        
        gf.check_events(game_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        # Espaçonave e projeteis
        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(game_settings, screen, stats,sb, ship, aliens, bullets)
        
        gf.update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, play_button)
            
            
run_game() 