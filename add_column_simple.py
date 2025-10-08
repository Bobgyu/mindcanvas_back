import psycopg2
import os

def add_column():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='mindcanvas_db',
            user='postgres',
            password='password'
        )
        
        cur = conn.cursor()
        cur.execute("ALTER TABLE drawing ADD COLUMN IF NOT EXISTS drawing_type VARCHAR(50) DEFAULT 'normal'")
        conn.commit()
        print('Column added successfully')
        
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    add_column()
