""" We are checking to see which class can be used to parse the
contents of a file, using a for loop iterating over four choices.
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .TextIngestor import TextIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    
    importers = [DocxIngestor, TextIngestor,
                 CSVIngestor, PDFIngestor]
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
