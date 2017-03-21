import matplotlib.pyplot as pyplot

# inspired by http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html

xIterations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
hadoop = [4.2, 4.099, 4.043, 4.133, 4.078, 4.104, 4.118, 4.128, 4.060, 4.018]
spark = [6.615, 6.900, 6.715, 6.924, 7.024, 6.930, 6.929, 6.947, 6.742, 6.458]

fig = pyplot.figure()
fig.suptitle("WordCount : Hadoop vs Spark")

ax = fig.add_subplot(111) # subplot(nbcol, nbligne, numfigure)
ax.plot(xIterations, hadoop, label="Hadoop")
ax.plot(xIterations, spark, label="Spark")
ax.set_xlabel("iterations")
ax.set_ylabel("real time (s)")
ax.set_ylim(0,8)
ax.legend(loc="lower right")

pyplot.tight_layout()
pyplot.subplots_adjust(top=0.9)

pyplot.show()