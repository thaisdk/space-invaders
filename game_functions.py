import sys
import pygame

def check_events():
    # Eventos pressionando teclas e mouses
    for event in pygame.event.get():  # Event -> ação do usuário
                if event.type == pygame.QUIT:
                    sys.exit()
                    
def update_screen(screen, ship):
    # Atualiza as imagens da tela
    ship.blitme()
    pygame.display.flip()