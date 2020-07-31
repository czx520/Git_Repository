# -*- coding:utf-8 -*-
# @Time:2020/7/30 11:02
# @Author:whweia
# @File:read_excel.py

import xlrd


class ExcelUtil(object):
    def __init__(self, excelPath, sheetname):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print('总行数小于1')
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):                  # 遍历取值，将每个key与他们的值对应
                s = {}
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)          # 将每行的key=value放入字典
                j+=1                 # 下一行
            return r


# 调试
if __name__ == '__main__':
    filepath = 'testdata.xlsx'
    sheetName = 'Sheet1'
    data = ExcelUtil(filepath, sheetName)            # 实例化
    # print(data)
    print(data.dict_data())
    print(type(data.dict_data()))
