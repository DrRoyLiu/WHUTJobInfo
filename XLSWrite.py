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

    def save(self, filepath):
        self.xls.save(filepath)
