from platform import python_branch
import pygame

class Ship():
    # Espaço nave
    def __init__(self, screen):
        # Incializa a espaço nave
        self.screen = screen
        self.image = pygame.image.load('images\ship1.png')
        
        self.rect = self.image.get_rect()  # Pega o retangulo da imagen
        self.screen_rect = screen.get_rect()  # Pega o retagulo da tela
        
        # Posição
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        # Desenha a espaço nave
        self.screen.blit(self.image, self.rect)