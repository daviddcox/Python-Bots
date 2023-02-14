import threading

# Global variable
counter = 0

def increment_counter():
    global counter
    counter += 1

def decrement_counter():
    global counter
    counter -= 1

def thread_task():
    while True:
        increment_counter()

def thread_task2():
    global counter
    while True:
        print(counter)

def thread_task3():
    while True:
        decrement_counter()

def main_task():
    global counter
    counter = 0

    # Create two threads
    thread3 = threading.Thread(target=thread_task3)
    thread1 = threading.Thread(target=thread_task)
    thread2 = threading.Thread(target=thread_task2)

    # Start both threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    thread3.join()

    print("Counter: {}".format(counter))

if __name__ == '__main__':
    main_task()
