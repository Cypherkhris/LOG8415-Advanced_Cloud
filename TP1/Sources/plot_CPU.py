import matplotlib.pyplot as pyplot
import numpy

# inspired by http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html

xTickMarks = ["azure A1", "azure A4"]
N = 2
CPU_total_time = [66.8626, 66.6122]
CPU_avg_request = [6.69, 6.66]

ind = numpy.arange(N)
width = 0.35

fig = pyplot.figure()
fig.suptitle("sysbench CPU benchmark")

ax = fig.add_subplot(121) # subplot(nbcol, nbligne, numfigure)
ax.bar(ind, CPU_total_time, width)
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(min(CPU_total_time)-1, max(CPU_total_time)+1)
ax.set_xticks(ind)
ax.set_ylabel("total time (s)")
xtickNames = ax.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

ax2 = fig.add_subplot(122)
ax2.bar(ind, CPU_avg_request, width)
ax2.set_xlim(-width,len(ind)+width)
ax2.set_ylim(min(CPU_avg_request)-1, max(CPU_avg_request)+1)
ax2.set_xticks(ind)
ax2.set_ylabel("avg time per request (ms)")
xtickNames = ax2.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

pyplot.tight_layout()
pyplot.subplots_adjust(top=0.9)

pyplot.show()

