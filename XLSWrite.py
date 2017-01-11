import xlwt


class XLSWrite():
    def __init__(self):
        self.xls = xlwt.Workbook()

    def newSheet(self, sheetName):
        self.sheet = self.xls.add_sheet(sheetName)

    def write(self, x, y, value):
        try:
            self.sheet.write(x, y, value)
        except Exception as e:
            print(x,y,value)
            print(e)

    def write_url(self, x, y, value, name):
    try:
        self.sheet.write(x, y, Formula('HYPERLINK("' + value + '";"' + name + '")'))
    except Exception as e:
        print(x, y, value, name)
        print(e)

    def save(self, filepath):
        self.xls.save(filepath)
