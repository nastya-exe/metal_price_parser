import sqlite3
from config import database_url


def save_price_to_db(metal, price, date):
    db = sqlite3.connect(database_url)
    cursor = db.cursor()

    if metal == 'gold':
        cursor.execute("""
            INSERT INTO gold_price(price, date)
            VALUES (?, ?)
        """, (price, date))

    elif metal == 'silver':
        cursor.execute("""
            INSERT INTO silver_price(price, date)
            VALUES (?, ?)
        """, (price, date))

    db.commit()
    db.close()


def select_week_graph(metal: str):
    db = sqlite3.connect(database_url)
    cursor = db.cursor()

    if metal == 'gold':
        cursor.execute("""
            SELECT price, date FROM gold_price
            WHERE date IN (
                SELECT MAX(date) FROM gold_price
                WHERE date >= DATETIME('now', '-7 days')
                GROUP BY DATE(date)
            )
            ORDER BY date ASC;
        """)
    elif metal == 'silver':
        cursor.execute("""
            SELECT price, date FROM silver_price
            WHERE date IN (
                SELECT MAX(date) FROM silver_price
                WHERE date >= DATETIME('now', '-7 days')
                GROUP BY DATE(date)
            )
            ORDER BY date ASC;
        """)

    rows = cursor.fetchall()

    db.close()

    return rows


def select_mont_graph(metal: str):
    db = sqlite3.connect(database_url)
    cursor = db.cursor()

    if metal == 'gold':
        cursor.execute("""
            SELECT price, date FROM gold_price
            WHERE date IN (
                SELECT MAX(date) FROM gold_price
                WHERE date >= DATETIME('now', '-30 days')
                GROUP BY DATE(date)
            )
            ORDER BY date ASC;
        """)
    elif metal == 'silver':
        cursor.execute("""
            SELECT price, date FROM silver_price
            WHERE date IN (
                SELECT MAX(date) FROM silver_price
                WHERE date >= DATETIME('now', '-30 days')
                GROUP BY DATE(date)
            )
            ORDER BY date ASC;
        """)

    rows = cursor.fetchall()

    db.close()

    return rows


def select_day_graph(metal):
    db = sqlite3.connect(database_url)
    cursor = db.cursor()

    if metal == 'gold':
        cursor.execute("""
            SELECT price, date FROM gold_price
            WHERE date(date) = date('now')
            ORDER BY date;
        """)
    elif metal == 'silver':
        cursor.execute("""
            SELECT price, date FROM silver_price
            WHERE date(date) = date('now')
            ORDER BY date;
        """)

    rows = cursor.fetchall()

    db.close()

    return rows


def get_last_price(metal):
    db = sqlite3.connect(database_url)
    cursor = db.cursor()

    if metal == 'gold':
        cursor.execute("""
            SELECT price FROM gold_price
            ORDER BY date DESC
            LIMIT 1;
        """)
    elif metal == 'silver':
        cursor.execute("""
            SELECT price FROM silver_price
            ORDER BY date DESC
            LIMIT 1;
        """)

    rows = cursor.fetchall()

    db.close()

    return rows[0]


# if __name__ == '__main__':
#     save_price_to_db('silver', 900, '2025-09-12')
#     save_price_to_db('silver', 850, '2025-09-11')
#     save_price_to_db('silver', 990, '2025-09-10')
#     save_price_to_db('silver', 820, '2025-09-09')
#     save_price_to_db('silver', 950, '2025-09-08')
#     save_price_to_db('silver', 888, '2025-09-07')
#     save_price_to_db('silver', 906, '2025-09-06')
#     save_price_to_db('silver', 890, '2025-09-05')
