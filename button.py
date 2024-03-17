import pygame.font

class Button:
    """Klasa przeznaczona do tworzenia przyciskow dla gry."""

    def __init__(self, ai_game, msg):
        """Inicjalizacja atrybutow przyciskow"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Zdefiniowanie wymiarow i wlasciwosci przycisku.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Utworzenie prostokata przycisku i wysrodkowanie go.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Komunikat wyswietlany przez przycisk trzeba przygotowac tylko jednokrotnie.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Umieszczenie komunikatu w wygenerowanym obrazie i wysrodkowanie tekstu na przycisku."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Wyswietlenie pustego przycisku , a nastepnie komunikatu na nim
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)