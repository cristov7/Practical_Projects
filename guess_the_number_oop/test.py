from guess_the_number_oop.guess_the_number import Game
import unittest


class GameTests(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game()
        self.game_2 = Game(5)

    def test___init___successfully(self):
        assert self.game.max_attempts == 3
        assert isinstance(self.game.max_attempts, int)

        assert self.game_2.max_attempts == 5
        assert isinstance(self.game_2.max_attempts, int)

        assert self.game.attempts == 0
        assert isinstance(self.game.attempts, int)

        assert self.game.won is False
        assert isinstance(self.game.won, bool)

    def test_guess_and_the_number_is_lower_successfully(self):
        self.game.number = 5
        assert isinstance(self.game.number, int)

        self.game.guess(10)

        assert self.game.attempts == 1
        assert isinstance(self.game.attempts, int)

    def test_guess_and_the_number_is_higher_successfully(self):
        self.game.number = 5

        self.game.guess(1)
        self.game.guess(2)

        assert self.game.attempts == 2

    def test_guess_and_you_won_successfully(self):
        self.game.number = 5

        self.game.guess(5)

        assert self.game.attempts == 1

        assert self.game.won is True
        assert isinstance(self.game.won, bool)

    def test_guess_and_you_lost_successfully(self):
        self.game.number = 5

        self.game.guess(1)
        self.game.guess(2)
        self.game.guess(3)

        assert self.game.attempts == 3
        assert self.game.won is False


if __name__ == "__main__":
    unittest.main()
