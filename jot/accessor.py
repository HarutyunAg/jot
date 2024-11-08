import re
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import Optional, Any


class DataAccessor(ABC):
    @abstractmethod
    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a value using dot notation."""
        pass

    def format(self, s: str):
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

    def format(self, s: str) -> str:
        def replace(match):
            if not s:
                return ''
            
            keys: list[str] = match.group(1).split('.')
            value_not_found: str = '{' + '.'.join(keys) + '}'

            # Traverse XML tree based on keys
            nested = self.root
            for key in keys:
                if isinstance(nested, ET.Element):
                    nested = nested.find(key)
                    if nested is None:
                        return value_not_found
                else:
                    return value_not_found

            if nested.attrib:
                last_key = keys[-1]
                if last_key in nested.attrib:
                    return str(nested.attrib[last_key])
            return str(nested.text) if nested is not None else value_not_found
        return re.sub(r'\{([\w\.]+)\}', replace, s)
