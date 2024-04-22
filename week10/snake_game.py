import psycopg2

# Вставка пользователя
def insert_user(username):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()

    cursor.execute("INSERT INTO user (username) VALUES (%s)", (username,))
    
    conn.commit()
    cursor.close()
    conn.close()

# Получение уровня пользователя
def get_user_level(username):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()

    cursor.execute(
        "SELECT level FROM user_score JOIN user ON user_score.user_id = user.id WHERE user.username = %s ORDER BY level DESC LIMIT 1",
        (username,)
    )
    
    level = cursor.fetchone()[0] if cursor.rowcount > 0 else None

    cursor.close()
    conn.close()

    return level

# Сохранение состояния и оценки
def save_score(user_id, level, score, paused):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_user",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO user_score (user_id, level, score, paused) VALUES (%s, %s, %s, %s)",
        (user_id, level, score, paused)
    )
    
    conn.commit()
    cursor.close()
    conn.close()
