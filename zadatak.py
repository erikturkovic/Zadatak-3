import random
import time
import multiprocessing

def process_name(name):
    delay = random.random() * 5
    time.sleep(delay)
    print(f"PID: {multiprocessing.current_process().pid}, ime: {name}, delay: {delay} sekundi")

if __name__ == '__main__':
    while True:
        input("Enter za početak")
        names = ['lmao','Erik', 'Filip', 'Nevup', 'Perica', 'Ela']
        processes = [multiprocessing.Process(target=process_name, args=(name,)) for name in names]
        for p in processes:
            p.start()
        for p in processes:
            p.join()