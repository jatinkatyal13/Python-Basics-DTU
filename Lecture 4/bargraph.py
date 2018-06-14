import matplotlib.pyplot as p

if __name__ == "__main__":
    # x-coordinates of left sides of bars 
    left = [1, 2, 3, 4, 5]
    # heights of bars
    height = [10, 24, 36, 40, 5]
    # labels for bars
    tick_label = ['one', 'two', 'three', 'four', 'five']
    p.xlabel('x - axis')
    p.ylabel('y - axis')
    p.title('My bar chart!')
    # plotting a bar chart
    p.bar(left, height, tick_label = tick_label,
            width = 0.5, color = ['red', 'blue', 'green'])
    p.show()