import yfinance
from plotly import graph_objects

ticker = yfinance.Ticker("TSLA")
dataframe = ticker.history("5y")

yesterday_high = dataframe["High"]["2022-03-18"]

print(dataframe)
print(yesterday_high)


# diagram = graph_objects.Figure(
#     graph_objects.Candlestick(
#         x=dataframe.index,
#         low=dataframe["Low"],
#         high=dataframe["High"],
#         open=dataframe["Open"],
#         close=dataframe["Close"],
#     )
# )
#
#
# diagram.show()