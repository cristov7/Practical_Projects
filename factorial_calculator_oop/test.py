from factorial_calculator_oop.factorial_calculator import FactorialCalculator
import unittest


class FactorialCalculatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.factorial_calculator = FactorialCalculator(5)

    def test___init___successfully(self):
        assert self.factorial_calculator.number == 5
        assert isinstance(self.factorial_calculator.number, int)

        assert self.factorial_calculator.factorial_of_number is None

    def test_set_number_successfully(self):
        self.factorial_calculator.number = 7

        assert self.factorial_calculator.number == 7
        assert isinstance(self.factorial_calculator.number, int)

    def test_set_number_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.factorial_calculator.number = "7"
        assert str(content.exception) == "The number must be an integer!"

        assert self.factorial_calculator.number == 5
        assert isinstance(self.factorial_calculator.number, int)

    def test_calculate_factorial_of_number_successfully(self):
        self.factorial_calculator.calculate_factorial_of_number()

        assert self.factorial_calculator.factorial_of_number == 120
        assert isinstance(self.factorial_calculator.factorial_of_number, int)

    def test___repr___with_set_factorial_of_number_successfully(self):
        self.factorial_calculator.number = 0
        assert self.factorial_calculator.number == 0
        assert isinstance(self.factorial_calculator.number, int)
        self.factorial_calculator.calculate_factorial_of_number()

        assert self.factorial_calculator.__repr__() == "Factorial function:" \
                                                       "\n0! = 1" \
                                                       "\nResult: 1"
        assert isinstance(self.factorial_calculator.__repr__(), str)

        self.factorial_calculator.number = 1
        self.factorial_calculator.calculate_factorial_of_number()

        assert self.factorial_calculator.__repr__() == "Factorial function:" \
                                                       "\n1! = 1" \
                                                       "\nResult: 1"
        assert isinstance(self.factorial_calculator.__repr__(), str)

        self.factorial_calculator.number = 10
        self.factorial_calculator.calculate_factorial_of_number()

        assert self.factorial_calculator.__repr__() == "Factorial function:" \
                                                       "\n10! = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3628800" \
                                                       "\nResult: 3628800"
        assert isinstance(self.factorial_calculator.__repr__(), str)

    def test___repr___without_set_factorial_of_number_successfully(self):
        assert self.factorial_calculator.__repr__() == "First you have to calculate factorial of number!"
        assert isinstance(self.factorial_calculator.__repr__(), str)


if __name__ == '__main__':
    unittest.main()
