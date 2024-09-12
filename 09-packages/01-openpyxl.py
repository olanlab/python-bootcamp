from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['A1'] = 11

wb.save("example.xlsx")