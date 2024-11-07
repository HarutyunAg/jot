import re
from typing import Optional, Any
from abc import ABC, abstractmethod
from jot.loader import FileLoaderFactory, FileLoader


class JotGrand(ABC):

    @abstractmethod
    def get(self, key: str, default: Optional[Any] = None):
        """Retrieve a value from the data using dot notation."""
        pass

    def format(self, s: str) -> str:
        """
        Replace placeholders in a string with corresponding values from loaded data.

        This method scans the input string `s` for placeholders in the format `{key.subkey}`, 
        where each placeholder corresponds to a nested key path in the loaded data.
        If a key path does not exist, the placeholder is left unchanged in the string.

        Args:
            s (str):
            The input string containing placeholders to be replaced.

        Returns:
            str:
            The formatted string with placeholders replaced by corresponding values.
            Placeholders with no matching key path remain unchanged.
        """
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
            
            nested = self.data
            for key in keys:
                if isinstance(nested, dict) and key in nested:
                    nested = nested[key]
                else:
                    return value_not_found
            return str(nested)
        return re.sub(r'\{([\w\.]+)\}', replace, s)
