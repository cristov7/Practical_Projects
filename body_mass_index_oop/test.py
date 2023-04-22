from body_mass_index_oop.body_mass_index import BodyMassIndex
import unittest


class BodyMassIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bmi = BodyMassIndex(78.500, 178.500)

    def test___init___successfully(self):
        assert self.bmi.weight == 78.500
        assert isinstance(self.bmi.weight, float)

        assert self.bmi.height == 178.500
        assert isinstance(self.bmi.weight, float)

        assert self.bmi.body_mass_index is None

    def test_set_weight_successfully(self):
        self.bmi.weight = 87
        assert self.bmi.weight == 87
        assert isinstance(self.bmi.weight, int)

        self.bmi.weight = 99.500
        assert self.bmi.weight == 99.5
        assert isinstance(self.bmi.weight, float)

    def test_set_weight_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.bmi.weight = 300.1
        assert str(content.exception) == "Invalid weight. Try again in kg..."

        assert self.bmi.weight == 78.500
        assert isinstance(self.bmi.weight, float)

    def test_set_height_successfully(self):
        self.bmi.height = 185
        assert self.bmi.height == 185
        assert isinstance(self.bmi.height, int)

        self.bmi.height = 199.750
        assert self.bmi.height == 199.75
        assert isinstance(self.bmi.height, float)

    def test_set_height_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.bmi.height = 300.1
        assert str(content.exception) == "Invalid height. Try again in cm..."

        assert self.bmi.height == 178.500
        assert isinstance(self.bmi.weight, float)

    def test_calculate_body_mass_index_with_zero_degree_of_obesity_successfully(self):
        self.bmi.calculate_body_mass_index()
        assert self.bmi.body_mass_index == 0
        assert isinstance(self.bmi.body_mass_index, int)

    def test_calculate_body_mass_index_with_first_degree_of_obesity_successfully(self):
        self.bmi.weight = 83.500

        self.bmi.calculate_body_mass_index()
        assert self.bmi.body_mass_index == 1
        assert isinstance(self.bmi.body_mass_index, int)

    def test_calculate_body_mass_index_with_second_degree_of_obesity_successfully(self):
        self.bmi.weight = 99.500

        self.bmi.calculate_body_mass_index()
        assert self.bmi.body_mass_index == 2
        assert isinstance(self.bmi.body_mass_index, int)

    def test_calculate_body_mass_index_with_third_degree_of_obesity_successfully(self):
        self.bmi.weight = 130.000

        self.bmi.calculate_body_mass_index()
        assert self.bmi.body_mass_index == 3
        assert isinstance(self.bmi.body_mass_index, int)

    def test___repr___without_set_body_mass_index_successfully(self):
        assert self.bmi.__repr__() == "First you have to calculate body mass index!"
        assert isinstance(self.bmi.__repr__(), str)

    def test___repr___already_set_body_mass_index_successfully(self):
        self.bmi.calculate_body_mass_index()

        assert self.bmi.__repr__() == "0th degree of obesity."
        assert isinstance(self.bmi.__repr__(), str)


if __name__ == '__main__':
    unittest.main()
