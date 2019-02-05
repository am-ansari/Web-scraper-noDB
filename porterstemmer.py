# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 20:16:38 2018

@author: Abdullah
"""
import re
import numpy as np

vowel = ['a','e','i','o','u','y']

# method to fetch the measure value of a string (# of VCs sequences)
def getMeasure(word):
    
    m = 0
    vCheck = False
    yCheck = ""
    word = word.lower()
    for i in range(len(word)):
        if word[i] in vowel:
            if (word[i] == 'y' and yCheck not in vowel) or word[i] != 'y':
                vCheck = True
            continue
        elif word[i] not in vowel:
            if vCheck == True:
                m += 1
                vCheck = False
        else:
            m = 0
        yCheck = word[i] 
   
    return m           

def step1a(string):
    
    string = string.lower()
    if len(string) > 3:
        if string.endswith("sses"): 
            return string[:-4]+"ss"
        elif string.endswith("ies"): 
            return string[:-3]+"i"
        elif string.endswith("ss"): 
            return string
        elif string.endswith("s"): 
            return string[:-1]+""
        else:
            return string
    else:
         return string

def checkCVC(string):
    if string[-3:-2] not in vowel and string[-1:] not in vowel  and string[-2:-1] in vowel and string[-1:] not in ['x','w','y']:
        return True
    else:
        return False


def step1b(string):
    string = string.lower()
    newString = ""
    substr    = ""
    if string.endswith("eed") and getMeasure(string[:-3]) > 0:
        newString = string[:-3]+"ee"
    elif string.endswith("ed") and re.search('[aeiou]',string[:-2]) != None:
        substr = string[:-2]
    elif string.endswith("ing") and re.search('[aeiou]',string[:-3]) != None:
        substr = string[:-3]
    else:
        newString = string
    
    if len(substr) > 0:
        if (substr[-2:] in ['at','bl','iz']) or (getMeasure(substr) == 1 and  checkCVC(substr) == True):
                newString = substr + "e"
        elif substr[-2:-1]==substr[-1:] and substr[-1:] not in ['l','s','z']:
            newString = substr[:-1] 
        else:
            newString = substr
    else:
         newString = string       
    
    return newString

def step1c(string):
    if string.endswith("y") and re.search('[aeiou]',string[:-1]) != None:
        return string[:-1] + "i"
    else:
        return string

def step2(string):
    
    newStr = string
    if getMeasure(string) > 0:
        arr = np.array([['ational','ate'],
                        ['tional','tion'],
                        ['enci','ence'],
                        ['anci','ance'],
                        ['izer','ize'],
                        ['abli','able'],
                        ['alli','al'],
                        ['entli','ent'],
                        ['eli','e'],
                        ['ousli','ous'],
                        ['ization','ize'],
                        ['ation','ate'],
                        ['ator','ate'],
                        ['alism','al'],
                        ['iveness','ive'],
                        ['fulness','ful'],
                        ['ousness','ous'],
                        ['aliti','al'],
                        ['iviti','ive'],
                        ['biliti','ble']
                        ])

        for i in range(arr.shape[-2]):
            if string.endswith(arr[i][0]):
                newStr = string.replace(arr[i][0],arr[i][1])
                break
            else:
                continue
    return newStr 

def step3(string):
    
    newStr = string
    if getMeasure(string) > 0:
        arr = np.array([['icate','ic'],
                        ['ative',''],
                        ['alize','al'],
                        ['iciti','ic'],
                        ['ical','ic'],
                        ['ful',''],
                        ['ness','']
                        ])
    
        for i in range(arr.shape[-2]):
            if string.endswith(arr[i][0]):
                newStr = string.replace(arr[i][0],arr[i][1])
                break
            else:
                continue
    return newStr          

def step4(string):
    
    newStr = string
    if getMeasure(string) > 1:
        arr = np.array([['al',''],
                        ['ance',''],
                        ['ence',''],
                        ['er',''],
                        ['ic',''],
                        ['able',''],
                        ['ible',''],
                        ['ant',''],
                        ['ement',''],
                        ['ment',''],
                        ['ent',''],
                        ['sion',''],
                        ['tion',''],
                        ['ou',''],
                        ['ism',''],
                        ['ate',''],
                        ['iti',''],
                        ['ous',''],
                        ['ive',''],
                        ['ize','']
                        ])
    
        for i in range(arr.shape[-2]):
            if string.endswith(arr[i][0]):
                newStr = string.replace(arr[i][0],arr[i][1])
                break
            else:
                continue
    return newStr   

def step5a(string):

    measure = getMeasure(string[:-1])
    if string.endswith('e') and ((measure > 1) or (measure == 1 and checkCVC(string[:-1]) == False)):
        return string[:-1]
    else:
        return string 

def step5b(string):

    if getMeasure(string) > 1 and string[-2:-1] == string[-1:]:
        return string[:-1]
    else:
        return string

def getStem(word) :
    
    #for i in range(len(wordArr)):

    step11 = step1a(word)
    step12 = step1b(step11)
    step13 = step1c(step12)
    step2s = step2(step13)
    step3s = step3(step2s)
    step4sa = step4(step3s)
    step4sb = step4(step4sa)
    step5as = step5a(step4sb)
    final = step5b(step5as)
        
    #arr.append(final)
            
    return final

