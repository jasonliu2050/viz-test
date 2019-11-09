
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd


df = pd.read_csv('housing.data', sep='\s+', header=None)
# Setting columns to dataset
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']


# Fixing random state for reproducibility
np.random.seed(19680801)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
price = df["MEDV"]
figs = [df["TAX"],df["AGE"],df["B"],df["PTRATIO"],df["ZN"],df["INDUS"],df["NOX"],df["RAD"]]
colors = ['r', 'g', 'b', 'y', 'r', 'g', 'b', 'y']
yticks = [0, 1, 2, 3 ,4 ,5 ,6, 7]
for c, k in zip(colors, yticks):
    # Generate the random data for the y=k 'layer'.
    xs = price.to_numpy()
    ys = figs[7-k].to_numpy()

    # You can provide either a single color or an array with the same length as
    # xs and ys. To demonstrate this, we color the first bar of each set cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'

    # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    #ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)


ax.set_xlabel('House Price')
ax.set_ylabel('Number of Figures')
ax.set_zlabel('')

# On the y axis let's only label the discrete values that we have data for.
ax.set_yticks(yticks)

plt.show()