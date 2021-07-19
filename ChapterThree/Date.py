class Date:
    _day = 0
    _month = 0
    _year = 0

    def date(self, day, month, year):

        if 0 < day < 31:
            self._day = day

        if 0 < month < 12:
            self._month = month

        self._year = year

    def display(self):
        print("Today's date is: " + str(self._day) + "/" + str(self._month) + "/" + str(self._year))


def main():
    dt = Date()
    dt.date(19, 7, 2021)
    dt.display()


main()
