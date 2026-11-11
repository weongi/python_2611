import openpyxl
print(openpyxl.__version__)

w1 = openpyxl.Workbook()

ws = w1.active

w1.save('test.xlsx')
