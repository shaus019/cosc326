This submission is for etude # 12 of email. To compile the file please use Python email.py and the file name you want to test it on.
I have used three differnt files for testing my code and am hopefull that it will pass all the test cases.
The code is a bit everywhere so my apologies for that.
To compile:
python3 email.py < email.txt
python3 email.py < bad.txt
python3 email.py < good.txt

It will print out a valid email in lower case with an mailbox name, @ symbol, a domain name, a (".") symbol and a valid domain extension.
If the domain name is given in numeric form it uses ipaddrresses library of python to check that if it is a valid domain name or not.
Only a few domain name extension are considered valid from a list which is given in the etude.
The mailbox name cannot start from any invalid symbols and may have multiple parts seperated by dots.
There is a subtitution for additional security measures which has been replaced. Means "_dot_" has been replaced with "."
and "_at_" has been replace with "@" symbol.

I found the program quite helpful, it was a bit similar to the dates one which took me along time but
this one i have managed to program it a bit quicker than the date one. I have done a lot of research for trying to find functions
which will make ther job easier than doing it kind of manually.
Thankyou Hamza and Stiffanie.
kind regards
Usman shah
