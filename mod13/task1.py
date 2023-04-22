import sqlite3

request = """
SELECT COUNT(*) 
FROM 'table_truck_with_vaccine'
WHERE (temperature_in_celsius NOT BETWEEN 16 AND 20)  AND (truck_number = ?)
"""


def check_if_vaccine_has_spoiled(
        c: sqlite3.Cursor,
        truck_number: str,
) -> bool:
    result = c.execute(request, (truck_number,)).fetchone()[0]
    if result >= 3:
        return False
    return True


with sqlite3.connect("hw.db") as conn:
    cursor = conn.cursor()
    truck_number = input("Введите номер грузовика: ")
    if check_if_vaccine_has_spoiled(cursor, truck_number):
        print("Вакцина не испорчена")
    else:
        print("Вакцина испорчена")
