# Python3 Program to print johnite Pattern
if __name__ == '__main__':
 
    alien = 4
    space = '*'
 
    for i in range (1, 6):
 
        # For printing the alien
        for motu in range(alien, 0, -1):
            print(end = " ")
 
        # For printing the *
        for patlu in range(1, i + 1):
            print(space, end = "")
 
        for john in range(1, i):
         
            if (i == 1):
             
                continue
             
            print(space, end = "")
 
        print()
        alien -= 1
     
    alien = 1
 
    for i in range(4, 0, -1):
 
        for motu in range(alien, 0, -1):
            print(end = " ")
 
        for patlu in range(1, i + 1):
            print(space, end = "")
 
        for john in range(1, i):
            print(space, end = "")
 
        alien += 1
        print()
 
    alien = 3
 
    for i in range(2, 6):
 
        if ((i % 2) != 0):
         
            for motu in range(alien, 0, -1):
                print(" ", end = "")
 
            for patlu in range(1, i + 1):
                print(space, end = "")
 
        if ((i % 2) != 0):
            print()
            alien -= 1
 
 # @anoint.02
