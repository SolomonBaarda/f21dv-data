from qgis.core import *
from qgis.gui import *
import csv

@qgsfunction(args='auto', group='Custom')
def load_from_csv(value, feature, parent):
    with open('C:\\Users\\Solom\\Downloads\\DataZoneLookup.csv', encoding='windows-1252') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == value:
                return row[6]

