class Settings():
    # Armazena todas as configurações do jogo
    
    def __init__(self):
        # Inicializa as configurações
        self.screen_width = 600
        self.screen_height = 600
        self.screen_background = (30,30,30)
        
        # Infos da nave
        self.ship_speed_factor = 1.5
        
        # Infos da bala
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250,250,250