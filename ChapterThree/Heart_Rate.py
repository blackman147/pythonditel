class Heart_Rate:
    _firstname = ""
    _lastname = ""
    _day = 0
    _month = 0
    _birth_year = 0
    _age = 0
    _current_year = 2021
    _maximum_heart_rate = 0
    _target_heart_rate = 0.0

    def heart_rate(self, firstname, lastname, day, month, year):
        self._firstname = firstname
        self._lastname = lastname
        self._day = day
        self._month = month
        self._birth_year = year

    def calculate_age(self):
        self._age = self._current_year - self._birth_year

    def calculate_maximum_heart_rate(self):
        self._maximum_heart_rate = 220 - self._age

    def calculate_target_heart_rate(self):
        self._target_heart_rate = 0.67 * self._maximum_heart_rate

    def display(self):
        print("Your name is: " + self._firstname + " " + self._lastname)
        print("your date of birth is: " + str(self._day) + "/" + str(self._month) + "/" + str(self._birth_year))
        print("Your age is: " + str(self._age))
        print("Your Maximum Heart Rate is: " + str(self._maximum_heart_rate))
        print("Your Target Heart Rate is: " + str(self._target_heart_rate))


def main():
    hr = Heart_Rate()
    hr.heart_rate("Francis", "Ntoka", 3, 7, 1992)
    hr.calculate_age()
    hr.calculate_maximum_heart_rate()
    hr.calculate_target_heart_rate()
    hr.display()


main()
