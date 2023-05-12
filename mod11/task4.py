import queue
import random
import threading
import time


class Task:
    def __init__(self, priority):
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(priority={self.priority})"


class Producer(threading.Thread):
    def __init__(self, task_queue):
        super().__init__()
        self.task_queue = task_queue
        print("Producer: Running")

    def run(self):
        for i in range(10):
            task = Task(random.randint(0, 10))
            self.task_queue.put(task)


class Consumer(threading.Thread):
    def __init__(self, task_queue):
        super().__init__()
        self.task_queue = task_queue
        print("Consumer: Running")

    def run(self):
        while True:
            try:
                task = self.task_queue.get(block=False)
            except queue.Empty:
                break
            start_time = time.time()
            self.random_sleep()
            end_time = time.time()
            print(f">running {task} sleep({end_time - start_time})")
            self.task_queue.task_done()

    def random_sleep(self):
        time.sleep(random.random())


def main():
    task_queue = queue.PriorityQueue()
    task_queue.join()
    producer = Producer(task_queue)
    consumer = Consumer(task_queue)

    producer.start()
    producer.join()

    consumer.start()
    consumer.join()
    print("Producer: Done")
    print("Consumer: Done")


if __name__ == "__main__":
    main()
