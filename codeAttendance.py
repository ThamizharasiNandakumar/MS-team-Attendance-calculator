# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:29:08 2021

@author: Admin
"""

# Reading an excel file using Python
import pandas as pd
import csv
import codecs
import numpy as np
from datetime import timedelta
import re


def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))


UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}

def convert_to_seconds(s):
    return int(timedelta(**{
        UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
        for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', s, flags=re.I)
    }).total_seconds())


# Give the location of the file E:/Vel Tech/MAD/Attendance-S9+L9/Attendance.xlsx    

loc = ("E:\\Vel Tech\Summer 21-22\\MAD\\Attendance\\Attendance.xlsx")
loc1 = ("E:\\Vel Tech\Summer 21-22\\MAD\\Attendance\\09.08.21-9.45am-Mon.csv")



# To open Workbook
Att = pd.read_excel(loc)
l1 = np.array(Att["Name"])

list2 =[]
list1 =[] 
presentStudents = {}

for i in l1 :
    list1.append(i.strip())
#today = pd.read_csv(loc1, sep = '\t')
with codecs.open(loc1, 'rU','utf-16') as file:
    reader = csv.reader(file)
    next(file)
    for row in reader:
        if row != [] and len(row) > 2:
            time = row[2].split("\t")[1]
            name = row[0].split("\t")[0]
            if name not in presentStudents.keys() :
                presentStudents[name] = convert_to_seconds(time)
            elif name in presentStudents.keys() :
                presentStudents[name] +=convert_to_seconds(time)

for student, duration in presentStudents.items():
    if student in list1 and duration >= 600:
    
        list2.append(student)

print(presentStudents)
l = Diff(list1,list2)
l.sort()
print(l,len(l))
