from fastapi import APIRouter

from my_finance.models import StockModel, StockExtendedModel
from my_finance.stock.stock_factory import StockFactory
from my_finance.stock.stock import Stock
from my_finance.stock.stock_repo import StockRepository

stocks_router = APIRouter(prefix="/stocks")
stocks_repo = StockRepository()


@stocks_router.post("")
def add_new_stock(stock_info: StockModel):
    new_stock = StockFactory.make_from_model(stock_info)
    stocks_repo.add(new_stock)


# example if you want to do a tasks app return the list of tasks, and rename the url /items -> /tasks
@stocks_router.get("", response_model=list[StockModel])
def get_stocks(field: str = None, min_employees: int = None, page: int = None, items_per_page: int = None):
    stocks = stocks_repo.get_all()
    if field:
        stocks = [s for s in stocks if s.field == field]
    if min_employees:
        stocks = [s for s in stocks if s.number_of_employees >= min_employees]
    if page is not None and page >= 0:
        # below, it's called a ternary operator
        number_of_items_per_page = items_per_page if items_per_page else conf.get_number_of_items_per_page()
        # page = 0, 0:2
        # page = 1, 2:4
        stocks = stocks[page * number_of_items_per_page:(page + 1) * number_of_items_per_page]
    return stocks


# we can put an id in the URL to select only one resource
@stocks_router.get("/{ticker_id}", response_model=StockExtendedModel)
def get_one_stock(ticker_id: str):
    return stocks_repo.get_by_ticker(ticker_id)




@stocks_router.delete("")
def remove_stock(ticker: str):
    stocks_repo.remove(ticker)