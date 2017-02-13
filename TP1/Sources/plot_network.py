import matplotlib.pyplot as pyplot
import numpy

# inspired by http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html

xTickMarks = ["azure A1", "azure A4", "amazon T2", "amazon C4", "amazon M4", "amazon R4"]
N = 6
network_download = [1080.68, 1638.51, 370.52, 881.72, 804.7, 421.53]
network_upload = [390.24, 266.74, 166.03, 145, 166.70, 172.51]

ind = numpy.arange(N)
width = 0.35

fig = pyplot.figure()
fig.suptitle("SpeedTest network benchmark")

ax = fig.add_subplot(121) # subplot(nbcol, nbligne, numfigure)
ax.bar(ind, network_download, width)
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(min(network_download)-1, max(network_download)+1)
ax.set_xticks(ind)
ax.set_ylabel("download (Mbit/s)")
xtickNames = ax.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

ax2 = fig.add_subplot(122)
ax2.bar(ind, network_upload, width)
ax2.set_xlim(-width,len(ind)+width)
ax2.set_ylim(min(network_upload)-1, max(network_upload)+1)
ax2.set_xticks(ind)
ax2.set_ylabel("upload (Mbit/s)")
xtickNames = ax2.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

pyplot.tight_layout()
pyplot.subplots_adjust(top=0.9)

pyplot.show()

