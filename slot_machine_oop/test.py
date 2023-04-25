from slot_machine_oop.slot_machine import SlotMachine
import unittest


class SlotMachineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.slot_machine = SlotMachine()

    def test___init___successfully(self):
        assert self.slot_machine.icons == ['🍒', '🍊', '🍋', '🍉', '🍇', '🍓']
        assert isinstance(self.slot_machine.icons, list)

        assert self.slot_machine.bet == 0
        assert isinstance(self.slot_machine.bet, int)

        assert self.slot_machine.balance == 0
        assert isinstance(self.slot_machine.balance, int)

    def test_add_money_successfully(self):
        assert self.slot_machine.add_money(1000) == f"\n\nAdded 1000 lv. to your balance." \
                                                    f"\nYour new balance is: 1000 lv."
        assert self.slot_machine.balance == 1000
        assert isinstance(self.slot_machine.balance, int)

        assert self.slot_machine.add_money(500) == f"\n\nAdded 500 lv. to your balance." \
                                                   f"\nYour new balance is: 1500 lv."
        assert self.slot_machine.balance == 1500
        assert isinstance(self.slot_machine.balance, int)

    def test_remove_money_successfully(self):
        self.slot_machine.add_money(1000)
        assert self.slot_machine.balance == 1000
        assert isinstance(self.slot_machine.balance, int)

        assert self.slot_machine.remove_money(100) == f"\n\nRemoved 100 lv.from your balance." \
                                                      f"\nYour new balance is: 900"
        assert self.slot_machine.balance == 900
        assert isinstance(self.slot_machine.balance, int)

    def test_remove_money_unsuccessfully(self):
        assert self.slot_machine.remove_money(100) == f"\n\nCan't remove 100 lv. from your balance!" \
                                                      f"\nYour balance is: 0"

    def test_play_without_money_successfully(self):
        assert self.slot_machine.play() == "Sorry, you don't have enough money to play."

    # def test_play_with_different_equal_icons_successfully(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
