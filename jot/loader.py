import json
import toml
import yaml
from typing import Dict
from pathlib import Path
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class FileLoader(ABC):
    def __init__(self, file_path: str):
        self.file_path: Path = Path(file_path)

    @abstractmethod
    def load(self) -> dict:
        """Load and return data from the source."""
        pass


class JSONLoader(FileLoader):
    def load(self) -> Dict:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)


class YAMLoader(FileLoader):
    def load(self) -> Dict:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)


class TOMLLoader(FileLoader):
    def load(self) -> Dict:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return toml.load(f)


class XMLLoader(FileLoader):
    def load(self) -> ET.Element:
        tree = ET.parse(self.file_path)
        return tree.getroot()


class FileLoaderFactory:
    """
    A factory class to create the appropriate file loader based on file extension.

    FileLoaderFactory detects the file type from the file extension and selects the 
    appropriate loader class (JSONLoader, YAMLoader, TOMLLoader, or XMLLoader) to 
    load the file content.
    
    If an unsupported file type is provided, it raises a ValueError,
    ensuring only compatible file formats are used.

    Attributes:
        loaders (dict):
        A dictionary mapping file extensions to their corresponding 
        loader classes.

    Methods:
        get(path: str) -> FileLoader:
            Returns an instance of the appropriate FileLoader subclass based on 
            the file extension of the given path.
    """
    loaders = {
        '.json': JSONLoader,
        '.yaml': YAMLoader,
        '.yml': YAMLoader,
        '.toml': TOMLLoader,
        '.xml': XMLLoader
    }

    @staticmethod
    def get(path: str) -> FileLoader:
        for ext, loader_class in FileLoaderFactory.loaders.items():
            if path.endswith(ext):
                return loader_class(path)
        raise ValueError("Unsupported file type. Only JSON, YAML, TOML, and XML are supported.")
