# This program prints number 1 to 10 with a forloop

import threading
import time

def main():
    for i in range(1, 11):
        time.sleep(1)
        print(i)

threading.Thread(target=main).start()
