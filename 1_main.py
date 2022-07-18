# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('furkan')

numpy.binary_repr(231)
print(numpy.binary_repr(231))

def NN (m1, m2, w1, w2, b):
    z = m1 * w1 + m2 * w2 + b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1+numpy.exp(-x))

w1 = numpy.random.randn()
w2 = numpy.random.randn()
b = numpy.random.randn()

print(NN(3 , 1.5 , w1 , w2 , b))
print(NN(2, .5 , w1 , w2 , b))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
