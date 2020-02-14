#library that implements regular expressions
#socket and ipaddress libraries to deal with  numeric form of domain
import re
import fileinput
import socket
import ipaddress

#class to check for the validation of email, A valid email should be converted into lowwr case
#and have a format od mailbox name,@ sign, domain name,(".")sign and a domain extension.
class ValidEmail:
        #reading the inputfile 
        for line in fileinput.input():
                #convert the input into lower case and strip the blank space at the end
                lower = line.lower().strip("\n")
                #For additional security mesures, some addresses have replaced @ and . symbols
                #To replace _dot_ with a (.) and _at_ with (@) symbols
                lower = lower.replace("_dot_",".")
                lower = lower.replace("_at_","@")
                #separating mailbox name from the input email
                #global name
                #name = lower.split('@')[0]
                #seperating domain name and extension from the input email
                #global domain
                #domain = lower.split('@')

                def containsInvalid(lower):
                        if "#" in lower:
                                print(lower,"<-Invalid email has a # sign")
                                return -1             
                #this function is going through the mailbox name
                #to make sure it does not start with any invalid symbols
                #and does not have any double symbols in a row
                def mailbox(lower):
                        name = lower.split('@')[0]
                        validsigns = [' ','.','_','-','/']
                        for x in validsigns:
                                i = 1;
                                count = 0;
                                while i < len(name):
                                      if name[i] in validsigns and name[i-1] in validsigns:
                                              count += 1;
                                              if count == 1:
                                                      print(lower," cannot have double dots in the mailbox name")
                                                      return -1
                                              
                                      i += 1
                                if name.startswith(x) == True or name.endswith(x) == True:
                                        print(lower,"start or ends with invalid signs")
                                        return -1

                def startspace(lower):
                        if lower.startswith(' ') == True or lower.endswith(' ') == True:
                                print(lower,"Invalid email starts or ends with space")
                                lower.rstrip()
                                return -1
                                
          #function for checking if there is a space in the email

                def spacecheck(lower):
                        count = 0
                        i = 1;
                        while i < len(lower):
                                if lower[i] == ' ':
                                        count+=1;
                                        
                                        if count > 0:
                                                print(lower,"<-Invalid email has a space in it")
                                                return -1
                                i+=1
                #this function checks the domain name and domain extension
                #checks if the domain name is numeric form, if it is splits it on the bases of square brackets
                #and then checks if the numeric domain is valid or not in try catch block
                #checks if the domain extension is a valid one
                #then checks if the domain name has any invalid symbols

                def domain(lower):
                        domain = lower.split('@')
                        #Domain name could be separated with one of these symbols
                        validsigns = [' ','.','_','-','/','#']
                        #List of valid domain extensions
                        validdomain = ['co.nz','com.au','co.ca','com','co.us','co.uk']
                        #prints an error message if an email is missing @ symbol
                        if "@" not in lower:
                                 print(lower,"<-Missing @ sign")
                #If the email has @ symbol then it will check the other requirements
                        elif "@" in lower:
                                #splits the domain name and extension from the input email
                                domain = lower.split('@')[1]
                                for x in validsigns:
                                        #checks if the domain name starts or ends with an invalid sign from the list valid signs
                                        if domain.startswith(x) == True or domain.endswith(x) == True:
                                                print(lower,"domain start or ends with invalid signs")
                                                return
                                        #checks if the domain name is in numeric form
                                if domain.endswith("]") == True and domain.startswith("[") == True:
                                        numeric = lower.strip("]")
                                        numeric = numeric.split("[")
                                        numeric = numeric[1]
                                        #print(numeric)
                                        #using the ipaddress library to check if the ip is valid or not
                                        try:
                                                ipaddress.ip_address(numeric)
                                        #ip = ipaddress.ip_address(numeric)
                                                print(lower)
                                        except:
                                                print(lower,"<-Invalid ip address")
                                                        

                                else:
                                        counts = 0;
                                        for x in validdomain:
                                                #checks if the the extension used is valid or not
                                                if domain.endswith(x) == True:
                                                        counts += 1;
                                                        #if it is a avlid extension and the lenght of the domain is greater than the domain extension
                                                        #means there is a domain name before the extension
                                                        if counts == 1 and len(domain) > 4:
                                                                #stripping the domain extension from the domain name
                                                                domainname = domain.strip('.'+x)
                                                                #checking if the domain name is valid or not
                                                                #for x in validsigns:
                                                                i = 1;
                                                                count = 0;
                                                                while i < len(domainname):
                                                                        if domainname[i] in validsigns and domainname[i-1] in validsigns:
                                                                                count += 1;
                                                                                if count == 1:
                                                                                        print(lower," cannot have double signs in the domain name")
                                                                                        return
                                                                        i += 1
                                                                print(lower)
                                        #prints an error message if the domain extension is not valid
                                        if counts == 0:
                                                print(lower,"<-Invalid extension")
                               
                #calling the two functions which i have used here
               

                check = startspace(lower)
                if(check==-1):
                        continue
                check = containsInvalid(lower)
                if check == -1:
                        continue
                check = spacecheck(lower)
                if(check==-1):
                         continue
                check = mailbox(lower)
                if(check==-1):
                        continue
                domain(lower)
                                                                
