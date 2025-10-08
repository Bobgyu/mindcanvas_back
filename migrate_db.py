from app import app, db
import psycopg2

def add_drawing_type_column():
    with app.app_context():
        try:
            # 직접 SQL 실행 (새로운 방식)
            with db.engine.connect() as conn:
                conn.execute(db.text("ALTER TABLE drawing ADD COLUMN IF NOT EXISTS drawing_type VARCHAR(50) DEFAULT 'normal'"))
                conn.commit()
            print("drawing_type column added successfully")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    add_drawing_type_column()
