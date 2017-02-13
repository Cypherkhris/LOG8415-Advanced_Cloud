import matplotlib.pyplot as pyplot
import numpy

# inspired by http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html

xTickMarks = ["azure A1", "azure A4", "amazon T2", "amazon C4", "amazon M4", "amazon R4"]
N = 6
io = [39.9, 33.5, 74.44, 145, 131, 103]

ind = numpy.arange(N)
width = 0.35

fig = pyplot.figure()
fig.suptitle("dd IO benchmark")

ax = fig.add_subplot(111) # subplot(nbcol, nbligne, numfigure)
ax.bar(ind, io, width)
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(min(io)-1, max(io)+1)
ax.set_xticks(ind)
ax.set_ylabel("I/O (MB/s)")
xtickNames = ax.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

pyplot.tight_layout()
pyplot.subplots_adjust(top=0.9)

pyplot.show()

