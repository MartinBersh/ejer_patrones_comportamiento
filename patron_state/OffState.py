from patron_state.LockedState import LockedState
from patron_state.State import State


class OffState(State):
    def _init_(self, phone):
        super()._init_(phone)

    def on_home(self):
        self.phone.set_state(LockedState(self.phone))
        return self.phone.turn_on()

    def on_off_on(self):
        self.phone.set_state(LockedState(self.phone))
        return self.phone.turn_on()
