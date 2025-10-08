#!/usr/bin/env python3
"""
Drawing 테이블에 새로운 컬럼들을 추가하는 스크립트
"""
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def add_columns():
    # 데이터베이스 연결
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'mindcanvas_db'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'password')
    )

    cur = conn.cursor()

    try:
        # drawing_type 컬럼 추가
        cur.execute("ALTER TABLE drawing ADD COLUMN IF NOT EXISTS drawing_type VARCHAR(50) DEFAULT 'normal'")
        print('✅ drawing_type 컬럼 추가 완료')
        
        # original_image 컬럼 추가
        cur.execute("ALTER TABLE drawing ADD COLUMN IF NOT EXISTS original_image VARCHAR(255)")
        print('✅ original_image 컬럼 추가 완료')
        
        # title 컬럼 추가
        cur.execute("ALTER TABLE drawing ADD COLUMN IF NOT EXISTS title VARCHAR(255)")
        print('✅ title 컬럼 추가 완료')
        
        conn.commit()
        print('🎉 모든 컬럼이 성공적으로 추가되었습니다!')
        
    except Exception as e:
        print(f'❌ 오류 발생: {e}')
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    add_columns()
