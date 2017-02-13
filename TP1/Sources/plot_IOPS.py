import matplotlib.pyplot as pyplot
import numpy

# inspired by http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html

xTickMarks = ["azure A1", "azure A4", "amazon T2", "amazon C4", "amazon M4", "amazon R4"]
N = 6
iops_sequential_output = [490, 501, 1201.2, 1296.2, 1088.8, 1119.8]
iops_sequential_output_latency = [22436, 22702, 7137, 6217.4, 7403.4, 7245.6]
iops_sequential_input = [1808, 2082, 4872.2, 5900.6, 4998.4, 4888.2]
iops_sequential_input_latency = [33882, 10888, 2317.6, 1395.2, 1635.6, 1700.4]
iops_random_seeks = [882.7, 2843, 9387, 0, 0, 0]
iops_random_seeks_latency = [203000, 19529, 4638.4, 34, 1055.2, 319.4]

ind = numpy.arange(N)
width = 0.35

fig = pyplot.figure()
fig.suptitle("hdparm disk benchmark")

ax = fig.add_subplot(231) # subplot(nbcol, nbligne, numfigure)
ax.bar(ind, iops_sequential_output, width)
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(min(iops_sequential_output)-1, max(iops_sequential_output)+1)
ax.set_xticks(ind)
ax.set_ylabel("sequential output per char (K/s)")
xtickNames = ax.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

ax2 = fig.add_subplot(232)
ax2.bar(ind, iops_sequential_output_latency, width)
ax2.set_xlim(-width,len(ind)+width)
ax2.set_ylim(min(iops_sequential_output_latency)-1, max(iops_sequential_output_latency)+1)
ax2.set_xticks(ind)
ax2.set_ylabel("sequential output latency per char (us)")
xtickNames = ax2.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

ax3 = fig.add_subplot(233)
ax3.bar(ind, iops_sequential_input, width)
ax3.set_xlim(-width,len(ind)+width)
ax3.set_ylim(min(iops_sequential_input)-1, max(iops_sequential_input)+1)
ax3.set_xticks(ind)
ax3.set_ylabel("sequential input per char (K/s)")
xtickNames = ax3.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

ax4 = fig.add_subplot(234)
ax4.bar(ind, iops_sequential_input_latency, width)
ax4.set_xlim(-width,len(ind)+width)
ax4.set_ylim(min(iops_sequential_input_latency)-1, max(iops_sequential_input_latency)+1)
ax4.set_xticks(ind)
ax4.set_ylabel("sequential input latency per char (us)")
xtickNames = ax4.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

ax5 = fig.add_subplot(235)
ax5.bar(ind, iops_random_seeks, width)
ax5.set_xlim(-width,len(ind)+width)
ax5.set_ylim(min(iops_random_seeks)-1, max(iops_random_seeks)+1)
ax5.set_xticks(ind)
ax5.set_ylabel("random seeks (/s)")
xtickNames = ax5.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

ax6 = fig.add_subplot(236)
ax6.bar(ind, iops_random_seeks_latency, width)
ax6.set_xlim(-width,len(ind)+width)
ax6.set_ylim(min(iops_random_seeks_latency)-1, max(iops_random_seeks_latency)+1)
ax6.set_xticks(ind)
ax6.set_ylabel("random seeks latency (us)")
xtickNames = ax6.set_xticklabels(xTickMarks)
pyplot.setp(xtickNames, rotation=45, fontsize=10)

pyplot.tight_layout()
pyplot.subplots_adjust(top=0.9)

pyplot.show()

