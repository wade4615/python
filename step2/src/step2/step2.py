'''
Created on Sep 2, 2020

@author: wade4
'''


def main():
    nterms = int(input("How many terms? "))
    
    # first two terms
    n1, n2 = 0, 1
    count = 0
    
    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence up to", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

           
if __name__ == "__main__":
    main()
    
