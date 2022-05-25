import json


class Configuration:
    def __init__(self):
        file = open("my_finance/configuration/config.json")
        contents = file.read()
        file.close()
        print(contents)
        self.conf = json.loads(contents)

    def get_number_of_items_per_page(self) -> int:
        return self.conf["number_of_items_per_page"]

    def get_db_type(self) -> str:
        return self.conf["database"]["type"]

    def get_db_path(self) -> str:
        return self.conf["database"]["path"]