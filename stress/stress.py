"""
A trivial utility for consuming system resources.
"""
from __future__ import print_function

import argparse
import multiprocessing
import psutil
import signal
import sys
import time


def _spin():
    """
    Spin in an infinite loop.

    :return: None
    """

    while True:
        pass


def _parse_args():
    """
    Parse the command line arguments

    :return: the parsed arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cores",
                        help="The number of cores to stress")
    parser.add_argument("-m", "--memory",
                        help="The amount of memory in MB to allocate")

    return parser.parse_args()


def stress_processes(num_processes):
    """
    Starts a given number infinite processing loops.

    :param num_processes: the number of processes to spin
    :return: None
    """

    for _ in range(num_processes):
        multiprocessing.Process(target=_spin).start()


def stress_ram(ram_to_allocate_mb):
    """
    Attempts to allocate the given amount of RAM to the running Python process.

    :param ram_to_allocate_mb: the amount of RAM in megabytes to allocate
    :return: None
    """

    try:
        # Each element takes approx 8 bytes
        # Multiply n by 1024**2 to convert from MB to Bytes
        _ = [0] * int(((ram_to_allocate_mb / 8) * (1024 ** 2)))

        while True:
            # This is just to keep the process running until halted
            time.sleep(1)
    except MemoryError:
        # We didn't have enough RAM for our attempt, so we will recursively try
        # smaller amounts 10% smaller at a time
        stress_ram(int(ram_to_allocate_mb * 0.9))


def _cmd_line():
    """
    The command line entry point for this script.

    :return: None
    """

    arguments = _parse_args()
    cores_to_stress = int(arguments.cores) if arguments.cores else None
    memory_to_allocate = int(arguments.memory) if arguments.memory else None

    # This eats the interrupted exception when the process is terminated
    signal.signal(signal.SIGINT, lambda x, y: sys.exit(1))

    if not cores_to_stress and not memory_to_allocate:
        cores_to_stress = multiprocessing.cpu_count()
        memory_to_allocate = psutil.virtual_memory().total

    if cores_to_stress:
        # The CPU stress has to happen in another process since it is infinitely
        # CPU hungry
        multiprocessing.Process(target=stress_processes,
                                args=(cores_to_stress,)).start()
    if memory_to_allocate:
        # We can allocate RAM in this process
        stress_ram(memory_to_allocate)


if __name__ == '__main__':
    _cmd_line()
