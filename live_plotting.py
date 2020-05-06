import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

'''
def rect(x, B):
    """
    create a rectangle function
    returns a numpy array that is 1 if |x| < w and 0 if |x| > w
    B is the rectangle width centered at 0
    x is the number of points in the array
    """

    B = int(B)
    x = int(x)

    high = np.ones(B)
    low1 = np.zeros(int(x/2 - B/2))
    x1 = np.append(low1, high)
    rect = np.append(x1, low1)

    if x > len(rect):
        rect = np.append(rect, 0)
    elif x < len(rect):
        rect = rect[:-1]

    return rect

'''
# matplotlib notebook


# constants and x array
pi = np.pi
length = 2000
x = np.linspace(-10, 10, length)

# create figure and axes
fig, (ax1, ax2) = plt.subplots(2, figsize=(12, 6))

# creating our line objects for the plots
# sinc, = ax1.plot(x, np.sin(x), '-b')
# sin,  = ax2.plot(x, np.sin(x), '-r')
counter = -1


def animate(B, t, d):
    """
    this function gets called by FuncAnimation
    each time called, it will replot with a different width "B"

    B: rect width

    return:
        sinc: ydata
        box: ydata
    """
    global counter
    ax2.cla()
    print(t)
    # print(d)
    # create our rect object
    counter = (counter + 1) % len(freq_steps)
    fc = t[counter]

    f = np.sin(2*pi*(x - 0.01*B)*fc)
    ax2.plot(x, f)
    # create our sinc object
    ax1.cla()
    F = (B / length) * np.sin(x * B / 2) / (x * B / 2)
    ax1.plot(x, F)

    # adjust the sinc plot height in a loop
    '''
    ax1.set_ylim(np.min(F), np.max(F))

    # format the ax1 yticks
    plt.setp(ax1, xticks=[-0.25, 0.25], xticklabels=['-1/4', '1/4'],
             yticks=[0, np.max(F)],
             yticklabels=['0', 'B={:.2f}'.format((B / length))])

    # format the ax2 xticks to move with the box
    plt.setp(ax2, yticks=[0, 1],
             xticks=[-1, -1 * B / length, 1 * B / length, 1],
             xticklabels=['-1', '-B/2', 'B/2', '1'])
    '''
    return ax1, ax2


def init():
    """
    initialize the figure
    """

    ax2.set_ylim(-0.2, 1.1)
    ax1.set_xlim(-10, 10)
    ax2.set_xlim(-10, 10)
    ax1.axhline(0, color='black', lw=1)
    ax2.axhline(0, color='black', lw=1)
    plt.rcParams.update({'font.size': 14})

    return ax1, ax2


# the FuncAnimation function iterates through our animate function
#  using the steps array

freq_step = 1
step = 10
freq_steps = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# freq_steps = np.arange(0, 10, freq_step)
steps = np.arange(10, 1000, step)
ani = FuncAnimation(fig, animate, steps, init_func=init, fargs=(freq_steps, 2),
                    interval=1, blit=False)

plt.show()
