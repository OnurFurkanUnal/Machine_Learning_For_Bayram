# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np

# datamız
# third value color 1 is red 0 is blue
data = [[3, 1.5, 1],
        [2, 1, 0],
        [4, 1.5, 1],
        [3, 1, 0],
        [3.5, .5, 1],
        [2, .5, 0],
        [5.5, 1, 1],
        [1, 1, 0]]
mystery_flower = [4.5, 1]
print(data[1])

# network
#    o   flower type
#  /   \ w1,w2,b
# o      o length, width

w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

def sigmoid (x):
    return  1/(1 + np.exp(-x))
def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))

T = np.linspace(-5,5,10)
print(T)
Y = sigmoid(T)
print(Y)
#plt.plot(T,Y)
#plt.show(block=True)
plt.cla()

# scatter data
plt.axis([0,6,0,6])
plt.grid()
for i in range(len(data)):
        point = data[i]
        color = "r"
        if point[2] == 0:
                color = "blue"

        plt.scatter(point[0],point[1], c = color)
        #plt.show(block=True)
plt.show(block=True)

#training data
learning_rate = 0.001
costs = []
for i in range(100000):
        ri = np.random.randint(len(data))
        point = data[ri]

        z = point[0] * w1 + point[1] * w2 + b
        pred = sigmoid(z)

        target = point[2]
        cost = np.square(pred - target)

       # if i %1000 == 0:
       #         print(cost)
        costs.append(cost)
        dcost_pred = 2 * (pred - target)
        dpred_dz = sigmoid_p(z)
        dz_dw1 = point[0]
        dz_dw2 = point[1]
        dz_db = 1

        dcost_dz = dcost_pred * dpred_dz

        dcost_dw1 = dcost_dz * dz_dw1
        dcost_dw2 = dcost_dz * dz_dw2
        dcost_db = dcost_dz * dz_db

        w1 = w1 - learning_rate * dcost_dw1
        w2 = w2 - learning_rate * dcost_dw2
        b = b - learning_rate * dcost_db
plt.cla()
plt.plot(costs)
plt.show(block=True)

# seeing model prediction
for i in range(len(data)):
        point = data[i]
        print(point)
        z = point[0] * w1 + point[1] * w2 + b
        pred = sigmoid(z)
        print("pred: {}".format(pred))
z = mystery_flower[0] * w1 + mystery_flower[1] * w2 + b
pred = sigmoid(z)
print(pred)

# test
def which_flower(lenght, width):
        z = lenght * w1 + width * w2 + b
        pred = sigmoid(z)
        if pred < .5:
                print("blue")
        else:
                print("red")


which_flower(4 , 1.5)
