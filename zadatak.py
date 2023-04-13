import random
import time
import multiprocessing

def process_name(name):
    delay = random.random() * 0.9
    time.sleep(delay)
    print(f"PID: {multiprocessing.current_process().pid}, ime: {name}, delay: {delay} sekundi")

if __name__ == '__main__':
    while True:
        if input("Stisni Enter za početak, napiši 'end' za izlazak: ") == 'end':
            break
        names = ['lmao','Erik', 'Filip', 'Nevup', 'Perica', 'Ela']
        processes = [multiprocessing.Process(target=process_name, args=(name,)) for name in names]
        for p in processes:
            p.start()