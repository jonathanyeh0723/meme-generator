#from QuoteEngine import DocxImporter, CSVImporter, TXTImporter, PDFImporter


#print(DocxImporter.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
#print(CSVImporter.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
#print(TXTImporter.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
#print(PDFImporter.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))

from QuoteEngine import Ingestor
import random

ext = ['docx', 'csv', 'txt', 'pdf']
choice = random.randrange(0, 4)
path = './_data/DogQuotes/DogQuotes' + ext[choice].upper() + '.' + ext[choice]

print(Ingestor.parse(path))
print(f'Using {path}')
