import sqlite3

from my_finance.stock.persistance_interface import StockPersistanceInterface


class StockSqlPersistance(StockPersistanceInterface):
    def __init__(self, path: str):
        self.path = path

    def get_all(self) -> list[dict]:
        command = "SELECT * FROM stocks;"
        print("Reading all the elements from stocks table ...")
        stocks = self.__execute_command(command)
        return [{
            "ticker": s[0],
            "company": s[1],
            "field": s[2],
            "amount": s[3],
            "longSummary": s[4],
            "exchange": s[5],
            "country": s[6],
            "numberOfEmployees": s[7],
        } for s in stocks]

    def add(self, stock_info: dict):
        command = f"INSERT INTO stocks (ticker, company, field, amount, long_summary, exchange, country, employees) " \
                  f"VALUES ('{stock_info['ticker']}','{stock_info['company']}','{stock_info['field']}',0," \
                  f"'{stock_info['longSummary']}','{stock_info['exchange']}','{stock_info['country']}'," \
                  f"{stock_info['numberOfEmployees']});"
        print("SQL command for add: " + command)
        self.__execute_command(command)

    def remove(self, stock_id: str):
        command = f"DELETE FROM stocks WHERE ticker='{stock_id}'"
        print("SQL command for remove: " + command)
        self.__execute_command(command)

    def __execute_command(self, command: str) -> list:
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute(command)
        info = cursor.fetchall()
        connection.commit()
        connection.close()
        return info