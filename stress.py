"""
A trivial utility for consuming system resources.
"""
import multiprocessing
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

    # TODO: take -p n processes to spin and -m n megabytes of RAM to allocate

    pass


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
        _list = [0] * int(((ram_to_allocate_mb / 8) * (1024 ** 2)))

        while True:
            time.sleep(1)
    except MemoryError:
        # We didn't have enough RAM for our attempt, so we will recursively try
        # smaller amounts 10% smaller at a time
        stress_ram(int(ram_to_allocate_mb * 0.9))


if __name__ == '__main__':
    # TODO: Parse the args and execute the correct stress
    # TODO: Default to spinning max core count and allocating max phys RAM
    pass
