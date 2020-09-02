'''
Created on Sep 2, 2020

@author: wade4
'''
import numpy as np

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

def main():
    inputValues = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])                   
    outputValues = np.array([[0],[1],[1],[0]])
    np.random.seed(1)
    # randomly initialize our weights with mean 0
    inputMiddleWeights = 2*np.random.random((3,4)) - 1
    middleOutputWeights = 2*np.random.random((4,1)) - 1
    
    for j in range(60000):
    
        # Feed forward through layers 0, 1, and 2
        inputLayer = inputValues
        middleLayer = nonlin(np.dot(inputLayer,inputMiddleWeights))
        outputLayer = nonlin(np.dot(middleLayer,middleOutputWeights))
    
        # how much did we miss the target value?
        outputLayerError = outputValues - outputLayer
        
        if (j% 10000) == 0:
            print("Error:" + str(np.mean(np.abs(outputLayerError))))
            
        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        outputLayerDelta = outputLayerError*nonlin(outputLayer,deriv=True)
    
        # how much did each middleLayer value contribute to the outputLayer error (according to the weights)?
        middleLayerError = outputLayerDelta.dot(middleOutputWeights.T)
        
        # in what direction is the target middleLayer?
        # were we really sure? if so, don't change too much.
        middleLayerDelta = middleLayerError * nonlin(middleLayer,deriv=True)
    
        middleOutputWeights += middleLayer.T.dot(outputLayerDelta)
        inputMiddleWeights += inputLayer.T.dot(middleLayerDelta)

if __name__ == "__main__":
    main()
    