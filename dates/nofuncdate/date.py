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

    #checking if the year is valid
    #If the year is written with only two digits, the date lies between 1950 and 2049, so
    #65 means 1965 and 42 means 2042
    if y.isdigit():
      if(len(y)==2):
        if(int(y)>=50):
          y = "19"+y
        else:
          if(int(y) < 50):
            y = "20"+y
    else:
      print(y,"invalid year")
      continue
        
      
  ##Getting the format right for the month
  #checking if the month is valid 
    if m.isdigit():
      if(len(m) == 1):
        m = "0" + m
      elif(len(m)==2):
        m = m
      else:
        print(d,m,y,"<-Invalid input for month")
        continue
    else:
      if m not in months:
        print(d,m,y,"<-Invalid input for month")
        continue
      else:
        for i in range(len(months)):
          if months[i] == m:
            m=(i+1)
            m = str(m)
            m = "0" + m
          
          

     ##formating the day
     #Here we are checking if the the entry for the day is valid
    if(len(d) > 2):
      print(d,m,y,"<-Invalid entry for day")
      continue
    else:
      if len(d) == 1:
          d = "0"+d
      else:
          d = d

    ##whether or not input is a valid date between the years 1753 and 3000,the month 1 and 12 and days 1 and 31.      
    if(1753 <= int(y) <= 3000):
      if(0 < int(m) < 13):
        if(0 < int(d) < 32):
          
          #these months can not have more than 30 days
          #if there is more than 31 days for this month it will pront an invalid message
          if int(m) in [4,6,9,11]:
            if int(d)<=30:
              oldformat = d+m+y
              oldformat = datetime.strptime(oldformat,'%d%m%Y').strftime('%d %b %Y')
              print(oldformat)
            else:
              print(d,m,y, "- INVALID: Days out of range for month yayayay")
              
              #checking for leap year
              #29th of February is only considered a valid date in leap years
              #otherwise it will print an error message
          elif int(y) % 400 == 0 or int(y) % 4 == 0 and int(y) % 100 != 0 : # Every 4 year "Leap" year occures so checking...
            if int(m) == 2: # In "Leap" year February has 29 days
              if int(d) < 30:
                oldformat = d+m+y
                oldformat = datetime.strptime(oldformat,'%d%m%Y').strftime('%d %b %Y')
                print(oldformat)
              else:
                print(d,m,y, "- INVALID: Days out of range for February")

              #If it is not a leap year,February will only have 28 days
          elif int(m) == 2:
                  if(int(d) <29):
                    oldformat = d+m+y
                    oldformat = datetime.strptime(oldformat,'%d%m%Y').strftime('%d %b %Y')
                    print(oldformat)
                  else:
                    print(d,m,y, "- INVALID: Days out of range for February")

               #if it is not a leap year and is not the month of February     
          elif int(y)% 4 != 0 and m != 2:
            oldformat = d+m+y
            oldformat = datetime.strptime(oldformat,'%d%m%Y').strftime('%d %b %Y')
            print(oldformat)
        else:
          print(d,m,y, "- INVALID: Days out of range")#if days are out of range
      else:
        print(d,m,y, "- INVALID: Month out of range")#if month is out of range
    else:
      print(d,m,y," - INVALID: Year out of range.")#if year is not in range
                  


 
  
  
  
