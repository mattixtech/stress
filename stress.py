"""
A trivial utility for consuming system resources.
"""
import multiprocessing
import sys
import time


def _log(log_msg):
    """
    Logs a message.

    :return: None
    """

    print(log_msg)


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

    pass


def stress_processes(n):
    """
    TODO

    :param n: the number of processes to spin
    :return: None
    """

    for _ in range(n):
        multiprocessing.Process(target=_spin).start()


def stress_ram(n):
    """
    TODO

    :param n: the amount of RAM in megabytes to allocate
    :return: None
    """

    try:
        # Each element takes approx 8 bytes
        # Multiply n by 1024**2 to convert from MB to Bytes
        l = [0] * int(((n / 8) * (1024 ** 2)))
        allocated_bytes = int(sys.getsizeof(l) / (1024 ** 2))
        _log("Allocated {} megabytes".format(allocated_bytes))
        #time.sleep(10)
    except MemoryError:
        # We didn't have enough RAM for our attempt, so we will recursively try
        # smaller amounts 10% smaller at a time
        stress_ram(int(n * 0.9))


if __name__ == '__main__':
    # spin_n(multiprocessing.cpu_count())
    # spin_n(2)
    start = time.time()
    stress_ram(1024 * 10)
    end = time.time()
    _log("Took {} seconds".format(round(end - start, 2)))
