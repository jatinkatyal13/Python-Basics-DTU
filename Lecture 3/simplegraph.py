import matplotlib.pyplot as plt

if __name__ == "__main__":

    x = [1,2,3]
    y = [2,4,1]

    plt.title('My first graph!')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.plot(x,y)
    plt.show()