import pygame

class Alien(pygame.sprite.Sprite):
    # Classe que representa um único alienígena
    def __init__(self, game_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        
        # Carrega a imagem
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def update(self):
        # Move o alienigena para direita ou para esquerda
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x
    
    def blitme(self):
        # Desenha o alien
        self.screen.blit(self.image, self.rect)