
class Translator:

   #read users input
   raw_txt = input("Please type in an English sentence: ")
   #split the input and set it global
   global parts
   parts = raw_txt.lower().split(" ")
   #initialize noun and set it global
   global noun
   noun = parts[0]
   #initialize verb and set it global
   global verb
   verb = parts[len(parts) - 1]

   #creating dictionaries
   global verb_trans
   verb_trans = {
           'go': "haere", 'went': "haere", 'going': "haere",
           'make': "hana", 'made': "hana", 'making': "hana",
           'see': "kite", 'saw': "kite", 'seeing': "kite",
           'want': "hiahia", 'wanted': "hiahia", 'wanting': "hiahia",
           'call': "karanga", 'called': "karanga", 'calling': "karanga",
           'ask': "patai", 'asked': "patai", 'asking': "patai",
           'read': "panui", 'reading': "panui",
           'learn': "ako", 'learnt': "ako", 'learning': "ako"}

   #function that working on tense
   def tenseDetector():
       present_indicator = "ing"
       future_indicator = "will"
       past_indicator = "ed"
       special_past = ["went", "made", "read", "saw", "leart"]

       for item in parts:
           #detect the future tense
           if len(parts) == 3:
               if future_indicator in parts[1]:
                   print("ka")
                   break
               # present -ing
               elif present_indicator in verb:
                   print("Kei te")
                   break
           #detect the past tense
           elif len(parts) == 2:
               if verb.endswith(past_indicator) or verb in special_past:
                   print("I")
                   break
               # present eg. I go
               elif verb in verb_trans:
                   print("Kei te")
                   break
               else:
                   print("invalid input: not a valid sentence")
                   break
           #detect the present with incl or excl
           elif len(parts) > 2 and present_indicator in verb:
               print("Kei te")
               break
           #if the len(parts) < 2
           else:
               print("invalid sentence")
               break



   #function that working on verb translation
   def verbTranslator():
       
       #print (verb_trans['going'])
       for item in verb_trans:
           if verb in verb_trans:
               print (verb_trans[verb])
               break
           else:
               print ("unknown verb: " + verb)
               break

   #function that working on noun translation
   def nounTranslator():
       oneP = {'i': "au", 'you': "koe", 'he': "ia", 'she': "ia"}
       twoP_incl = {'we': "taua", 'you': "korua", 'they': "raua"}
       twoP_excl = {'we': "maua", 'you': "korua", 'they': "raua"}
       threeP_incl = {'we': "tatou", 'you': "koutou", 'they': "ratou"}
       threeP_excl = {'we': "matou", 'you': "koutou", 'they': "ratou"}

       #if the input in five lists
       for item in oneP, twoP_incl, twoP_excl:
           #if the string input has more than 3 words
           if len(parts) > 3:
               num = parts[1]
               exOrIn = parts[2]
               #if is two people
               if num[len(num) - 1] == "2":
                   #inclusive
                   if exOrIn == "incl)":
                       print(twoP_incl[noun])
                       break
                   #exclusive
                   elif exOrIn == "excl)":
                       print(twoP_excl[noun])
                       break
               #if is three or more people
               elif num[len(num) - 1] == "3":
                   #inclusive
                   if exOrIn == "incl)":
                       print(threeP_incl[noun])
                       break
                   #exclusive
                   elif exOrIn == "excl)":
                       print(threeP_excl[noun])
                       break
               #if is neither 2 nor 3 more
               else:
                   print ("unknown noun: " + noun)
                   break
           #if the string input has less than 3 words
           else:
               #if in the dictionary
               if noun in oneP:
                   print (oneP[noun])
                   break
               else:
                   print ("unknown noun: " + noun)
                   break



   while True:
       if len(parts) >= 2:
           print ('translated result in Maori: ')
           tenseDetector(). verbTranslator()
          
           nounTranslator()
           break
       else:
           print ("invalid sentence")
           break
