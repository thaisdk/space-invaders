import sys, pygame
from bullet import Bullet

def check_keydown_events(event, game_settings, screen, ship, bullets):                    
    if event.key == pygame.K_RIGHT:
        # Espaçonave para direita.
        ship.moving_right = True
                    
    elif event.key == pygame.K_LEFT:
        # Espaçonave para esquerda.
        ship.moving_left = True
        
    elif event.key == pygame.K_SPACE:
        # Espaçonave atira.
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_eventes(event, ship):
    #  Parar  
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
                        
    elif event.key == pygame.K_LEFT:
        ship.moving_left =  False


def check_events(game_settings, screen, ship, bullets):
    # Eventos pressionando teclas e mouses
    for event in pygame.event.get():  # Event -> ação do usuário
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, 
                                 screen, ship, bullets)
            
        elif event.type == pygame.KEYUP:
            check_keyup_eventes(event, ship)
            
                    
def update_screen(game_settings, screen, ship, bullets):
    # Atualiza as imagens da tela         
    
    screen.fill(game_settings.screen_background)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()   
    pygame.display.flip()
        
    
    
    