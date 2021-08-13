"""Construct a pdf importer."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

import os
import subprocess
import random


class PDFImporter(IngestorInterface):
    """
    Define PDFImporter class.

    The PDFImporter inherits from IngestorInterface class,
    and has a method to ingest a path (string format).
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """To parse a pdf format file."""
        if not cls.can_ingest(path):
            raise Exception("Can not ingest pdf extensions!")

        if not os.path.exists('./tmp'):
            try:
                os.mkdir('./tmp')
            except Exception as e:
                print(e)

        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, 'r')
        cats = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_cat = QuoteModel(parsed[0], parsed[1])
                cats.append(new_cat)

        file_ref.close()
        os.remove(tmp)

        return cats
