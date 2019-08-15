import csv
import openpyxl
from openpyxl import Workbook

def WriteToCSV(filename, items):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in items:
            writer.writerow([item['title'], item['link']])

def WriteToXLS(filename, items):
    wb = Workbook()
    ws = wb.active
    for i in range(0, len(items)):
        ws.cell(row = i + 1, column = 1, value = items[i]['title'])
        ws.cell(row = i + 1, column = 2, value = items[i]['link'])
    wb.save(filename)
