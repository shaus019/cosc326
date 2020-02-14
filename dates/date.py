#program for formating dates
from datetime import datetime
import re#library for regular expression
import fileinput
for line in fileinput.input():
  n = re.split("[\/\- ]", line.strip())#to split the input
  #first check if the input has three values for day, month and year
  if(len(n)!=3):
    print(n,"invalid input")
    #to give the proper index for year, month and day
  else:
    y = n[2]
    m = n[1]
    d = n[0]
    #in case the month is not a number
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    m = m.lower()


    #If the year is written with only two digits, the date lies between 1950 and 2049, so
    #65 means 1965 and 42 means 2042
    def check_year(y):
      if y.isdigit():
        if(len(y)==2) and int(y) != 0:
          if(int(y)>=50):
            y = "19"+y
          else:
            y = "20"+y
        else:
          if(len(y) == 4):
            y = y
      else:
        print(y,"invalid year")
        return -1
        
      
  ##Getting the format right for the month
    def check_month(m):
      mdict = {28: 'feb', 29: 'feb',31: 'jan', 31: 'mar',30: 'apr', 31: 'may', 31: 'aug', 30: 'sep', 31: 'oct', 30:'nov',31:'dec'}
      if m.isdigit():
        if(len(m) == 1):
          m = "0" + m
        elif(len(m)==2):
          m = m
        else:
          print(d,m,y,"invalid input for month")
          return -1
      else:
        if m not in months:
          print(d,m,y,"invalid input for month")
          return -1
        else:
          for i in range(len(months)):
            if months[i] == m:
              m=(i+1)
              m = str(m)
              if(len(m) == 1):
                m = "0" + m
              elif(len(m)==2):
                m = m
              return -1

    #checking the day        
    def check_day(d):
      if(len(d) > 2):
        print(d,m,y,"invalid entry for day")
        return -1
      else:
        if len(d) == 1:
          d = "0"+d
        else:
          d = d


      def validdays(m,d):
        if int(m) == 1 or 3 or 5 or 7 or 8 or 10 or 12:
          print(m)
          if int(d) > 31:
            print(d)
            print(d,m,y, "onvalid days with more thatn 30 days")
            return -1;
        elif int(m) == 4 or 6 or 9 or 11:
          if int(d) > 30:
            print(d,m,y,"invalid month with more than 30 days")
            return -1

          

    ##whether or not input is a valid date between the years 1753 and 3000,the month 1 and 12 and days 1 and 31.
      def valid_date(d,m,y):
      #print(y)
        if(int(y) >=1753 and  int(y) <= 3000):
        #print(y)
          if(0 < int(m) < 13):
            if(0 < int(d) < 32):
              if (int(y) % 4 == 0) or (int(y) % 4 == 0) and (int(y) % 100 != 0): # Every 4 year "Leap" year occures so checking...
                if int(m) != 2: #if it is a leap year and is not the month of february that is where you made the changes
                  if int(m) in [1,3,5,7,8,10,12]:
                    if int(d) <= 31:
                      oldformat = d+m+y
                      oldformat = datetime.strptime(oldformat,'%d%m%Y').strftime('%d %b %Y')
                      print(oldformat)
                    else:
                      print("Invalid days for the month")
                  elif int(m) == [4,6,9,11]:
                    if int(d) <= 30:
                      oldformat = d+m+y
                      oldformat = datetime.strptime(oldformat,'%d%m%Y').strftime('%d %b %Y')
                      print(oldformat)
                    else:
                      print("Invalid days for the month")
                if int(m) == 2: # In "Leap" year February has 29 days
                  if int(d) < 30:
                    oldformat = d+m+y
                    oldformat = datetime.strptime(oldformat,'%d%m%Y').strftime('%d %b %Y')
                    print(oldformat)
                  else:
                    print(d,m,y, "- INVALID: Days out of range for February")
                    return -1
              elif int(m) == 2: # But if it's not "Leap" year February will have 28 days
                      if(int(d) <29):
                        oldformat = d+m+y
                        oldformat = datetime.strptime(oldformat,'%d%m%Y').strftime('%d %b %Y')
                        print(oldformat)
                      else:
                        print(d,m,y, "- INVALID: Days out of range for February")
                        return -1
              elif int(y)% 4 != 0 and m != 2:#if it is not a leap year and is not the month of Februar
                oldformat = d+m+y
                oldformat = datetime.strptime(oldformat,'%d%m%Y').strftime('%d %b %Y')
                print(oldformat)
            else:
              print(d,m,y, "- INVALID: Days out of range")
              return -1
          else:
            print(d,m,y, "- INVALID: Month out of range")
            return -1
        else:
          print(d,m,y," - INVALID: Year out of range.")
          return -1

  
    check = check_year(y)
    if check == -1:
      continue
    check = check_month(m)
    if check == -1:
      continue
    check = check_day(d)
    if check == -1:
      continue
      check = validdays(d,m)
      if check == -1:
        continue
      check = valid_date(d,m,y)
      if check == -1:
        continue
                  


 
  
  
  
