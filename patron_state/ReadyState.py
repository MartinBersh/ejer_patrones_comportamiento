from patron_state import OffState
from patron_state.State import State


class ReadyState(State):
    def _init_(self, phone):
        super()._init_(phone)

    def on_home(self):
        return self.phone.home()

    def on_off_on(self):
        self.phone.set_state(OffState.OffState(self.phone))
        return self.phone.lock()

