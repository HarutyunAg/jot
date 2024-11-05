import json
from typing import Any, Dict
from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def load_data(self) -> Dict[str, Any]:
        """Load and return data from the source."""
        pass


class FileDataSource(DataSource):

    def __init__(self, file_path: str):
        self.file_path: str = file_path

    def load_data(self) -> Dict[str, Any]:
        """Load JSON data from a file."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
