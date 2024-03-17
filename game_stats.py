
class GameStats:
    """Monitorowanie danych statystycznych w grze "Inwazja obcych". """
    def __init__(self, ai_game):
        """Inicjalizacja danych statystycznych."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, ktore moga zmieniac sie w trakcie gry."""
        self.ships_left = self.settings.ship_limit
        self.score = 0