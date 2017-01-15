import numpy as np
import matplotlib.pyplot as plt

plt.ion()
mu, sigma = 100, 15
fig = plt.figure()
x = mu + sigma*np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
for i in range(50):
    x = mu + sigma*np.random.randn(10000)
    n, bins = np.histogram(x, bins, normed=True)
    for rect,h in zip(patches,n):
        rect.set_height(h)
    fig.canvas.draw()
