from pydantic import BaseModel, Field


# TODO create model for adding a stock & a model for getting a stock

class StockModel(BaseModel):
    ticker: str = Field(description="The ticker ID of the stock, for example Tesla has TSLA")
    company: str = Field(default="", description="The full company name, leave empty for POST")
    field: str = Field(default="")
    price: float = Field(default=-1, description="Current price updated in real time")

    class Config:
        orm_mode = True


class StockExtendedModel(StockModel):
    long_summary: str = Field(description="The business summary of the company")
    exchange: str = Field(description="The name of the exchange where the company is listed")
    country: str = Field()
    number_of_employees: str = Field(150)


class DiagramModel(BaseModel):
    tickers: list[str] = Field()
    info: str = Field(default="Close", description="Values: Open, Close, High, Low")
    start_date: str = Field(default="2015-06-01", description="Format: YYYY-MM-DD")
    end_date: str = Field(default=None)