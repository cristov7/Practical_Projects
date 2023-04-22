from online_calculator_oop.online_calculator import OnlineCalculator
import unittest


class OnlineCalculatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.online_calculator = OnlineCalculator("+", 12.5, 7.5)

    def test_valid_operators_dict_successfully(self):
        assert self.online_calculator.VALID_OPERATORS_LIST == ["+", "-", "*", "/"]
        assert isinstance(self.online_calculator.VALID_OPERATORS_LIST, list)

    def test___init___successfully(self):
        assert self.online_calculator.operator == "+"
        assert isinstance(self.online_calculator.operator, str)

        assert self.online_calculator.first_number == 12.5
        assert isinstance(self.online_calculator.first_number, float)

        assert self.online_calculator.second_number == 7.5
        assert isinstance(self.online_calculator.second_number, float)

        assert self.online_calculator.result is None

    def test_set_operator_successfully(self):
        self.online_calculator.operator = "*"
        assert self.online_calculator.operator == "*"
        assert isinstance(self.online_calculator.operator, str)

    def test_set_operator_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.online_calculator.operator = "plus"
        assert str(content.exception) == "Invalid operator. Try again..."

        assert self.online_calculator.operator == "+"
        assert isinstance(self.online_calculator.operator, str)

    def test_set_first_number_successfully(self):
        self.online_calculator.first_number = 10
        assert self.online_calculator.first_number == 10
        assert isinstance(self.online_calculator.first_number, int)

        self.online_calculator.first_number = 99.99
        assert self.online_calculator.first_number == 99.99
        assert isinstance(self.online_calculator.first_number, float)

    def test_set_first_number_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.online_calculator.first_number = "1"
        assert str(content.exception) == "Invalid number. Try again..."

        assert self.online_calculator.first_number == 12.5
        assert isinstance(self.online_calculator.first_number, float)

    def test_set_second_number_and_raise_zero_division_error(self):
        self.online_calculator.operator = "/"
        assert self.online_calculator.operator == "/"
        assert isinstance(self.online_calculator.operator, str)

        with self.assertRaises(ZeroDivisionError) as content:
            self.online_calculator.second_number = 0
        assert str(content.exception) == "Invalid operation! Can't divide by zero!"

        assert self.online_calculator.second_number == 7.5
        assert isinstance(self.online_calculator.second_number, float)

    def test_set_second_number_successfully(self):
        self.online_calculator.second_number = 10
        assert self.online_calculator.second_number == 10
        assert isinstance(self.online_calculator.second_number, int)

        self.online_calculator.second_number = 99.99
        assert self.online_calculator.second_number == 99.99
        assert isinstance(self.online_calculator.second_number, float)

    def test_set_second_number_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.online_calculator.second_number = "100"
        assert str(content.exception) == "Invalid number. Try again..."

        assert self.online_calculator.second_number == 7.5
        assert isinstance(self.online_calculator.second_number, float)

    def test___add_successfully(self):   # private method
        assert self.online_calculator._OnlineCalculator__add() == 20.0
        assert isinstance(self.online_calculator._OnlineCalculator__add(), float)

    def test___subtract_successfully(self):   # private method
        assert self.online_calculator._OnlineCalculator__subtract() == 5.0
        assert isinstance(self.online_calculator._OnlineCalculator__add(), float)

    def test___multiply_successfully(self):   # private method
        assert self.online_calculator._OnlineCalculator__multiply() == 93.75
        assert isinstance(self.online_calculator._OnlineCalculator__add(), float)

    def test___divide_successfully(self):   # private method
        assert self.online_calculator._OnlineCalculator__divide() == 1.66666666666666666
        assert isinstance(self.online_calculator._OnlineCalculator__add(), float)

    def test_calculating_with_add_successfully(self):
        self.online_calculator.calculating()

        assert self.online_calculator.result == 20.0
        assert isinstance(self.online_calculator.result, float)

    def test_calculating_with_subtract_successfully(self):
        self.online_calculator.operator = "-"
        assert self.online_calculator.operator == "-"
        assert isinstance(self.online_calculator.operator, str)

        self.online_calculator.calculating()

        assert self.online_calculator.result == 5.0
        assert isinstance(self.online_calculator.result, float)

    def test_calculating_with_multiply_successfully(self):
        self.online_calculator.operator = "*"
        assert self.online_calculator.operator == "*"
        assert isinstance(self.online_calculator.operator, str)

        self.online_calculator.calculating()

        assert self.online_calculator.result == 93.75
        assert isinstance(self.online_calculator.result, float)

    def test_calculating_with_divide_successfully(self):
        self.online_calculator.operator = "/"
        assert self.online_calculator.operator == "/"
        assert isinstance(self.online_calculator.operator, str)

        self.online_calculator.calculating()

        assert self.online_calculator.result == 1.66666666666666666
        assert isinstance(self.online_calculator.result, float)

    def test___repr___while_result_is_not_none_successfully(self):
        self.online_calculator.calculating()

        assert self.online_calculator.result == 20.0
        assert isinstance(self.online_calculator.result, float)

        assert self.online_calculator.__repr__() == "Calculation: 12.5 + 7.5 = 20.0" \
                                                    "\nResult: 20.0"
        assert isinstance(self.online_calculator.__repr__(), str)

        self.online_calculator.second_number = -2.5
        assert self.online_calculator.second_number == - 2.5
        assert isinstance(self.online_calculator.second_number, float)

        self.online_calculator.calculating()

        assert self.online_calculator.result == 10.0
        assert isinstance(self.online_calculator.result, float)

        assert self.online_calculator.__repr__() == "Calculation: 12.5 + (-2.5) = 10.0" \
                                                    "\nResult: 10.0"
        assert isinstance(self.online_calculator.__repr__(), str)

    def test___repr___while_result_is_none_successfully(self):
        assert self.online_calculator.__repr__() == "First you have to calculating!"
        assert isinstance(self.online_calculator.__repr__(), str)


if __name__ == "__main__":
    unittest.main()
