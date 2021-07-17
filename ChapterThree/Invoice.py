class Invoice:
    part_number = "2f567p"
    part_description = "hammer"
    item_quantity = 10
    item_price = 500.0
    total_item_amount = 0

    def __int__(self, number, description, quantity, price):
        self.part_number = number
        self.part_description = description
        self.item_quantity = quantity
        self.item_price = price

    def display(self):
        print("Item part number is: " + str(self.part_number))
        print("part description is: " + str(self.part_description))
        print("item quantity = " + str(self.item_quantity))
        print("Item price = " + str(self.item_price))
        print("Total amount of items bought = " + str(self.total_item_amount))

    def total_invoice_amount(self):
        self.total_item_amount = self.item_price * self.item_quantity


obj = Invoice()
obj.total_invoice_amount()
obj.display()
