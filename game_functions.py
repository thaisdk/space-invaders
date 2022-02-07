import sys, pygame

from time import sleep
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, game_settings, screen, ship, bullets):                    
    if event.key == pygame.K_RIGHT:
        # Espaçonave para direita.
        ship.moving_right = True                
    elif event.key == pygame.K_LEFT:
        # Espaçonave para esquerda.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Atirar
        fire_bullets(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    #  Parar  
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
                        
    elif event.key == pygame.K_LEFT:
        ship.moving_left =  False


def check_events(game_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    # Eventos pressionando teclas e mouses
    for event in pygame.event.get():  # Event -> ação do usuário
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats,sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, 
                                 screen, ship, bullets)   
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def check_play_button(game_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        game_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()       
        stats.game_active = True 
        sb.prep_score()
        sb.prep_high_score()  
        sb.prep_level()  
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()
        
def check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets):          
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += game_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        game_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(game_settings, screen, ship, aliens)
        
def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
    

def update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # Atualiza as imagens da tela         
    
    screen.fill(game_settings.screen_background)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen) 
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets):
    # Atualiza a posição dos projeteis
    bullets.update()
    # Apaga os projeteis antigos para não consumir memoria.
    
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets)
    
def update_aliens(game_settings,screen, stats,sb, ship, aliens, bullets):
    # Atualiza a posição
    check_fleet_edges(game_settings, aliens)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, screen, stats,sb, ship, aliens, bullets)
    aliens.update()
    check_aliens_bottom(game_settings, screen, stats, sb, ship, aliens, bullets)
    
def ship_hit(game_settings, screen, stats,sb, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

        
def check_aliens_bottom(game_settings, screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, screen, stats,sb , ship, aliens, bullets)
            break

def check_fleet_edges(game_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    # Faz a frota descer e mudar de direção
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1
        

def fire_bullets(game_settings, screen, ship, bullets):
    # Cria um novo projétil e adiciona ao grupo de projeteis
    if len(bullets) < game_settings.bullets_allowed:
        # Dispara apenas quando o limite não foi atingido
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)



    
def get_number_aliens_x(game_settings, alien_width):
    avaliable_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    
    return number_aliens_x


def get_number_rows(game_settings,ship_height, alien_height ):
    avaliable_space_y = (game_settings.screen_height - 
                         (3 * alien_height) - ship_height)
    number_rows = int(avaliable_space_y / (3 * alien_height))
    
    return number_rows


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

    
def create_fleet(game_settings, screen,ship, aliens):
    # Cria uma frota de alienígenas
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, 
                                  alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, 
                         row_number)



        
