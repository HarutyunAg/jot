import re
from typing import Optional, Any
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from jot.loader import FileLoaderFactory, FileLoader
from jot.accessor import DataAccessor, DictAccessor, XMLAccessor


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
        loader: FileLoader = FileLoaderFactory.get(path)
        self.data = loader.load()
        self.__accessor: DataAccessor = self.__init_accessor()

    def __init_accessor(self):
        if isinstance(self.data, dict):
            return DictAccessor(self.data)
        elif isinstance(self.data, ET.Element):
            return XMLAccessor(self.data)
        else:
            raise ValueError("Unsupported data format")

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.__accessor.get(key, default)

    def format(self, s: str) -> str:
        return self.__accessor.format(s)
