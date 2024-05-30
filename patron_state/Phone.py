from patron_state.OffState import OffState

class Phone:
    def __init__(self):
        self.state = OffState(self)

    def set_state(self, state):
        self.state = state

    def lock(self):
        return "Locking phone and turning off the screen"

    def home(self):
        return "Going to home-screen"

    def unlock(self):
        return "Unlocking the phone to home"

    def turn_on(self):
        return "Turning screen on, device still locked"

    def click_home(self):
        return self.state.on_home()

    def click_power(self):
        return self.state.on_off_on()
