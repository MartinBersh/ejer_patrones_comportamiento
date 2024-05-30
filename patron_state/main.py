from patron_state.Phone import Phone

class MainApp:
    @staticmethod
    def main():
        phone = Phone()
        MainApp.simulate_phone_clicks(phone)

    @staticmethod
    def simulate_phone_clicks(phone):
        print(phone.click_power())
        print(phone.click_power())
        print(phone.click_home())
        print(phone.click_home())
        print(phone.click_home())
        print(phone.click_power())
        print(phone.click_power())
        print(phone.click_home())

if __name__ == "__main__":
    MainApp.main()
