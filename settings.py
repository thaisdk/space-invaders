class Settings():
    # Armazena todas as configurações do jogo
    
    def __init__(self):
        # Inicializa as configurações
        self.screen_width = 1366
        self.screen_height = 768
        self.screen_background = (30,30,30)
        
        # Infos da nave
        self.ship_limit = 3
        
        # Infos da bala
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250,250,250
        self.bullets_allowed = 3
        
        # Infos alien
        self.fleet_drop_speed = 10
        
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # direita (1) esquerda (-1)
        self.fleet_direction = 1   

        # Pontuação
        self.alien_points = 50
        
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)