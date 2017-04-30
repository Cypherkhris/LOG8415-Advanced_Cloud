import matplotlib.pyplot as pyplot
import numpy
import sys


def main():
    values = []
    timestamps = []
    filename = sys.argv[1]
    plotname = sys.argv[2]
    outputfilename = sys.argv[3]

    with open(filename, 'r') as f:
        lines = f.readlines()
        seconds = 0.5
        for line in lines:
            line = line.strip('\n')
            id, timestamp, value = line.split(';')
            value = float(value) * 0.001 * seconds # calcul en joules : W * s avec W = 0.001 * mW
            values.append(value)
            timestamps.append(timestamp)
            seconds += 0.5

    fig = pyplot.figure()
    fig.suptitle(plotname)

    ax = fig.add_subplot(111) # subplot(nbcol, nbligne, numfigure)
    ax.plot(timestamps, values)
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Consommation (J)')
    pyplot.tight_layout()
    pyplot.subplots_adjust(top=0.9)

    fig.savefig(outputfilename)

if __name__ == '__main__':
    main()

