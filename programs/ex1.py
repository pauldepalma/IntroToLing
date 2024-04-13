#ex1.py
#variables and assignment

def main():
    var1 = 112
    var2 = 21

    print("Before")
    print(var1)
    print(var2)

    #assignments
    tmp = var1
    var1 = var2
    var2 = tmp

    print("After")
    print(var1)
    print(var2)

main()
          
