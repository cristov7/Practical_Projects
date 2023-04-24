from calculate_macronutrients_oop.macronutrients import Macronutrients


class Carb(Macronutrients):
    PERCENT: int = 55

    @property                           # getter
    def kcal_per_gram(self) -> float:   # implemented method
        kcal = 4.1
        return kcal
