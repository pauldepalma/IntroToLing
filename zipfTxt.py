'''
Demonstrates Zipf's law for written language
Plots
1) rank against frequency (rank as a function of frequency) or vice-versa
   (if the x and y axis data are shifted)
2) log frequency against log rank or vice-versa
3) Displays table r, f, r x f, word for
  r = 1 - 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 2000,
      3000, 4000, 5,000, 10,000, 20,000
4) Writes r, f, r X f, word for all ranks.  The file name is the same name
as the corpus but with the extension .out
5) Computes statistical data for r x f and r x f x 10
  
For any text corpus input is:
full path plus file name of corpus
'''

import matplotlib.pyplot as plt
import re
import string
import math
import statistics
#from nltk.tokenize import word_tokenize
#import keyboard

def getData(fname):
    fin = open(fname, 'r')
    text = fin.read()  #read in text as a string
    fin.close()
    return text

def tokenize(text):

    #discover non-ascii characters
    #Project Gutenberg uses lots of them
    dict = {ord(ch) : ch for ch in text if ord(ch) > 127}
    nonAscii = ''.join(list(dict.values()))

    #NLTK tokenizer
    #word_lst = word_tokenize(text)

    #splitting on white space works fine
    word_lst = text.split()

    #characters to be removed from the text
    remove = string.digits + string.punctuation + nonAscii
    
    #map characters to be removed(key) to 'None'(value)
    #empty params indicate key/value pairs are implicit in remove
    table = str.maketrans('','',remove)
    
    #for each word, if the character is found, substitue 'None'
    word_lst = [w.translate(table) for w in word_lst]

    #Remove empty words from the list
    word_lst = [word for word in word_lst if len(word) > 0]
   
    #In the index that Zipf used, only capitalization for 
    #proper nouns was retained.  This would distinguish between
    #the rare word used as a proper noun, "Reed" and "reed" for 
    #example.  
    #Transform to lower case
    word_lst = [word.lower() for word in word_lst]

    #Remove invalid single letter words from list:
    word_lst = [word for word in word_lst if len(word) > 1 or
                word == 'i' or word == 'a']
    
    return word_lst


def count_words(word_lst):
    word_dict = {}
    for word in word_lst:
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    return word_dict
            
def make_lst(word_dict):
    #Turn dictionary into a list of tuples:[(word,freq)]
    lst = [(word,word_dict[word]) for word in word_dict.keys()]
    print(lst)
    print()
    #sort list by frequency in reverse order
    lst.sort(key = lambda tuple: tuple[1],reverse=True)
    print(lst)
    quit()
    #insert a rank, starting at 1: [(rank,word,freq)]
    rank_word_freq = [tuple([index] + list(item)) for index, item in enumerate(lst,1)]

    #FORMAT [rank, word, frequency)
    return rank_word_freq


def write_data(rank_word_freq,file_name,numWords): 
    #format: [rank, word, freq]
    firstOcc = True
    for item in rank_word_freq:
        if item[2] < 50 and firstOcc:
            print("First Rank with < 50 occurences: " + str(item[0]))
            firstOcc = False
        if item[2] == 1:
            print("First Rank of Word Used Once:  " + str(item[0]))
            break
        
    t = "\t\t"

    if (len(rank_word_freq)) < 50:
        print("There must be at least 50 word types in the corpus")
        quit()
    
    #Ranks from Zipf's table, p. 24
    tbl = [10,20,30,40,50,100]
    if len(rank_word_freq) >= 200:
        tbl.append(200)
    if len(rank_word_freq) >= 300:
        tbl.append(300)
    if len(rank_word_freq) >= 400:
        tbl.append(400)
    if len(rank_word_freq) >= 500:
        tbl.append(500)
    if len(rank_word_freq) >= 1000:
        tbl.append(1000)
    if len(rank_word_freq) >= 2000:
        tbl.append(2000)
    if len(rank_word_freq) >= 3000:
        tbl.append(3000)
    if len(rank_word_freq) >= 4000:
        tbl.append(4000)
    if len(rank_word_freq) >= 5000:
        tbl.append(5000)
    if len(rank_word_freq) >= 10000:
        tbl.append(10000)
    if (len(rank_word_freq)) >= 20000:
        tbl.append(20000)
    if (len(rank_word_freq)) != 20000:
        tbl.append(len(rank_word_freq))
    
    #all ranks (used for testing the tokenizer)
    #tbl = [item[0] for item in rank_word_freq]
    
    #Display selected data on screen
    print("Rank" + t + "Freq" + t + "R X F" + t + "Word")
    for index in tbl:
        item = rank_word_freq[index-1] #b.c. rank 1 is at position in tbl
        #0 and so on
        line = str(item[0]) + t + str(item[2]) + t + str(item[0] * item[2]) + t + item[1]
        print(line)

    #Write all data to file
    line = line + '\n'
    fn = file_name + '.out'
    fout = open(fn, 'w')
    fout.write("Rank" + t + "Freq" + t + "Prob" + t + t + t + "R X F" + t + "Word\n")
    for item in rank_word_freq:
        line = str(item[0]) + t + str(item[2]) + t + str(item[2]/numWords) + t + t + str(item[0] * item[2]) + t + item[1] + '\n'
        fout.write(line)
    fout.close()
    
    #Write cs file
    fn1 = file_name + '.csv'
    fout1 = open(fn1, 'w')
    for item in rank_word_freq:
        line1 = str(item[0]) + "," + str(item[2]) + '\n' 
        fout1.write(line1)
    fout1.close()

