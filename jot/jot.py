import re
from typing import Optional, Any
from abc import ABC, abstractmethod
from jot.loader import FileLoaderFactory, FileLoader


class JotGrand(ABC):

    @abstractmethod
    def get(self, key: str, default: Optional[Any] = None):
        """Retrieve a value from the data using dot notation."""
        pass


class Jot(JotGrand):

    def __init__(self, path: str):
        loader: FileLoader = FileLoaderFactory.get(path=path)
        self.data: dict = loader.load()

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

    def format(self, s: str) -> str:
        def replace(match):
            if not s:
                return ''

            keys: list[str] = match.group(1).split('.')
            value_not_found: str = '{' + '.'.join(keys) + '}'
            if len(keys) == 1:
                k: str = keys[0]
                v: str = self.data.get(k, value_not_found)
            elif len(keys) > 1:
                nested_data = self.data.copy()
                for k in keys:
                    try:
                        nested_data = nested_data.get(k, value_not_found)
                        v = nested_data
                    except Exception:
                        v = value_not_found
            return v
        return re.sub(r'\{([\w\.]+)\}', replace, s)
