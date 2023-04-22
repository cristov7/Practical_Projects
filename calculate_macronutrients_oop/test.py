from calculate_macronutrients_oop.calculate_macronutrients import CalculateMacronutrients
import unittest


class CalculateMacronutrientsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calc_macros = CalculateMacronutrients(2500)

    def test_percents_dict_successfully(self):
        assert self.calc_macros.PERCENTS_DICT == {"Protein": 15, "Fat": 30, "Carb": 55}
        assert isinstance(CalculateMacronutrients.PERCENTS_DICT, dict)

    def test___init___successfully(self):
        assert self.calc_macros.daily_target_kcal == 2500
        assert isinstance(self.calc_macros.daily_target_kcal, int)

        assert self.calc_macros.protein_kcal is None

        assert self.calc_macros.fat_kcal is None

        assert self.calc_macros.carb_kcal is None

    def test_set_daily_target_kcal_successfully(self):
        self.calc_macros.daily_target_kcal = 2800.50
        assert self.calc_macros.daily_target_kcal == 2800.50
        assert isinstance(self.calc_macros.daily_target_kcal, float)

        self.calc_macros.daily_target_kcal = 3250
        assert self.calc_macros.daily_target_kcal == 3250
        assert isinstance(self.calc_macros.daily_target_kcal, int)

    def test_set_daily_target_kcal_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.calc_macros.daily_target_kcal = 0
        assert str(content.exception) == "Invalid kcal! Try again..."

        assert self.calc_macros.daily_target_kcal == 2500
        assert isinstance(self.calc_macros.daily_target_kcal, int)

    def test___calculate_protein_kcal_successfully(self):
        self.calc_macros._CalculateMacronutrients__calculate_protein_kcal()   # private method

        assert self.calc_macros.protein_kcal == 375.0
        assert isinstance(self.calc_macros.protein_kcal, float)

    def test___calculate_fat_kcal_successfully(self):
        self.calc_macros._CalculateMacronutrients__calculate_fat_kcal()   # private method

        assert self.calc_macros.fat_kcal == 750.0
        assert isinstance(self.calc_macros.fat_kcal, float)

    def test___calculate_carb_kcal_successfully(self):
        self.calc_macros._CalculateMacronutrients__calculate_carb_kcal()   # private method

        assert self.calc_macros.carb_kcal == 1375.0
        assert isinstance(self.calc_macros.carb_kcal, float)

    def test_calculate_macronutrients_successfully(self):
        self.calc_macros.calculate_macronutrients()

        assert self.calc_macros.protein_kcal == 375.0
        assert isinstance(self.calc_macros.protein_kcal, float)

        assert self.calc_macros.fat_kcal == 750.0
        assert isinstance(self.calc_macros.fat_kcal, float)

        assert self.calc_macros.carb_kcal == 1375.0
        assert isinstance(self.calc_macros.carb_kcal, float)

    # def test___repr___successfully(self):
    #     assert self.calc_macros.__repr__() == "Protein 15 % -> 375.00 kcal" \
    #                                           "\nFat 30 % -> 750.00 kcal" \
    #                                           "\nCarb 55 % -> 1375.00 kcal" \
    #                                           "\n\n(1 g Protein = 4.1 kcal)" \
    #                                           "\n(1 g Fat = 9.3 kcal)" \
    #                                           "\n(1 g Carb = 4.1 kcal)"


if __name__ == '__main__':
    unittest.main()
