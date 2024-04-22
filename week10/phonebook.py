import csv
import psycopg2

# Вставка данных из CSV-файла
def insert_from_csv(filename):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Пропустить заголовок
        for row in reader:
            cursor.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                row
            )
    
    conn.commit()
    cursor.close()
    conn.close()

# Вставка данных с консоли
def insert_from_console():
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()

    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cursor.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    
    conn.commit()
    cursor.close()
    conn.close()

# Обновление данных
def update_data(id, name, phone):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE phonebook SET name = %s, phone = %s WHERE id = %s",
        (name, phone, id)
    )
    
    conn.commit()
    cursor.close()
    conn.close()

# Запрос данных с фильтрами
def query_data(name=None, phone=None):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()

    query = "SELECT * FROM phonebook"
    params = []

    if name:
        query += " WHERE name = %s"
        params.append(name)
    
    if phone:
        query += " WHERE phone = %s"
        params.append(phone)

    cursor.execute(query, params)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

# Удаление данных
def delete_data(phone):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()

    cursor.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    
    conn.commit()
    cursor.close()
    conn.close()
