from numerals_systems_oop.numerals_systems import NumeralsSystems
import unittest


class NumeralsSystemsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.numerals_systems = NumeralsSystems("1", 47)

    def test_numerals_systems_dict_successfully(self):
        assert self.numerals_systems.NUMERALS_SYSTEMS_DICT == {"1": ["From Decimal to Binary numeral system", 10, 2],
                                                               "2": ["From Hexadecimal to Binary numeral system", 16, 2],
                                                               "3": ["From Binary to Decimal numeral system", 2, 10],
                                                               "4": ["From Hexadecimal to Decimal numeral system", 16, 10],
                                                               "5": ["From Binary to Hexadecimal numeral system", 2, 16],
                                                               "6": ["From Decimal to Hexadecimal numeral system", 10, 16]}
        assert isinstance(self.numerals_systems.NUMERALS_SYSTEMS_DICT, dict)

    def test___init___successfully(self):
        assert self.numerals_systems.option == "1"
        assert isinstance(self.numerals_systems.option, str)

        assert self.numerals_systems.number == 47
        assert isinstance(self.numerals_systems.number, int)

        assert self.numerals_systems.convert_number is None

    def test_set_option_successfully(self):
        self.numerals_systems.option = "2"

        assert self.numerals_systems.option == "2"
        assert isinstance(self.numerals_systems.option, str)

    def test_set_option_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.numerals_systems.option = 2
        assert str(content.exception) == "Invalid numeral system! Try again..."

        assert self.numerals_systems.option == "1"
        assert isinstance(self.numerals_systems.option, str)

    def test_set_number_with_option_1_successfully(self):
        self.numerals_systems.number = 100
        assert self.numerals_systems.number == 100
        assert isinstance(self.numerals_systems.number, int)

    def test_set_number_with_option_1_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.numerals_systems.number = "100"
        assert str(content.exception) == "Invalid number! Try again..."

        assert self.numerals_systems.number == 47
        assert isinstance(self.numerals_systems.number, int)

    def test_set_number_with_option_6_successfully(self):
        self.numerals_systems.option = "6"
        assert self.numerals_systems.option == "6"
        assert isinstance(self.numerals_systems.option, str)

        self.numerals_systems.number = 100
        assert self.numerals_systems.number == 100
        assert isinstance(self.numerals_systems.number, int)

    def test_set_number_with_option_6_and_raise_value_error(self):
        self.numerals_systems.option = "6"
        assert self.numerals_systems.option == "6"
        assert isinstance(self.numerals_systems.option, str)

        with self.assertRaises(ValueError) as content:
            self.numerals_systems.number = "100"
        assert str(content.exception) == "Invalid number! Try again..."

        assert self.numerals_systems.number == 47
        assert isinstance(self.numerals_systems.number, int)

    def test_set_number_with_option_2_successfully(self):
        self.numerals_systems.option = "2"
        assert self.numerals_systems.option == "2"
        assert isinstance(self.numerals_systems.option, str)

        self.numerals_systems.number = "100"
        assert self.numerals_systems.number == "100"
        assert isinstance(self.numerals_systems.number, str)

    def test_set_number_with_option_2_and_raise_value_error(self):
        self.numerals_systems.option = "2"
        assert self.numerals_systems.option == "2"
        assert isinstance(self.numerals_systems.option, str)

        with self.assertRaises(ValueError) as content:
            self.numerals_systems.number = 100
        assert str(content.exception) == "Invalid number! Try again..."

        assert self.numerals_systems.number == 47
        assert isinstance(self.numerals_systems.number, int)

    def test_set_number_with_option_4_successfully(self):
        self.numerals_systems.option = "4"
        assert self.numerals_systems.option == "4"
        assert isinstance(self.numerals_systems.option, str)

        self.numerals_systems.number = "100"
        assert self.numerals_systems.number == "100"
        assert isinstance(self.numerals_systems.number, str)

    def test_set_number_with_option_4_and_raise_value_error(self):
        self.numerals_systems.option = "4"
        assert self.numerals_systems.option == "4"
        assert isinstance(self.numerals_systems.option, str)

        with self.assertRaises(ValueError) as content:
            self.numerals_systems.number = 100
        assert str(content.exception) == "Invalid number! Try again..."

        assert self.numerals_systems.number == 47
        assert isinstance(self.numerals_systems.number, int)

    def test_set_number_with_option_3_successfully(self):
        self.numerals_systems.option = "3"
        assert self.numerals_systems.option == "3"
        assert isinstance(self.numerals_systems.option, str)

        self.numerals_systems.number = "100"
        assert self.numerals_systems.number == "100"
        assert isinstance(self.numerals_systems.number, str)

    def test_set_number_with_option_3_and_raise_value_error(self):
        self.numerals_systems.option = "3"
        assert self.numerals_systems.option == "3"
        assert isinstance(self.numerals_systems.option, str)

        with self.assertRaises(ValueError) as content:
            self.numerals_systems.number = 100
        assert str(content.exception) == "Invalid number! Try again..."

        assert self.numerals_systems.number == 47
        assert isinstance(self.numerals_systems.number, int)

    def test_set_number_with_option_5_successfully(self):
        self.numerals_systems.option = "2"
        assert self.numerals_systems.option == "2"
        assert isinstance(self.numerals_systems.option, str)

        self.numerals_systems.number = "100"
        assert self.numerals_systems.number == "100"
        assert isinstance(self.numerals_systems.number, str)

    def test_set_number_with_option_5_and_raise_value_error(self):
        self.numerals_systems.option = "5"
        assert self.numerals_systems.option == "5"
        assert isinstance(self.numerals_systems.option, str)

        with self.assertRaises(ValueError) as content:
            self.numerals_systems.number = 100
        assert str(content.exception) == "Invalid number! Try again..."

        assert self.numerals_systems.number == 47
        assert isinstance(self.numerals_systems.number, int)

    def test_convert_number_with_option_1_successfully(self):
        self.numerals_systems.set_convert_number()

        assert self.numerals_systems.convert_number == "101111"
        assert isinstance(self.numerals_systems.convert_number, str)

    def test_convert_number_with_option_2_successfully(self):
        self.new_numerals_systems = NumeralsSystems("2", "1A")

        self.new_numerals_systems.set_convert_number()

        assert self.new_numerals_systems.convert_number == "00011010"
        assert isinstance(self.new_numerals_systems.convert_number, str)

        with self.assertRaises(ValueError) as content:
            self.new_numerals_systems = NumeralsSystems("2", 11010)
        assert str(content.exception) == "Invalid number! Try again..."

    def test_convert_number_with_option_3_successfully(self):
        self.new_numerals_systems = NumeralsSystems("3", "01011010")

        self.new_numerals_systems.set_convert_number()

        assert self.new_numerals_systems.convert_number == 90
        assert isinstance(self.new_numerals_systems.convert_number, int)

        with self.assertRaises(ValueError) as content:
            self.new_numerals_systems = NumeralsSystems("3", 1011010)
        assert str(content.exception) == "Invalid number! Try again..."

    def test_convert_number_with_option_4_successfully(self):
        self.new_numerals_systems = NumeralsSystems("4", "1A")

        self.new_numerals_systems.set_convert_number()

        assert self.new_numerals_systems.convert_number == 26
        assert isinstance(self.new_numerals_systems.convert_number, int)

        with self.assertRaises(ValueError) as content:
            self.new_numerals_systems = NumeralsSystems("4", 110)
        assert str(content.exception) == "Invalid number! Try again..."

    def test_convert_number_with_option_5_successfully(self):
        self.new_numerals_systems = NumeralsSystems("5", "01011010")

        self.new_numerals_systems.set_convert_number()

        assert self.new_numerals_systems.convert_number == "5A"
        assert isinstance(self.new_numerals_systems.convert_number, str)

        with self.assertRaises(ValueError) as content:
            self.new_numerals_systems = NumeralsSystems("5", 1011010)
        assert str(content.exception) == "Invalid number! Try again..."

    def test_convert_number_with_option_6_successfully(self):
        self.new_numerals_systems = NumeralsSystems("6", 90)

        self.new_numerals_systems.set_convert_number()

        assert self.new_numerals_systems.convert_number == "5A"
        assert isinstance(self.new_numerals_systems.convert_number, str)

        with self.assertRaises(ValueError) as content:
            self.new_numerals_systems = NumeralsSystems("6", "90")
        assert str(content.exception) == "Invalid number! Try again..."

    def test___repr__with_set_convert_number_successfully(self):
        self.numerals_systems.set_convert_number()

        assert self.numerals_systems.__repr__() == "From Decimal to Binary numeral system:" \
                                                   "\n47(10) = 101111(2)"
        assert isinstance(self.numerals_systems.__repr__(), str)

    def test___repr__without_set_convert_number_successfully(self):
        assert self.numerals_systems.__repr__() == "First you have to set convert number!"
        assert isinstance(self.numerals_systems.__repr__(), str)


if __name__ == "__main":
    unittest.main()
