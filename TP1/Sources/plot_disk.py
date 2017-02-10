import matplotlib.pyplot as pyplot
import numpy

# inspired by http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html

xTickMarks = ["azure A1", "azure A4"]
N = 2
disk_cached_reads = [3966.54, 4329.98]
disk_buffered_disk_reads = [21.96, 43.87]

ind = numpy.arange(N)
width = 0.35

fig = pyplot.figure()
fig.suptitle("hdparm disk benchmark")

ax = fig.add_subplot(121) # subplot(nbcol, nbligne, numfigure)
ax.bar(ind, disk_cached_reads, width)
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(min(disk_cached_reads)-1, max(disk_cached_reads)+1)
ax.set_xticks(ind)
ax.set_ylabel("timing cached reads (MB/s)")
xtickNames = ax.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

ax2 = fig.add_subplot(122)
ax2.bar(ind, disk_buffered_disk_reads, width)
ax2.set_xlim(-width,len(ind)+width)
ax2.set_ylim(min(disk_buffered_disk_reads)-1, max(disk_buffered_disk_reads)+1)
ax2.set_xticks(ind)
ax2.set_ylabel("timing buffered disk reads (MB/s)")
xtickNames = ax2.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

pyplot.tight_layout()
pyplot.subplots_adjust(top=0.9)

pyplot.show()

