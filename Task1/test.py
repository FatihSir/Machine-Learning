import unittest
from Task import guess

class TestGuessGame(unittest.TestCase):

    def test_correct_guess_first_try(self):
        result = guess(ran=500, user_inputs=[500])
        self.assertEqual(result, ["Congratulations! You guessed the right number in just ONE try.\nYou are legend!"])

    def test_correct_guess_multiple_tries(self):
        result = guess(ran=500, user_inputs=[300, 700, 500])
        self.assertEqual(result[-1], "Congratulations! You guessed the right number in 3 tries.")

    def test_guess_lower(self):
        result = guess(ran=500, user_inputs=[600])
        self.assertEqual(result, ["Sorry you have to guess lower."])

    def test_guess_higher(self):
        result = guess(ran=500, user_inputs=[400])
        self.assertEqual(result, ["Sorry you have to guess higher."])

    def test_invalid_input(self):
        result = guess(ran=500, user_inputs=[1500])
        self.assertEqual(result, ["Please enter a number between 0 and 1000."])


if __name__ == "__main__":
    unittest.main()