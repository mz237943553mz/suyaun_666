import xlrd
# from ddt import ddt,data,unpack
# import unittest
# import time

class Excel1():
    def __init__(self, Excelpath):
        self.data = xlrd.open_workbook(Excelpath)
        self.table = self.data.sheet_by_name("Sheet1")
        # 取第一行的关键词
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNUM = self.table.nrows
        # 获取总列数
        self.colNUM = self.table.ncols

    def login_data(self):
        if self.rowNUM <= 1:
            print("总行数小于1")
        else:
            result = []
            # 按行读取表格内容添加到result列表中，方便调用
            for line in range(self.rowNUM):
                shuju = self.table.row_values(line)
                result.append(shuju)
            print(result)
            return result

# if __name__ == '__main__':
#     aa=Excel1(r"C:\Users\Administrator\Desktop\QQ-Login.xlsx")
#     aa.login_data()
