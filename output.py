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
    # format spreadsheet columns
    ws.column_dimensions['A'].width = 60
    ws.column_dimensions['B'].width = 60
    ws.column_dimensions['C'].width = 60
    for i in range(0, len(items)):
        title_cell = ws.cell(row = i + 1, column = 1, value = items[i]['title'])
        url_cell = ws.cell(row = i + 1, column = 2, value = items[i]['link'])
        url_cell.hyperlink = items[i]['link']
        url_cell.style = 'Hyperlink'
        snippet_cell = ws.cell(row = i + 1, column = 3, value = items[i]['snippet'])
    wb.save(filename)
