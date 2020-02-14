
This program takes a line of user input for each time, translating English sentences into Maori.
We build several dictionaries to store and map words in two different language.

There are one problem of this program needed to mention:
1) It cannot detect 'read' is in the past tense or the present tense

#How to run
1. using $python3 translator.py 
   either type in sentences by hand line by line without restart the program, 
   or copy & paste multiple lines as the input (should leave a blank line at the end)
2. using $python3 translator.py < test.txt (or the name of any input file)
   (still should leave a blank line at the end of the file)




#testing1 (copy & paste multiple lines with one empty line at the end)
We (3 excl) are going
I am going
They (2 excl) are reading
You (2 incl) are reading
I went
I will go
gibberish
We are coming
Kei te haere matou
Kei te haere au
Kei te panui raua
Kei te panui korua
I haere au
ka haere au
invalid sentence
Kei te  
unknown verb: coming


#testing2 (input lines one by one)
he goes 
Kei te haere ia
she read
I panui ia
they (10 excl) learnt
I ako ratou
they (2 incl) made  
I hana raua
you (8 incl) asked
I patai koutou
we (2 excl) will going
Kei te haere maua
we (5 incl) will making 
Kei te hana tatou
les poete maudit
invalid sentence
est-ce que tu peux voir
invalid sentence
labyrinthian 
invalid sentence

#testing3 (from file, see attachment)
Kei te haere matou
Kei te haere au
Kei te panui raua
Kei te panui korua
I haere au
ka haere au
invalid sentence
Kei te  
unknown verb: coming
Kei te haere ia
invalid sentence
I panui ia
invalid sentence
I ako ratou
I hana raua
I patai koutou
invalid sentence
Kei te haere maua
invalid sentence
Kei te hana tatou