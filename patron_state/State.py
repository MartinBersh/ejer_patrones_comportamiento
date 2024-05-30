class State:
    def __init__(self, phone):
        self.phone = phone

    def on_home(self):
        raise NotImplementedError

    def on_off_on(self):
        raise NotImplementedError
