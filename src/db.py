import sqlite3

def connect_db(db_name):
    return sqlite3.connect(db_name)


def create_table(conn):
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS news (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    unique_id TEXT NOT NULL UNIQUE,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            print("Table created successfully or already exists.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")


def insert_news_db(conn, unique_id, title, content):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO news (unique_id, title, content)
        VALUES (?, ?, ?)
    ''', (unique_id, title, content))
    conn.commit()


def get_all_news(conn):
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM news ORDER BY timestamp DESC')
        return cursor.fetchall()


def get_news_count(conn):
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM news')
        return cursor.fetchone()[0]


def delete_old_news(conn, limit):
    with conn:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM news
            WHERE id IN (
                SELECT id FROM news
                ORDER BY timestamp ASC
                LIMIT ?
            )
        ''', (limit,))


def manage_news_table(conn):
    news_count = get_news_count(conn)
    if news_count > 100:
        delete_old_news(conn, 20)

def check_news_exists(conn, unique_id):
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT EXISTS(SELECT 1 FROM news WHERE unique_id = ?)', (unique_id,))
        return cursor.fetchone()[0] == 1

# def main():
#     with connect_db('news.db') as conn:
#         create_table(conn)
#
#         # for i in range(123, 250):  # Insert 119 records for demonstration
#         #     insert_news(conn, f'UUID-{i:03}', f'News Title {i}', f'Content of news {i}')
#         #
#         # manage_news_table(conn)
#         #
#         # news = get_all_news(conn)
#         #
#         # for record in news:
#         #     print(record)


# if __name__ == '__main__':
#     main()