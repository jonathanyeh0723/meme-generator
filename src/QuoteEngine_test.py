"""Import modules."""
from QuoteEngine import DocxImporter, CSVImporter, TXTImporter, PDFImporter
from QuoteEngine import Ingestor
import random

# Unit test for DocxImporter
print(DocxImporter.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
# Unit test for CSVImporter
print(CSVImporter.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
# Unit test for TXTImporter
print(TXTImporter.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
# Unit test for PDFImporter
print(PDFImporter.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))

# Unit test for Ingestor
ext = ['docx', 'csv', 'txt', 'pdf']
choice = random.randrange(0, 4)
path = './_data/DogQuotes/DogQuotes' + ext[choice].upper() + '.' + ext[choice]

print(Ingestor.parse(path))
print(f'Using {path}')
