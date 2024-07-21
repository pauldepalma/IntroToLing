#This is a comment
# ex5.py
# decision within a loop

def main():

  tired = False
  
  while (not tired):
    var1 = int(input("Enter an integer\n"))
    var2 = int(input("Enter another integer\n"))

    if var1 > var2:
      print("The first number is greater than the second number")
    else:
      print("The second number is greater than the first number")
    
    more = input("Are you tired? (y/n)\n")
    if more == 'y':
      tired = True

  print ("AI in action")
  print("Mi dispiace, non sei più tired")  


main()
