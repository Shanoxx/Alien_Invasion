import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Klasa przeznaczona do zarzadzania pociskami wystrzeliwanymi przez statek."""

    def __init__(self, ai_game):
        """Utworzenie obiektu pocisku w aktualnum polozeniu statku."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #Utworzenie prostokata pocisku w punkcie (0,0), a nastepnie
        #zdefiniowanie dla niego odpowiedniego polozenia.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Polozenie pocisku zdefiniowane za pomoca wartoscie zmiennoprzecinkowej.
        self.y = float(self.rect.y)

    def update(self):
        """Poruszanie pociskiem po ekranie."""
        self.y -= self.settings.bullet_speed
        #Uaktualnienie polozenia prostokata pocisku.
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyswietlenie pocisku na ekranie."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        