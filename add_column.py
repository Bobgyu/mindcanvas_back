#!/usr/bin/env python3
"""
Drawing 테이블에 drawing_type 컬럼을 추가하는 스크립트
"""
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def add_drawing_type_column():
    try:
        # 데이터베이스 연결
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'mindcanvas_db'),
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASSWORD', 'password')
        )
        
        cur = conn.cursor()
        
        # drawing_type 컬럼 추가
        cur.execute("ALTER TABLE drawing ADD COLUMN IF NOT EXISTS drawing_type VARCHAR(50) DEFAULT 'normal'")
        conn.commit()
        print('✅ drawing_type 컬럼 추가 완료')
        
        cur.close()
        conn.close()
        print('🎉 성공!')
        
    except Exception as e:
        print(f'❌ 오류: {e}')

if __name__ == "__main__":
    add_drawing_type_column()
