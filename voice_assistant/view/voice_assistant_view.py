class VoiceAssistantView:
    def show_menu(self):
        print("Welcome to the Voice Assistant!")
        print("1. Get current time")
        print("2. Get current date")
        print("3. Exit")

    def show_time(self, time):
        print("Current time is:", time)

    def show_date(self, date):
        print("Current date is:", date)