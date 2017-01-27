#!/usr/bin/env python

# Script principal
# "For each instance type, you should execute your selected benchmarks at least 5 times and take the average."

import script_CPU
import script_IO

def main():
    script_CPU.main()
    script_IO.main()

if __name__ == '__main__':
    main()
