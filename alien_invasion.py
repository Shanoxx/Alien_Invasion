import sys 
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    "Ogolna klasa przeznaczona do zarzadzania zasobami i sposobem dzialania gry."

    def __init__(self):
        "Inicjalizacja gry i utworzenie jej zasobow"
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Inwazja Obcych")
        self.ship = Ship(self)

    def run_game(self):
        "Rozpoczecie petli glownej gry"
        while True:     
            self._chceck_events()
            self.ship.update()
            self._update_screen()     
            self.clock.tick(60)

    def _chceck_events(self):
        #Oczekiwanie na nacisniecie klawisza lub przycisku myszt.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reakcja na nacisniecie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key ==pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _update_screen(self):
        #Odswiezanie ekranu w trakcie kazdej iteracji petli.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #Wyswietlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()

if __name__ == '__main__':
    #Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()


