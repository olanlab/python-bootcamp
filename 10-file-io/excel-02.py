import os
from openpyxl import Workbook

dirname, filename = os.path.split(os.path.abspath(__file__))

wb = Workbook()
sheet = wb.active

sheet.title = "DEMO 2021"

sheet['A1'] = 1
sheet['B1'] = 3
sheet.cell(row=2,column=2).value = 2


wb.save(f"{dirname}/demo.xlsx")
