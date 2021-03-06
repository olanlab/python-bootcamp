from openpyxl import Workbook


wb = Workbook()
sheet = wb.active

sheet.title = "DEMO 2021"

sheet['A1'] = 1
sheet.cell(row=2,column=2).value = 2

wb.save('demo.xlsx')
