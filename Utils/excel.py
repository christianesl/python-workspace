import openpyxl

def displayExcelContent(file_path):
    work_book = openpyxl.load_workbook(file_path)
    sheet = work_book.active
    cells = sheet['A1':'C50']
    counter = 0

    for name, email, seat in cells:

        if(name.value == "EID"):
            continue

        if(name.value != None):
            counter += 1
            print(f"{name.value} has email: {email.value} and seats at {seat.value}.")
        
    print(f"Total number of employees is: {counter}")
    work_book.close()

if __name__ == "__main__" :
    displayExcelContent('C:\\Users\\christian.saldana\\coding-workplace\\python\\Info.xlsx')