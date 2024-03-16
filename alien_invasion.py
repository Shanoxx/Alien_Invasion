import sys 
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        "Rozpoczecie petli glownej gry"
        while True:     
            self._chceck_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()     
            self.clock.tick(60)
            self._check_bullet_alien_collisions()

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
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pociskow."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    

    def _update_bullets(self):
        """Uaktualnienie polozenia pociskow i usuniecie tych niewidocznych na ekranie."""
        self.bullets.update()
        #Usuniecie pociskow ktore znajduja sie poza ekranem.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self):
        #Sprawdzenie, czy ktorykolwiek pocisk trafil obcego.
        #Jezeli tak, usuwamy zarowno pocisk, jak i obcego.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            #Pozbycie sie istniejacych pociskow i utworzenie nowej floty.
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Prawdzenie, czy flota obcych znajduje sie przy krawedzi, Uaktualnienie polozenia wszystkich obcych we flocie."""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Utworzenie pelnej floty obcych."""
        #Utworzenie obcego
        #Odleglosc miedzy poszczegolnymi obcymi jest rowna szerokosci obcego.

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

                #Ukonczenie rzedu, wyzerowanie wartosci x oraz inkrementacja wartosci y.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Utworzenie obcego i umieszczenie go w rzedzie."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Odpowiednia reakcja, gdy obcy dotrze do krawedzi ekranu."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Przesuniecie calej flotyy w dol i zmiana, kierunku w ktorym sie ona porusza."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        #Odswiezanie ekranu w trakcie kazdej iteracji petli.
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)

            #Wyswietlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()

if __name__ == '__main__':
    #Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()


