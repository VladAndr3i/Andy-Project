import yfinance
from plotly import graph_objects
from matplotlib import pyplot
import random

from my_finance.models import DiagramModel


def show_simple_diagram(ticker_id: str, info: str = "Close", interval: str = "3y"):
    dataframe = __get_the_data_frame(interval, ticker_id)
    # draw the plot/figure/diagram
    scatter = graph_objects.Scatter(x=dataframe.index, y=dataframe[info])
    diagram = graph_objects.Figure([scatter])
    diagram.show()


def create_and_save_to_file(model: DiagramModel):
    dataframe = yfinance.download(model.tickers, start=model.start_date, end=model.end_date)
    figure, axis = pyplot.subplots(figsize=(16, 9))
    for key in dataframe[model.info]:
        axis.plot(dataframe[model.info].index, dataframe[model.info][key])
    pyplot.title(f"{'-'.join(model.tickers)} stock price evolution")
    pyplot.xlabel("Date")
    pyplot.ylabel("Price")
    axis.legend(dataframe[model.info].columns.values)
    pyplot.savefig(f"./stock/diagram/diagram_nr_{random.randrange(1000, 9999)}")


def __get_the_data_frame(interval, ticker_id):
    tsla = yfinance.Ticker(ticker_id)
    dataframe = tsla.history(interval)
    dataframe.reset_index()
    return dataframe