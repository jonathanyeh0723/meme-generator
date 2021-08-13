"""Construct a docx importer."""
from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxImporter(IngestorInterface):
    """
    Define DocxImporter class.

    The DocxImporter inherits from IngestorInterface class,
    and has a method to ingest a path (string format).
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """To parse a docx format file."""
        if not cls.can_ingest(path):
            raise Exception("Can not ingest docx extensions!")

        cats = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split('-')
                new_cat = QuoteModel(parsed[0], parsed[1])
                cats.append(new_cat)

        return cats
