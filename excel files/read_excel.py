import openpyxl

book = openpyxl.load_workbook('data.xlsx')

sheet = book.active

for row in sheet.iter_rows(min_row=1, min_col=1, max_row=10, max_col=5):
	for cell in row:
		print("value " + str(cell.value), end=" ")