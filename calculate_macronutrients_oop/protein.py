from calculate_macronutrients_oop.macronutrients import Macronutrients


class Protein(Macronutrients):
    PERCENT: int = 15

    @property                           # getter
    def kcal_per_gram(self) -> float:   # implemented method
        kcal = 4.1
        return kcal
