from threading import Lock, get_ident
import time
import concurrent.futures

s = time.time()
a = 1


def print_no1():
    locks[0].acquire()
    global a
    while a < 98:
        if locks[0].locked():
            print(f"Thread_{get_ident()}: {a}")
            a += 1
            locks[0].release()
            locks[1].acquire()
    print(f"Thread_1st finished")


def print_no2():
    global a
    while a < 99:
        if locks[1].locked():
            print(f"Thread_{get_ident()}: {a}")
            a += 1
            locks[1].release()
            locks[2].acquire()
    print(f"Thread_2nd finished")


def print_no3():
    global a
    while a < 100:
        if locks[2].locked():
            print(f"Thread_{get_ident()}: {a}")
            a += 1
            locks[2].release()
            locks[3].acquire()
    print(f"Thread_3rd finished")


def print_no4():
    global a
    while a < 101:
        if locks[3].locked():
            print(f"Thread_{get_ident()}: {a}")
            a += 1
            locks[3].release()
            locks[0].acquire()
    print(f"Thread_4th finished")


locks = [Lock() for _ in range(4)]

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(print_no1)
    executor.submit(print_no2)
    executor.submit(print_no3)
    executor.submit(print_no4)


f = time.time()

print(f"Total time: {f - s}")
