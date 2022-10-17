class Calc:
    def __init__(self, rent_property):
        self.prop = rent_property
        self.income = 0
        self.expense = 0
        self.investment = 0

    def income_per_month(self):
        while True:
            rent = float(input(f"How much do you make monthly in rent? $"))
            if rent is not None:
                self.income += rent
            laundry = float(input(f"How much do you charge for laundry? $"))
            if laundry is not None:
                self.income += laundry
            storage = float(
                input(f"How much do you charge monthly for storage? $"))
            if storage is not None:
                self.income += storage
            misc = float(
                input(f"How much do you make in additional income? $"))
            if misc is not None:
                self.income += misc
                print(
                    "-"*50, f"\nYour total monthly income is {self.income:,.2f}\n", "-"*50)
            self.gather_expense()

    def gather_expense(self):
        while True:
            taxes = float(input(f"How much do you pay monthly in taxes? $"))
            if taxes is not None:
                self.expense += taxes
            insurance = float(
                input(f"What is your monthly cost for insurance? $"))
            if insurance is not None:
                self.expense += insurance
            while True:
                utility = input(
                    f"Do you provide any utilities? If so what is it? ").lower()
                if utility == "no":
                    break
                elif utility in {"electric", "electricity", "power"}:
                    electric = float(
                        input(f"How much do you pay monthly in {utility}? $"))
                    self.expense += electric
                elif utility in {"water", "sewer"}:
                    water = float(
                        input(f"How much do you pay monthly in {utility}? $"))
                    self.expense += water
                elif utility in {"gas", "heat", "heating"}:
                    gas = float(
                        input(f"How much do you pay monthly in {utility}? $"))
                    self.expense += gas
                else:
                    continue
                ask = input("Have you listed all of your utilities? $")
                if ask == "yes":
                    break
            hoa = float(input(f"How much do you pay monthly in HOA fees? $"))
            if hoa is not None:
                self.expense += hoa
            lanscaping = float(
                input(f"What is your monthly cost for lanscaping? $"))
            if lanscaping is not None:
                self.expense += lanscaping
            repairs = float(
                input(f"How much do you put away monthly for repairs? $"))
            if repairs is not None:
                self.expense += repairs
            capital_expense = float(
                input(f"How much do you pay monthly in Capital Expense? $"))
            if capital_expense is not None:
                self.expense += capital_expense
            property = float(
                input(f"How much do you pay monthly for a Property Manager? $"))
            if property is not None:
                self.expense += property
            mortgage = float(
                input(f"What is your monthly cost for mortgage? $"))
            if mortgage is not None:
                self.expense += mortgage
                print(
                    "-"*50, f"\nYour total monthly expenses are ${self.expense:,.2f}.\n", "-"*50)
            self.cash_flow()

    def cash_flow(self):
        cash = self.income - self.expense
        print(f"Your pojected cash flow will be ${cash:,.2f}.")
        self.annual_cash = cash * 12
        print(
            f"If you were to look at your anual cash flow from {self.prop} will be ${self.annual_cash:,.2f}")
        self.return_on_investment()

    def return_on_investment(self):
        while True:
            down_payment = float(input(f"How much is your down payment? $"))
            if down_payment is not None:
                self.investment += down_payment
            closing_cost = float(input(f"what are your closing costs? $"))
            if closing_cost is not None:
                self.investment += closing_cost
            rehab = float(input(f"What is yout budget to fix up the place? $"))
            if rehab is not None:
                self.investment += rehab
            misc_costs = float(
                input(f"What do you expect in miscellaneous costs? $"))
            if misc_costs is not None:
                self.investment += misc_costs
            roi = self.annual_cash / self.investment
            if roi <= 0:
                total = (
                    "-"*50, f"Your return on your investment is -{roi:,.2f}%", "-"*50)
                return total
            else:
                total1 = (
                    "-"*50, f"Your return on your investment is {roi:,.2f}%", "-"*50)
                return total1


house1 = Calc("Blue Multi-family")
house1.income_per_month()
