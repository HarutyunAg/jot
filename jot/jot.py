from typing import Optional, Any
from jot.datasource import FileDataSource


class Jot:

    def __init__(self, data_source: FileDataSource):
        self.data: dict = data_source.load_data()

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a value from the data using dot notation."""
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
