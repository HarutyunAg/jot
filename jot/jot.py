from typing import Optional, Any
from abc import ABC, abstractmethod
from jot.datasource import DataSource


class JotGrand(ABC):

    @abstractmethod
    def get(self, key: str, default: Optional[Any] = None):
        """Retrieve a value from the data using dot notation."""
        pass


class Jot(JotGrand):

    def __init__(self, data_source: DataSource):
        self.data: dict = data_source.load_data()

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        keys = key.split('.')
        value = self.data

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default

        if isinstance(value, dict):
            raise KeyError(f"Invalid key path: {key}")
        return value
