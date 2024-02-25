class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawien gry."""

    def __init__(self):
        """Inicjalizacja ustawien gry."""
        #Ustawienia ekranu.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230 ,230)
        self.ship_speed = 2.5