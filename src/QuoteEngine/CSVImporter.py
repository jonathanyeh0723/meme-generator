"""Construct a csv importer."""
import csv
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVImporter(IngestorInterface):
    """
    Define CSVImporter class.

    The CSVImporter inherits from IngestorInterface class,
    and has a method to ingest a path (string format).
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """To parse a csv format file."""
        if not cls.can_ingest(path):
            raise Exception("Can not ingest csv extensions!")

        cats = []
        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                new_cat = QuoteModel(row[0], row[1])
                cats.append(new_cat)

        return cats
