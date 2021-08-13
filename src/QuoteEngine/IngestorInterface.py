"""Build a ingestor interface backbone."""
from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """
    Define abstract base class IngestorInterface.

    Abstract classes are classes that contain one or more abstract methods.
    Abstract classes cannot be instantiated, and require subclasses to
    provide implementations for the abstract methods.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """To confirm whether can ingest file extensions or not."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Create an abstract method.

        It is a method that is declared, but contains no implementation.
        """
        pass
