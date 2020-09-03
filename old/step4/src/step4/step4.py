'''
Created on Sep 2, 2020

@author: wade4
'''
import numpy as np

def main():
    mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3]) 
    mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7]) 
      
    # This will return dot product 
    res = np.dot(mat1,mat2) 
      
      
    # print resulted matrix 
    print(res) 

if __name__ == "__main__":
    main()
    