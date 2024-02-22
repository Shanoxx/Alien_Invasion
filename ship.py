import pygame

class Ship:
    """Klasa przeznaczona do zarzadzania sttatkiem kosmicznym."""

    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego i jego polozenie poczatkowe."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Wczytywanie obrazu statku kosmicznego i pobranie jego prostokata.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Kazdy nowy statek kosmiczny pojawia sie na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Wyswietlenie statku kosmicznego w jego aktualnym polozeniu."""
        self.screen.blit(self.image, self.rect)