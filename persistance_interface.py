from abc import ABC, abstractmethod


class StockPersistanceInterface(ABC):
    @abstractmethod
    def get_all(self) -> list[dict]:
        pass

    @abstractmethod
    def add(self, stock_info: dict):
        pass

    @abstractmethod
    def remove(self, stock_id: str):
        pass