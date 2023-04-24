from calculate_macronutrients_oop.macronutrients import Macronutrients


class Fat(Macronutrients):
    PERCENT: int = 30

    @property                           # getter
    def kcal_per_gram(self) -> float:   # implemented method
        kcal = 9.3
        return kcal
