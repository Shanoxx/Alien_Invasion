import sys 

import pygame

class AlienInvasion:
    "Ogolna klasa przeznaczona do zarzadzania zasobami i sposobem dzialania gry."

    def __init__(self):
        "Inicjalizacja gry i utworzenie jej zasobow"
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Inwazja Obcych")

        #Zdefiniowanie koloru tla.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        "Rozpoczecie petli glownej gry"
        while True:
            #Oczekiwanie na nacisniecie klawisza lub przycisku myszt.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Odswiezanie ekranu w trakcie kazdej iteracji petli.
            self.screen.fill(self.bg_color)

            #Wyswietlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    #Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()

