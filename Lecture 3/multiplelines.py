import matplotlib.pyplot as plt

if __name__ == "__main__" :
    # line 1 points
    x1 = [1,2,3]
    y1 = [2,4,1]

    # line 2 points
    x2 = [1,2,3]
    y2 = [4,1,3]

    plt.style.use('ggplot')

    plt.plot(x1, y1, label = "line 1", color = "green", linestyle = "dotted")
    plt.plot(x2, y2, label = "line 2", linestyle = "dashed")

    # available customisation options
    # plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
    #      marker='o', markerfacecolor='blue', markersize=8)

    plt.legend()
    plt.show()
