import numpy as np

def sigmoid(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))
    
X = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])
                
y = np.array([[0],
            [1],
            [1],
            [0]])

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,3)) - 1
syn2 = 2*np.random.random((3,1)) - 1

for j in range(100000):
    x = 100
    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = sigmoid(np.dot(l0,syn0))
    l2 = sigmoid(np.dot(l1,syn1))
    l3 = sigmoid(np.dot(l2,syn2))
    # print("layer 0")
    # print(l0)
    # print()
    # print("layer 1")
    # print(l1)
    # print()
    # print("layer 2")
    # print(l2)
    # print()

    # how much did we miss the target value?
    l3_error = y - l3
    
    if (j% 1000) == 0:
        print ("Error:" + str(np.mean(np.abs(l3_error))))
        
    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l3_delta = l3_error*sigmoid(l3,deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l2_error = l3_delta.dot(syn2.T)
    
    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error * sigmoid(l2,deriv=True)

    l1_error = l2_delta.dot(syn1.T)
    
    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * sigmoid(l1,deriv=True)

    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print()
print(l1)
print()
print(l2)
print()
print(l3)

"""
structure
        
        0   ---
0 ---               0    ---
        0   ---
0 ---               0    ---   0    ---
        0   ---
0 ---               0    ---
        0   ---    

^       ^           ^           ^
^       ^           ^           ^
l0      l1         l2           l3     
"""