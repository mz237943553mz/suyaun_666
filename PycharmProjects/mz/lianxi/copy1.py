import os
import shutil
import xlrd

source_path=os.path.abspath(r"C:\Users\Administrator\Desktop\2000_PCAP")
target_path=os.path.abspath(r"C:\Users\Administrator\Desktop\2000_PCAP_part1")

data=xlrd.open_workbook(r"C:\Users\Administrator\Desktop\name_list.xlsx")
table=data.sheet_by_name("NAME")
list1=[]
a=table.col_values(0)
for i in range(1,len(a)):
    list1.append(str(int(a[i])))
print(list1)

if os.path.exists(source_path):
    for file in os.listdir(source_path):
        print(file)
        for i in list1:
            if (i in file):
                src_file=os.path.join(source_path,file)
                shutil.copy(src_file, target_path)
