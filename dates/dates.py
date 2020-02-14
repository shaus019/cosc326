#program for formating dates
from datetime import datetime
import re#library for regular expression
import fileinput
for line in fileinput.input():
    n = re.split("[\/\- ]", line.strip())#to split the input
    def valid_format(n):
        if(len(n)!=3):
            print(n,"invalid input")
            return -1
            #to give the proper index for year, month and day
        else:
            y = n[2]
            m = n[1]
            y = n[0]
            continue


    def year_check(y):
        if y.isdigit():
          if(len(y)==2):
            if(int(y)>=50):
              y = "19"+y
            else:
              if(int(y) < 50):
                y = "20"+y
        else:
            print(y,"invalid year")


    check = valid_format(n)
    if check == -1:
        continue
    check = year_check(y)
    if check == -1:
        continue
