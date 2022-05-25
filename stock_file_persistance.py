import json

from my_finance.stock.persistance_interface import StockPersistanceInterface


class StockFilePersistance(StockPersistanceInterface):
    def __init__(self, path: str):
        self.path = path

    def get_all(self) -> list[dict]:
        print('get all')
        file = open(self.path)
        print('file opened')
        json_items = file.read()
        file.close()
        items = json.loads(json_items)
        return items

    def add(self, stock_info: dict):
        items = self.get_all()
        items.append(stock_info)
        self.__save(items)

    def __save(self, items: list[dict]):
        list_json = json.dumps(items, indent=2)
        file = open(self.path, "w")
        file.write(list_json)
        file.close()

    def remove(self, stock_id: str):
        items = self.get_all()
        items = [i for i in items if i["ticker"] != stock_id]
        self.__save(items)