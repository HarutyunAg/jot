import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import Optional, Any


class DataAccessor(ABC):
    @abstractmethod
    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a value using dot notation."""
        pass


class DictAccessor(DataAccessor):
    def __init__(self, data: dict):
        self.data = data

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        keys = key.split('.')
        value = self.data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value


class XMLAccessor(DataAccessor):
    def __init__(self, root: ET.Element):
        self.root = root

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        keys = key.split('.')
        element = self.root
        for k in keys:
            element = element.find(k)
            if element is None:
                return default
        return element.text if element.text is not None else default
