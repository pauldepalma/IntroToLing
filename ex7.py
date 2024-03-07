#ex7.py
#A simple function
import random as rand

def main():
  NUM = 5
  rands = []

  for i in range(NUM):
    rands.append(rand.randint(0,NUM))
    
  print(rands)

  #Invoke function with two parameters
  total = sum(rands,NUM)
  print("Sum = " + str(total))

#This is a called a function. 
def sum(rands,NUM):
  total = 0
  for i in range(NUM):
    total = total + rands[i]
  return total

main()
    
