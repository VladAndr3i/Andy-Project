class Stock:

    def __init__(self, ticker: str, company_name: str, field: str, country: str, number_of_employees: int,
                 amount: float = 0):
        self.ticker = ticker
        self.company = company_name
        self.field = field
        self.amount = amount
        self.long_summary = ""
        self.exchange = ""
        self.country = country
        self.number_of_employees = number_of_employees
        self.price = -1

    def set_long_summary(self, summary: str):
        self.long_summary = summary

    def set_exchange(self, exchange: str):
        self.exchange = exchange

    def set_price(self, value: float):
        print(value)
        self.price = value