import csv
import sqlite3

request = """
DELETE FROM table_fees 
WHERE timestamp = ? AND truck_number = ?
"""


def delete_wrong_fees(c: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            car_number, timestamp = row
            c.execute(request, (timestamp, car_number))
    print("Всё ошибачные штрафы удалены")


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()

        delete_wrong_fees(cursor, "wrong_fees.csv")
