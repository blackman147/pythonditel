class Sales_commission_calculator:
    price = 0.0
    salary = 200.00
    total_price_sales = 0.0
    nine_percent_of_total_sales = 0.0
    salary_for_the_week = 0.0

    def sales_data(self):
        counter = 0
        while counter < 4:
            if self.price > 0:
                self.total_price_sales += self.price
            self.price = float(input("Enter your price: "))
            counter += 1

    def calculate_nine_percent_of_total_sales(self):
        self.nine_percent_of_total_sales = (9.0 / 100) * self.total_price_sales

    def calculate_salary_for_the_week(self):
        self.salary_for_the_week = self.salary + (0.09 * self.total_price_sales)

    def display(self):
        print("your salary for the week is: " + str(self.salary))
        print("nine percent of your total sales for this week is: " + str(self.nine_percent_of_total_sales))
        print("your salary for the week is: " + str(self.salary_for_the_week))


def main():
    scc = Sales_commission_calculator()
    scc.sales_data()
    scc.calculate_nine_percent_of_total_sales()
    scc.calculate_salary_for_the_week()
    scc.display()


main()
