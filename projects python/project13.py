from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(title=" Take Rest ",
            message="Bohot der ho gayi betha h padh rha hai ya youtube dekh rha hai pata nhi par uth jaa abb",
            timeout=2)
            
        time.sleep(5)

