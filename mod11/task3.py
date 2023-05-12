import logging
import random
import threading
import time

MAX_TICKETS_TO_SOLD = random.randint(15, 25)
TOTAL_TICKETS = random.randint(8, 12)
MAX_SOLD_TICKETS = 3
ADD_TICKETS = random.randint(3, 6)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"max tickets to sold = {MAX_TICKETS_TO_SOLD}, total tickets = {TOTAL_TICKETS}")


class Director(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS
        global ADD_TICKETS
        global MAX_SOLD_TICKETS
        is_running = True
        added_tickets = TOTAL_TICKETS
        while is_running:
            with self.sem:
                if added_tickets >= MAX_TICKETS_TO_SOLD:
                    break
                if TOTAL_TICKETS <= MAX_SOLD_TICKETS:
                    if added_tickets + ADD_TICKETS >= MAX_TICKETS_TO_SOLD:
                        ADD_TICKETS = MAX_TICKETS_TO_SOLD - added_tickets
                    logger.info(f"Director is adding {ADD_TICKETS} tickets")
                    TOTAL_TICKETS += ADD_TICKETS
                    added_tickets += ADD_TICKETS
                    logger.info(f"Total tickets now: {TOTAL_TICKETS}")


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f'{self.name} sold one; {TOTAL_TICKETS} left')

        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


def main():
    semaphore = threading.Semaphore(1)
    director = Director(semaphore)
    sellers = []

    director.start()

    for _ in range(3):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()

    director.join()


if __name__ == '__main__':
    main()
