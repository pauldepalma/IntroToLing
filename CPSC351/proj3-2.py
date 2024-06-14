import sys
import re


def DFA(input):
    print('DFA')
    print(input)

    F = {'111','101','110','100'}
    STATE = '000'
    
    for inp in input:
        STATE = switch(STATE,inp)
    
    if (STATE in F):
        print('True')
    else:
        print('False')


def switch(STATE,inp):
    if STATE == '000':
        if inp == '0':
            return '000'
        elif inp == '1':
            return'001'

    if STATE == '001':
        if inp == '0':
            return '010'
        elif inp == '1':
            return '011'

    if STATE == '011':
        if inp == '0':
            return '110'
        elif inp == '1':
            return '111'

    if STATE == '111':
        if inp == '0':
            return '110'
        elif inp == '1':
            return '111'

    if STATE == '010':
        if inp == '0':
            return '100'
        elif inp == '1':
            return '101'

    if STATE == '101':
        if inp == '0':
            return '010'
        elif inp == '1':
            return '011'

    if STATE == '110':
        if inp == '0':
            return '100'
        elif inp == '1':
            return '101'

    if STATE == '100':
        if inp == '0':
            return '000'
        elif inp == '1':
            return '001'


def REGEX(string):
    print("Regular Expression")
    print(string)
    print(bool(re.search("1[0-1][0-1]$",string)))


def main():
    fin = open("string.txt", 'r')
    string = fin.read().rstrip()
    DFA(string)
    print() 
    REGEX(string)
    fin.close()
  
main()

   


