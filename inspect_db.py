import sqlite3
import os

db_path = "/home/hanins/code/web3/apps/nofx/data.db"

if not os.path.exists(db_path):
    print(f"Error: Database not found at {db_path}")
    exit(1)

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("--- Traders ---")
    cursor.execute("SELECT id, name, strategy_id FROM traders")
    traders = cursor.fetchall()
    for t in traders:
        print(f"ID: {t[0]}, Name: {t[1]}, StrategyID: '{t[2]}'")

    print("\n--- Strategies ---")
    cursor.execute("SELECT id, name FROM strategies")
    strategies = cursor.fetchall()
    for s in strategies:
        print(f"ID: {s[0]}, Name: {s[1]}")

    conn.close()
except Exception as e:
    print(f"Error: {e}")
