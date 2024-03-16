import pygame

class Ship:
    """Klasa przeznaczona do zarzadzania statkiem kosmicznym."""

    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego i jego polozenie poczatkowe."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Wczytywanie obrazu statku kosmicznego i pobranie jego prostokata.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Kazdy nowy statek kosmiczny pojawia sie na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom
        #Polozenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej.
        self.x = float(self.rect.x)

        #Opcje wskazujace na poruszanie sie statku.
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """
        Uaktualnienie polozenia statku na podstawie opcji wskazujacej na jego ruch.
        """
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        #Uaktualnienie wartosci wspolrzednej X statku, a nie jego prostokata.
        if self.moving_right and self.rect.right < self.screen_rect.right:
           self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed 

        #Uaktualnienie obiektu rect na podstawie wartosci self.x.
        self.rect.x = self.x

    def blitme(self):
        """Wyswietlenie statku kosmicznego w jego aktualnym polozeniu."""
        self.screen.blit(self.image, self.rect)