import time
import multiprocessing

def deposite(balance,lock):
    for i in range(100):
        lock.acquire()
        balance.value += 1
        lock.release()

def withdraw(balance,lock):
    for i in range(100):
        lock.acquire()
        balance.value -= 1
        lock.release()

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    balance = multiprocessing.Value('i', 100)  # Shared integer value initialized to 100
    t=time.time()
    t1 = multiprocessing.Process(target=deposite, args=(balance, lock))
    t2 = multiprocessing.Process(target=withdraw, args=(balance, lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Final balance: {balance.value}")
    print("time taken:", time.time() - t)