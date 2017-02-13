import matplotlib.pyplot as pyplot
import numpy

# inspired by http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html

xTickMarks = ["azure A1", "azure A4", "amazon T2", "amazon C4", "amazon M4", "amazon R4"]
N = 6
memory_bogo_ops = [27012.61, 26969.51, 34745.96, 34739.016, 34718.206, 34725.14]

ind = numpy.arange(N)
width = 0.35

fig = pyplot.figure()
fig.suptitle("stress-ng memory benchmark")

ax = fig.add_subplot(111) # subplot(nbcol, nbligne, numfigure)
ax.bar(ind, memory_bogo_ops, width)
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(min(memory_bogo_ops)-1, max(memory_bogo_ops)+1)
ax.set_xticks(ind)
ax.set_ylabel("bogo operations with user+system time (op/s)")
xtickNames = ax.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

pyplot.tight_layout()
pyplot.subplots_adjust(top=0.9)

pyplot.show()

