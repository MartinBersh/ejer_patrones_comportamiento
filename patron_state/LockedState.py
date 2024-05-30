from patron_state.ReadyState import ReadyState
from patron_state.State import State


class LockedState(State):
    def _init_(self, phone):
        super()._init_(phone)

    def on_home(self):
        self.phone.set_state(ReadyState(self.phone))
        return self.phone.unlock()

    def on_off_on(self):
        from patron_state.OffState import OffState
        self.phone.set_state(OffState(self.phone))
        return self.phone.lock()