def computeStats(rank_word_freq):
    #format: [rank,word,freq]

    #list of Zipf's constant, RxF
    C0 = [item[0] * item[2] for item in rank_word_freq]
    C1 = [item[0] * item[2] for item in rank_word_freq if item[2] > 10]
    lsts = (C0,C1)

    print()
    lists = 0
    print("Data for all words")
    for C in lsts:
        maximum = str(max(C))
        minimum = str(min(C))
    
        #Python statistics package functions
        median = str(statistics.median(C))
        mean = statistics.mean(C)
        mean = str(float("{:.2f}".format(mean)))   #2 decimal places
        stdev = statistics.stdev(C)
        stdev = str(float("{:.2f}".format(stdev))) #2 decimnal places
                
        print("R X F Data")
        print("Max: " + maximum)
        print("Min: " + minimum)
        print("Mean: " + mean)
        print("Median: " + median)
        print("Standard Deviation: " + stdev)
        print()
        lists = lists + 1
        if lists == 1:
            print("Data omitting words with frequency <= 10 ")

    print()
    
    for C in lsts:
        size = [item * 10 for item in C]
        mean = statistics.mean(size)
        mean = str(float("{:.2f}".format(mean)))   #2 decimal places
        if lists == 0:
            print("Mean of r x f x 10 for all words: " + str(mean))
        if lists == 1:
            print("Mean of r x f x 10, omitting words with frequency <= 10 " + str(mean))
        lists = lists + 1

    print()

def plots(rank_word_freq):
    plotRF = input("Display Data Plot? Y/N?\n")
    plotLogRF = input("Display Log Data Plot? Y/N\n")
    if plotRF == 'Y' or plotLogRF == 'Y':
        print("Lowest Rank is: " + str(len(rank_word_freq)))
        low = int(input("Enter lowest rank to include\n"))

    #using Frequency

    if plotRF == 'Y':
        RFX = [item[0] for item in rank_word_freq if item[0] <= low]
        RFY = [item[2] for item in rank_word_freq if item[0] <= low]
        doPlot(RFX,RFY,"Rank","Frequency")
        #doPlot(RFY,RFX, "Frequency", "Rank (Most Frequent to Least Frequent)")

    '''
    #using Probablity
    if plotRF == 'Y':
        RFX = [item[0] for item in rank_word_freq if item[0] <= low]
        RFY = [item[2]/numWords for item in rank_word_freq if item[0] <= low]
        doPlot(RFX,RFY,"Rank","Probability")
        #doPlot(RFY,RFX, "Probability", "Rank (Most Probable to Least Probable)")
    '''
        
    if plotLogRF == 'Y':
        LRFX = [math.log(item[0]) for item in rank_word_freq if item[0] <= low]
        LRFY = [math.log(item[2]) for item in rank_word_freq if item[0] <= low]
        doPlot(LRFX,LRFY,"Log Rank","Log Frequency")
        #doPlot(LRFY,LRFX,"Log Frequency","Log Rank")

def doPlot(RFX,RFY,xlabel,ylabel):
    ax1 = plt.subplot(1,1,1)
    ax1.plot(RFX,RFY)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    plt.show()
    
def main():

    #get data
    file_name = input("enter file name ")
    text = getData(file_name)

    #tokenize
    word_lst = tokenize(text) 

    #count words
    word_dict = count_words(word_lst) 
    
    #create a list of words and their frequencies ordered by rank
    #[(r1,w1,f1), ... (rn,wn,fn)]
    rank_word_freq = make_lst(word_dict)

    if input("Display and Print Ranks, Words, Freqs? Y/N\n") == 'Y':   
        #display Zipf's ranks on screen
        #write list to a file
        numWords = len(word_lst)
        #print("Word Tokens: " + str(numWords))
        #print("Word Types: " + str(word_dict.keys()))
        write_data(rank_word_freq,file_name,numWords)
        #Compute stats to assess accuracy of Zipf's prediction that RxF is ~constant
        #computeStats(rank_word_freq)

    #Zipfian Distribution Plots

<<<<<<< HEAD
    plots(rank_word_freq)
=======
    plots(rank_word_freq,numWords)
>>>>>>> cb05900bec9b1179d35edd04c2ba5aceba5f4eb9
    
        
    
main()
