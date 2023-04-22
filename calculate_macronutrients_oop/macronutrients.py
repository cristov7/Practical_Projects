from abc import ABC, abstractmethod


class Macronutrients(ABC):
    @property                           # getter
    @abstractmethod                     # abstractmethod
    def kcal_per_gram(self) -> float:   # must be implemented
        pass

    def details(self) -> str:
        class_name = self.__class__.__name__
        kcal = self.kcal_per_gram
        return f"1 g {class_name} = {kcal} kcal"
