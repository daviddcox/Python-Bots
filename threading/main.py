import logging
import concurrent.futures


def thread_function(name):
    x = 0
    print(f'hey {name}')
    x += 1
    x /= 25
    x *= 1000
    print(x)


if __name__ == "__main__":
    formats = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formats, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
