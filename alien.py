from typing import Any
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiajaca pojedynczego obcego we flocie."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Umieszczenie nowego obcego w poblizu lewego gornego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Przechowywanie dokladniego poziomego polozenia obcego.
        self.x = float(self.rect.x)
    
    def update(self):
        """Przesuniecie obcego w prawo"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x


    def check_edges(self):
        """Zwraca wartosc True, jesli obcy znajduje sie przy krawedzie ekranu."""
        screen_rect = self.screen.get_rect()
        return(self.rect.right >= screen_rect.right) or (self.rect.left <=0)
    