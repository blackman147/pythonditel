class Gas_mileage:
    miles_driven = 0
    gallons_used = 0
    miles_per_gallons = 0
    total_miles_per_gallons = 0

    def gas_data(self):

        while self.miles_driven != -1 and self.gallons_used != -1:
            miles_driven = int(input("Enter miles driven: "))
            gallons_used = int(input("Enter gallons used on this trip"))

            self.miles_per_gallons = miles_driven / gallons_used
            self.total_miles_per_gallons += self.miles_per_gallons

        while self.miles_driven == -1 and self.gallons_used == -1:
            print("your miles per gallons is: " + str(self.miles_per_gallons))
            print("your total miles per gallons is: " + str(self.total_miles_per_gallons))


def main():
    gm = Gas_mileage()
    gm.gas_data()


main()
