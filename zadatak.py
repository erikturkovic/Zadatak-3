import random
import time
import multiprocessing

def process_name(name):
    delay = random.random() * 0.9
    time.sleep(delay)
    print(f"PID: {multiprocessing.current_process().pid}, ime: {name}, delay: {delay} sekundi")

if __name__ == '__main__':
    input_number = 0
    request_time = int(input("Upiši broj vremena razmaka kašnjena između zahtjeva "))
    while input_number < 10:
        time.sleep(request_time)
        input_number+=1
        names = ['lmao','Erik', 'Filip', 'Nevup', 'Perica', 'Ela']
        processes = [multiprocessing.Process(target=process_name, args=(name,)) for name in names]
        for p in processes:
            p.start()