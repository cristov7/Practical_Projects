from daily_energy_consumption_oop.daily_energy_consumption import DailyEnergyConsumption
import unittest


class DailyEnergyConsumptionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.energy = DailyEnergyConsumption(83.750, 178.50, 26, "man", 1.55)

    def test___init___successfully(self):
        assert self.energy.weight == 83.750
        assert isinstance(self.energy.weight, float)

        assert self.energy.height == 178.50
        assert isinstance(self.energy.height, float)

        assert self.energy.age == 26
        assert isinstance(self.energy.age, int)

        assert self.energy.gender == "man"
        assert isinstance(self.energy.gender, str)

        assert self.energy.physical_activity_factor == 1.55
        assert isinstance(self.energy.physical_activity_factor, float)

        assert self.energy.main_exchange is None

        assert self.energy.daily_energy_consumption is None

    def test_set_weight_successfully(self):
        self.energy.weight = 87
        assert self.energy.weight == 87
        assert isinstance(self.energy.weight, int)

        self.energy.weight = 99.500
        assert self.energy.weight == 99.5
        assert isinstance(self.energy.weight, float)

    def test_set_weight_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.energy.weight = 300.1
        assert str(content.exception) == "Invalid weight. Try again in kg..."

        with self.assertRaises(ValueError) as content:
            self.energy.weight = 0.00
        assert str(content.exception) == "Invalid weight. Try again in kg..."

        assert self.energy.weight == 83.750
        assert isinstance(self.energy.weight, float)

    def test_set_height_successfully(self):
        self.energy.height = 185
        assert self.energy.height == 185
        assert isinstance(self.energy.height, int)

        self.energy.height = 199.750
        assert self.energy.height == 199.75
        assert isinstance(self.energy.height, float)

    def test_set_height_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.energy.height = 300.1
        assert str(content.exception) == "Invalid height. Try again in cm..."

        with self.assertRaises(ValueError) as content:
            self.energy.height = 0.00
        assert str(content.exception) == "Invalid height. Try again in cm..."

        assert self.energy.height == 178.50
        assert isinstance(self.energy.height, float)

    def test_set_age_successfully(self):
        self.energy.age = 18
        assert self.energy.age == 18
        assert isinstance(self.energy.age, int)

    def test_set_age_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.energy.age = 18.5
        assert str(content.exception) == "Invalid age. Try again..."

        with self.assertRaises(ValueError) as content:
            self.energy.age = 0
        assert str(content.exception) == "Invalid age. Try again..."

        with self.assertRaises(ValueError) as content:
            self.energy.age = 101
        assert str(content.exception) == "Invalid age. Try again..."

        assert self.energy.age == 26
        assert isinstance(self.energy.age, int)

    def test_calculate_main_exchange_while_is_none_as_a_woman_successfully(self):
        self.energy.gender = "woman"
        assert self.energy.gender == "woman"
        assert isinstance(self.energy.gender, str)

        self.energy.calculate_main_exchange()

        assert self.energy.main_exchange == 1664.725
        assert isinstance(self.energy.main_exchange, float)

    def test_calculate_main_exchange_while_is_none_as_a_man_successfully(self):
        self.energy.calculate_main_exchange()

        assert self.energy.main_exchange == 1830.725
        assert isinstance(self.energy.main_exchange, float)

    def test_calculate_main_exchange_while_is_not_none_successfully(self):
        self.energy.main_exchange = 2000
        assert self.energy.main_exchange == 2000
        assert isinstance(self.energy.main_exchange, int)

        self.energy.calculate_main_exchange()

        assert self.energy.main_exchange == 2000
        assert isinstance(self.energy.main_exchange, int)

    def test_calculate_daily_energy_consumption_factor_while_is_none_successfully(self):
        self.energy.calculate_daily_energy_consumption()

        assert self.energy.main_exchange == 1830.725
        assert isinstance(self.energy.main_exchange, float)

        assert self.energy.daily_energy_consumption == 2837.6237499999997
        assert isinstance(self.energy.daily_energy_consumption, float)

    def test_calculate_daily_energy_consumption_while_is_not_none_successfully(self):
        self.energy.main_exchange = 1850
        assert self.energy.main_exchange == 1850
        assert isinstance(self.energy.main_exchange, int)

        self.energy.calculate_daily_energy_consumption()

        assert self.energy.daily_energy_consumption == 2867.5
        assert isinstance(self.energy.daily_energy_consumption, float)

    def test___repr___while_main_exchange_and_daily_energy_consumption_are_not_none_successfully(self):
        self.energy.calculate_daily_energy_consumption()

        assert self.energy.__repr__() == "Calculation:" \
                                         "\n- Main Exchange: 1830.72 kcal." \
                                         "\n- Daily Energy Consumption: 2837.62 kcal."

    def test___repr___while_main_exchange_and_energy_consumption_are_none_successfully(self):
        assert self.energy.__repr__() == "First you have to calculate main exchange and daily energy consumption!"
        assert isinstance(self.energy.__repr__(), str)

    def test___repr___while_main_exchange_is_none_successfully(self):
        self.energy.daily_energy_consumption = 2750
        assert self.energy.daily_energy_consumption == 2750
        assert isinstance(self.energy.daily_energy_consumption, int)

        assert self.energy.__repr__() == "First you have to calculate main exchange and daily energy consumption!"
        assert isinstance(self.energy.__repr__(), str)

    def test___repr___while_energy_consumption_is_none_successfully(self):
        self.energy.calculate_main_exchange()

        assert self.energy.main_exchange == 1830.725
        assert isinstance(self.energy.main_exchange, float)

        assert self.energy.__repr__() == "First you have to calculate main exchange and daily energy consumption!"
        assert isinstance(self.energy.__repr__(), str)


if __name__ == '__main__':
    unittest.main()
