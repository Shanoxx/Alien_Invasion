class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawien gry."""

    def __init__(self):
        """Inicjalizacja ustawien gry."""
        #Ustawienia ekranu.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230 ,230)
        self.ship_speed = 2.5
        #Ustawienia dotyczace pocisku
        self.bullet_speed = 50.0
        self.bullet_width = 20
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        #Ustawienia dotyczace obcego
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #Wartosc fleet_direction wynoszaca 1 oznacza prawo, natomiast -1 lewo.
        self.fleet_direction = 1