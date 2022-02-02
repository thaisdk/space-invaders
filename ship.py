import pygame

class Ship():
    # Espaço nave
    def __init__(self, game_settings, screen):
        # Incializa a espaço nave
        self.screen = screen
        self.game_settings = game_settings
        
        # Carrega a imagem 
        self.image = pygame.image.load('images\ship1.png')
        self.rect = self.image.get_rect()  # Pega o retangulo da imagen
        self.screen_rect = screen.get_rect()  # Pega o retagulo da tela
        
        # Posição
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        
        # Flags de movimento
        self.moving_right = False
        self.moving_left =  False
    
    def update(self):
        #  Atualiza a posição da espaçonave
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
            
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        
        self.rect.centerx = self.center
        
        
    def blitme(self):
        # Desenha a espaço nave
        self.screen.blit(self.image, self.rect)