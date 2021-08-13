"""Import built modules."""
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .TXTImporter import TXTImporter
from .PDFImporter import PDFImporter


class Ingestor(IngestorInterface):
    """
    Define Ingestor class.

    It inherits from IngestorInterface class,
    and has a method to ingest a path with strategy.
    """

    ingestors = [DocxImporter, CSVImporter, TXTImporter, PDFImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """To parse a docx/csv/txt/pdf format file."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
