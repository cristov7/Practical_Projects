from energy_converter_oop.energy_converter import EnergyConverter
import unittest


class EnergyConverterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.energy_converter = EnergyConverter("from kcal to kJ", 2350.750)

    def test_energy_dict_successfully(self):
        assert self.energy_converter.ENERGY_DICT == {"from kcal to kJ": 4.18, "from kJ to kcal": 0.24}
        assert isinstance(self.energy_converter.ENERGY_DICT, dict)

    def test___init___successfully(self):
        assert self.energy_converter.option == "from kcal to kJ"
        assert isinstance(self.energy_converter.option, str)

        assert self.energy_converter.energy == 2350.750
        assert isinstance(self.energy_converter.energy, float)

        assert self.energy_converter.convert_energy is None

    def test_set_energy_successfully(self):
        self.energy_converter.energy = 3000
        assert self.energy_converter.energy == 3000
        assert isinstance(self.energy_converter.energy, int)

        self.energy_converter.energy = 2499.999
        assert self.energy_converter.energy == 2499.999
        assert isinstance(self.energy_converter.energy, float)

    def test_set_energy_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.energy_converter.energy = 0.00
        assert str(content.exception) == "Invalid energy. Try again..."

        assert self.energy_converter.energy == 2350.750
        assert isinstance(self.energy_converter.energy, float)

    def test___converter_from_kcal_to_kj_successfully(self):   # private method
        assert self.energy_converter._EnergyConverter__converter_from_kcal_to_kj() == 9826.135
        assert isinstance(self.energy_converter._EnergyConverter__converter_from_kcal_to_kj(), float)

    def test___converter_from_kj_to_kcal_successfully(self):   # private method
        assert self.energy_converter._EnergyConverter__converter_from_kj_to_kcal() == 564.18
        assert isinstance(self.energy_converter._EnergyConverter__converter_from_kj_to_kcal(), float)

    def test_calculate_convert_energy_from_kcal_to_kj_successfully(self):
        self.energy_converter.calculate_convert_energy()

        assert self.energy_converter.convert_energy == 9826.135
        assert isinstance(self.energy_converter.convert_energy, float)

    def test_calculate_convert_energy_from_kj_to_kcal_successfully(self):
        self.energy_converter.option = "from kJ to kcal"
        assert self.energy_converter.option == "from kJ to kcal"
        assert isinstance(self.energy_converter.option, str)

        self.energy_converter.calculate_convert_energy()

        assert self.energy_converter.convert_energy == 564.18
        assert isinstance(self.energy_converter.convert_energy, float)

    def test___repr___while_convert_energy_is_not_none_from_kcal_to_kj_successfully(self):
        self.energy_converter.calculate_convert_energy()

        assert self.energy_converter.convert_energy == 9826.135
        assert isinstance(self.energy_converter.convert_energy, float)

        assert self.energy_converter.__repr__() == "Converting from kcal to kJ:" \
                                                   "\n2350.75 kcal = 9826.14 kJ"
        assert isinstance(self.energy_converter.__repr__(), str)

    def test___repr___while_convert_energy_is_not_none_from_kj_to_kcal_successfully(self):
        self.energy_converter.option = "from kJ to kcal"
        assert self.energy_converter.option == "from kJ to kcal"
        assert isinstance(self.energy_converter.option, str)

        self.energy_converter.calculate_convert_energy()

        assert self.energy_converter.convert_energy == 564.18
        assert isinstance(self.energy_converter.convert_energy, float)

        assert self.energy_converter.__repr__() == "Converting from kJ to kcal:" \
                                                   "\n2350.75 kJ = 564.18 kcal"
        assert isinstance(self.energy_converter.__repr__(), str)

    def test___repr___while_convert_energy_is_none_successfully(self):
        assert self.energy_converter.__repr__() == "First you have to calculate convert energy!"
        assert isinstance(self.energy_converter.__repr__(), str)


if __name__ == "__main__":
    unittest.main()
