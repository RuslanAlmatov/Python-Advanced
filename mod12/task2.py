import psutil


def process_count(username: str) -> int:
    count = 0
    for process in psutil.process_iter():
        if process.username() == username:
            count += 1
    return count


def total_memory_usage(root_pid: int) -> float:
    total_memory = 0
    root_process = psutil.Process(root_pid)
    for child in root_process.children(recursive=True):
        memory_info = child.memory_info()
        total_memory += memory_info.rss
    total_memory += root_process.memory_info().rss
    total_memory_percent = total_memory / psutil.virtual_memory().total * 100
    return total_memory_percent


if __name__ == "__main__":
    print(process_count("el0"))
    print(total_memory_usage(1433))
