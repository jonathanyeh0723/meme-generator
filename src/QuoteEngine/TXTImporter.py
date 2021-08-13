"""Construct a txt importer."""
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TXTImporter(IngestorInterface):
    """
    Define TXTImporter class.

    The TXTImporter inherits from IngestorInterface class,
    and has a method to ingest a path (string format).
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """To parse a txt format file."""
        if not cls.can_ingest(path):
            raise Exception("Can not ingest txt extensions!")

        cats = []
        with open(path, 'r') as txtfile:
            for line in txtfile:
                # To handle end of line
                if line.startswith('\x0c'):
                    break
                # To handle line, and strip blank line
                if not line.startswith('\n'):
                    parsed = line.strip('\n').split('-')
                    new_cat = QuoteModel(parsed[0], parsed[1])
                    cats.append(new_cat)

            return cats
