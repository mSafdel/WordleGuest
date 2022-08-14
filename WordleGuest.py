import os
import random
import re

#Wordle Resolver

####################################
####       Draw main menu       ####
####################################
def drawMenu():
    os.system('cls')
    print("********************************\n")
    print("1: First Suggestion")
    print("2: Best Suggestion")
    print("3: Words contain specific letters")
    print("4: Words do not contain specific letters")
    print("5: Complex Search")
    print("9: Exit\n")
    print("********************************")

##############################################
####       Sort func for words list       ####
##############################################
def sorter(e):
    return e[1]

#############################################################
####       Select 5 random word from 100 best word       ####
#############################################################
def select5Random():
    strOut=""
    i1=random.randint(1, 100)
    strOut=str(words[i1])+"\n"

    i2=random.randint(1, 100)
    strOut+=str(words[i2])+"\n"

    i3=random.randint(1, 100)
    strOut+=str(words[i3])+"\n"

    i4=random.randint(1, 100)
    strOut+=str(words[i4])+"\n"

    i5=random.randint(1, 100)
    strOut+=str(words[i5])+"\n"
    
    return strOut

###########################################
####       Initialize Words List       ####
###########################################
def initializeWordsList(wordsList):
    freq='esiarntolcdugpmkhbyfvwzxqj'    
    [w.strip() for w in wordsList]
    wordsList=[word.strip() for word in wordsList if len(word)==6]

    iLen=len(wordsList)
    for i in range(iLen):
        score=0
        for c in wordsList[i]:
            if c in freq:
                score+=freq.index(c)
            else:
                score+=100
        
        wordsList[i]=[wordsList[i],score]
    
    wordsList.sort(key=sorter)
    return wordsList

#######################################
####       Select with Regex       ####
#######################################
def selectedRegexChoices():
    print("Your choice is 2\n")

###########################################################################
####       select words that do not contain the specific letters       ####
###########################################################################
def selectedNotContainWords():
    noLetters=input("Enter your Letters:(seperate with comma): ")
    answerList=[]
    if(len(noLetters)>0):
        noList=noLetters.split(',')
        for w in words:
            wList= [x for x in w[0]]
            check=any(item in wList for item in noList)
            if (check is False):
                answerList.append(w)

    print(answerList)
    iWordCount=len(answerList)
    print(f"{iWordCount} Words found!")

###########################################################################
####       select words that contain the specific letters       ####
###########################################################################
def selectedContainWords():
    containLetters=input("Enter your Letters:(seperate with comma): ")
    answerList=[]
    if(len(containLetters)>0):
        yesList=containLetters.split(',')
        for w in words:
            wList= [x for x in w[0]]
            check=all(item in wList for item in yesList)
            if (check is True):
                answerList.append(w)

    print(answerList)
    iWordCount=len(answerList)
    print(f"{iWordCount} Words found!")


##########################
####       Main       ####
##########################
f=open("words.txt","r")
words=f.readlines()

words=initializeWordsList(words)
drawMenu()
inputChoice=input("Enter your Choice: ")

while(inputChoice!="9"):
    if(inputChoice=="1"):
        print(select5Random())
        input("press any key to continue.....")
    elif(inputChoice=="2") : 
        selectedRegexChoices()
    elif(inputChoice=="3"):
        selectedContainWords()
    elif(inputChoice=="4"):
        selectedNotContainWords()
    else:
        print("Your choice is wrong\n")
    
    drawMenu()
    inputChoice=input("Enter your Choice: ")
