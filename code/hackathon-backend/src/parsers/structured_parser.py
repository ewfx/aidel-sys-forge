import csv
from io import StringIO

def parse_structured(csvcontents):
    csv_io = StringIO(csvcontents)
    reader = csv.DictReader(csv_io)
    contents = []
    for row in reader:
        contents.append(row)
    return contents