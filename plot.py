# plot.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    with open('data.json', 'r') as f:
        data = json.load(f)
    number = float(data['number'])
    line.set_ydata(np.sin(x + number * i / 50.0))  # update the data
    return line,

ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)

plt.show()