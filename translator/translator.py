import sys
# -*- coding: latin-1 -*-
""" a program that translating simple sentences of English into Maori """
__author__ = "Orlando Yuan, Usman Shah"

class Translator:
    
    #creating dictionaries of verbs
    global verb_trans
    verb_trans = {
            'go': "haere", 'went': "haere", 'going': "haere", 'goes': "haere",
            'make': "hana", 'made': "hana", 'making': "hana",
            'see': "kite", 'saw': "kite", 'seeing': "kite",
            'want': "hiahia", 'wanted': "hiahia", 'wanting': "hiahia",
            'call': "karanga", 'called': "karanga", 'calling': "karanga",
            'ask': "pātai", 'asked': "pātai", 'asking': "pātai",
            'read': "pānui", 'reading': "pānui",
            'learn': "ako", 'learnt': "ako", 'learning': "ako"}


    #function that working on tense
    def tenseDetector(self, raw_txt):
        #split input
        self.parts = raw_txt.lower().split(" ")
        #a sentence must be at least 2 words
        if len(self.parts) < 2:
            print ("invalid sentence")
            return
        
        self.noun = self.parts[0]
        self.verb = self.parts[len(self.parts) - 1]
        
        
        #initialize
        present_indicator = "ing"
        future_indicator = "will"
        past_indicator = "ed"
        special_past = ["went", "made", "read", "saw", "learnt"]

        for item in self.parts:
            #detect the future tense
            if len(self.parts) == 3:
                if future_indicator in self.parts[1]:
                    print("Ka ", end = '')
                    #if is valid call next function
                    self.verbTranslator()
                    break
                # present -ing
                elif present_indicator in self.verb:
                    print("Kei te ", end = '')
                    #if is valid call next function
                    self.verbTranslator()
                    break
                else:
                    print ("invalid sentence")
                    break
            #detect the past tense
            elif len(self.parts) >= 2 and len(self.parts) <= 4:
                if self.verb.endswith(past_indicator) or self.verb in special_past:
                    print("I ", end = '')
                    #if is valid call next function
                    self.verbTranslator()
                    break
                # present eg. I go
                elif self.verb in verb_trans:
                    print("Kei te ", end = '')
                    #if is valid call next function
                    self.verbTranslator()
                    break
                else:
                    #print error message
                    print("invalid sentence")
                    break
            #detect the present with incl or excl
            elif len(self.parts) > 2 and present_indicator in self.verb:
                print("Kei te ", end = '')
                #if is valid call next function
                self.verbTranslator()
                break
            #if the len(self.parts) < 2
            else:
                #print error message
                print("invalid sentence")
                break

 

    #function that working on self.verb translation
    def verbTranslator(self):
        #compare input with list
        for item in verb_trans:
            if self.verb in verb_trans:
                print (verb_trans[self.verb] + " ", end = '')
                #if is valid call next function
                self.nounTranslator()
                break
            else:
                #print error message
                print (" ")
                print ("unknown verb: " + self.verb)
                break



    #function that working on self.noun translation
    def nounTranslator(self):
        oneP = {'i': "au", 'you': "koe", 'he': "ia", 'she': "ia"}
        twoP_incl = {'we': "taua", 'you': "korua", 'they': "raua"}
        twoP_excl = {'we': "maua", 'you': "korua", 'they': "raua"}
        threeP_incl = {'we': "tatou", 'you': "koutou", 'they': "ratou"}
        threeP_excl = {'we': "matou", 'you': "koutou", 'they': "ratou"}

        #if the input in five lists
        for item in oneP, twoP_incl, twoP_excl:
            #if the string input has more than 3 words
            if len(self.parts) >= 3 and '(' in self.parts[1]:
                num = self.parts[1].split('(')
                exOrIn = self.parts[2]
                #print (num)
                #if is two people
                if int(num[len(num) - 1]) == 2:
                    #print (int(num[len(num) - 1]))
                    #inclusive
                    if exOrIn == "incl)":
                        print(twoP_incl[self.noun])
                        break
                    #exclusive
                    elif exOrIn == "excl)":
                        print(twoP_excl[self.noun])
                        break
                #if is three or more people
                elif int(num[len(num) - 1]) >= 3:
                    #inclusive
                    if exOrIn == "incl)":
                        print(threeP_incl[self.noun])
                        break
                    #exclusive
                    elif exOrIn == "excl)":
                        print(threeP_excl[self.noun])
                        break
                #if is neither 2 nor 3 more
                else:
                    print (" ")
                    print ("unknown noun1: " + self.noun)
                    break
            #if the string input has less than 3 words
            else:
                #if in the dictionary
                if self.noun in oneP:
                    print (oneP[self.noun])
                    break
                else:
                    print (" ")
                    print ("unknown noun2: " + self.noun)
                    break

#build the class
object = Translator()

try:
    #looping
    while True:
        #read user input
        raw_text = input()
        #execute
        object.tenseDetector(raw_text)
except:
    pass

