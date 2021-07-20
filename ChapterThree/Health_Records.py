class Health_Records:
    _firstname = ""
    _lastname = ""
    _gender = ""
    _day = 0
    _month = 0
    _birth_year = 0
    _height = 0.0
    _weight = 0.0
    _age = 0
    _current_year = 2021
    _maximum_heart_rate = 0
    _target_heart_rate = 0.0
    _bmi = 0.0

    def health_records(self, firstname, lastname, gender, day, month, year, height, weight):
        self._firstname = firstname
        self._lastname = lastname
        self._gender = gender
        self._day = day
        self._month = month
        self._birth_year = year
        self._height = height
        self._weight = weight

    def calculate_age(self):
        self._age = self._current_year - self._birth_year

    def calculate_maximum_heart_rate(self):
        self._maximum_heart_rate = 220 - self._age

    def calculate_target_heart_rate(self):
        self._target_heart_rate = 0.67 * self._maximum_heart_rate

    def calculate_BMI(self):
        self._bmi = (self._weight * 703) / (self._height * self._height);

    def display(self):
        print("Your name is: " + self._firstname + " " + self._lastname)
        print("your date of birth is: " + str(self._day) + "/" + str(self._month) + "/" + str(self._birth_year))
        print("Your age is: " + str(self._age))
        print("Your Maximum Heart Rate is: " + str(self._maximum_heart_rate))
        print("Your Target Heart Rate is: " + str(self._target_heart_rate))

        print("BMI VALUES")
        print("BMI = " + str(self._bmi))
        print("Underweight: less than 18.5")
        print("Normal: between 18.5 and 29.9")
        print("Obese: 30 or greater")


def main():
    hr = Health_Records()
    hr.health_records("Francis", "Ntoka", "male", 3, 7, 1992, 170.00, 80)
    hr.calculate_age()
    hr.calculate_maximum_heart_rate()
    hr.calculate_target_heart_rate()
    hr.calculate_BMI()
    hr.display()


main()
