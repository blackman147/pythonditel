class Employee:
    _firstname = ""
    _lastname = ""
    _monthly_salary = 0
    _yearly_salary = 0
    _monthly_salary_after_increase = 0
    _yearly_salary_after_increase = 0

    def employee_data(self, firstname, lastname, salary):
        self._firstname = firstname
        self._lastname = lastname

        if salary > 0:
            self._monthly_salary = salary
        else:
            print("invalid salary amount")

    def yearly_salary(self):
        self._yearly_salary = self._monthly_salary * 12

    def salary_increment_rate(self, rate):
        self._monthly_salary_after_increase = self._monthly_salary + ((rate / 100) * self._monthly_salary)

    def yearly_salary_after_increment(self, rate):
        self._yearly_salary_after_increase = (self._monthly_salary + ((rate / 100) * self._monthly_salary)) * 12

    def display(self):
        print("Employee firstname is: " + str(self._firstname))
        print("Employee lastname is: " + str(self._lastname))
        print("Employee monthly salary is: " + str(self._monthly_salary))
        print("Employee yearly salary is: " + str(self._yearly_salary))
        print("Employee salary after 10% increase is: " + str(self._monthly_salary_after_increase))
        print("Employee yearly salary after 10% increase is: " + str(self._yearly_salary_after_increase))


def main():
    emp1 = Employee()
    emp1.employee_data("Joy", "Udom", 100000)
    emp1.yearly_salary()
    emp1.salary_increment_rate(10.0)
    emp1.yearly_salary_after_increment(10.0)
    emp1.display()
    print( "Employee two  ")

    emp2 = Employee()
    emp2.employee_data("Blackman", "Francis", 100000)
    emp2.yearly_salary()
    emp2.salary_increment_rate(10.0)
    emp2.yearly_salary_after_increment(10.0)
    emp2.display()



main()
